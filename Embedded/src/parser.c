#include "parser.h"

void parser_init(struct parser *parser, enum command_type *command_type) {
	parser->command_type = command_type;
}

void parser_switch(struct parser *parser, enum command_type *command_type) {
	parser->command_type = command_type;
}

struct token parser_parse_command(struct parser *parser) {

	switch(*(parser->command_type)) {
		case BINARY:
			return parser_parse_bin_command(parser);
		case STRING:
			return parser_parse_str_command(parser);
	}
}

unsigned char calc_crc8(unsigned char *buffer, int buffer_index) {
	unsigned char crc = 0;

	for(int i=0; i < buffer_index; i++) {
		crc = _crc8_ccitt_update(crc, buffer[i]);
	}

	return crc;
}

struct token parser_parse_bin_command(struct parser *parser) {
	unsigned char c;
	unsigned char buffer[6];
	uint8_t buffer_index = 0;
	struct token token = token_reject();

	c = uart_recieve();
	if(c != 0x24) {
		return token_reject();
	}

	buffer[buffer_index] = c;
	buffer_index++;

	c = uart_recieve();
	token.tok = retrieve_bin_command(c);
	token.channel = retrieve_bin_channel(c);

	if(token.tok == REJECT || token.channel > 4) {
		return token_reject();
	}

	buffer[buffer_index] = c;
	buffer_index++;

	int32_t value = 0;
	for(int i=0; i<3; i++) {
		c = uart_recieve();
		buffer[buffer_index] = c;
		buffer_index++;
		value += c;
		value <<= 8;
	}

	if(check_bin_value(c, value) == -1) {
		return token_reject();
	}

	token.value = value;

	unsigned char crc = calc_crc8(buffer, buffer_index);
	c = uart_recieve();
	if(c != crc) {
		return token_reject();
	}

	buffer[buffer_index] = c;
	buffer_index++;

	uart_flush();

	return token;
}

struct token parser_parse_str_command(struct parser *parser) {
	bool end_parse = false;
	struct token token = token_reject();
	enum parser_state state = BEGIN;

	char buffer[30];
	int index = 0;
	memset(buffer, 0, 30);

	char c;
	while(!end_parse) {
		c = uart_recieve();
		switch(state) {
			case BEGIN:
				if(c == '%') {
					state = PARAMETER;
				} else {
					return token_reject();
				}
				break;
			case PARAMETER:
				switch(c) {
					case '\r':
						state = END;
						break;
					case ' ':
						state = VALUE;
						break;
					case '_':
						state = CHANNEL;
						break;
					default:
						buffer[index] = c;
						index++;
						break;
				}

				if(state != PARAMETER) {
					token.tok = retrieve_str_command(buffer);
					memset(buffer, 0, 30);
					index = 0;
				}
				break;
			case CHANNEL:
				if(c >= '0' && c <= '9') {
					token.channel = c - '0';
				} else if (c == ' ') {
					state = VALUE;
				} else {
					return token_reject();
				}
				break;
			case VALUE:
				if(c == '\r') {
					state = END;
					token.value = get_str_value(buffer);
					if(token.value == -2) {
						return token_reject();
					}
					memset(buffer,0,30);
					index = 0;
				} else {
					buffer[index] = c;
					index++;
				}
				break;
			case END:
				if(c == '\n') {
					end_parse = true;
				} else {
					return token_reject();
				}
				break;
			default:
				break;
		}
	}

	uart_flush();
	return token;
}
