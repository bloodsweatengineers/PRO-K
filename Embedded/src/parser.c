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
	uint8_t command = (uint8_t) command;
	token.tok = retrieve_bin_command(c);
	token.channel = retrieve_bin_channel(c);

	if(token.tok == REJECT || token.channel > 3) {
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

	if(check_bin_value(command, value) == -1) {
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
	return (struct token) {REJECT, -1, -1};
	/*
	bool end_parse = false;
	struct token token;
	enum parser_state state;

	char c;
	while(!end_parse) {
		c = uart_recieve();
		switch(state) {
			case BEGIN:
				if(c == '%') {
					state = PARAMETER;
				} else {
					return Token_Reject();
				}
				break;
			case PARAMETER:

		}
	}

	uart_flush();
	return token;
	*/
}

/*
enum tok_t validate_parameter(char *c) {
	if(strcmp(c, "frequency") == 0) {
		return FREQUENCY;
	} else if(strcmp(c, "phaseshift") == 0) {
		return PHASESHIFT;
	} else if(strcmp(c, "amplitude") == 0) {
		return AMPLITUDE;
	} else if(strcmp(c, "pwmfrequency") == 0) {
		return PWM_FREQUENCY;
	} else {
		return REJECT;
	}
} 

int32_t validate_value(char *c) {
	int32_t val = 0;

	for(int i=0; i<strlen(c); i++) {
		if((c[i] >= '0') && (c[i] <= '9')) {
			val *= 10;
			val += c[i] - '0';
		} else {
			return -1;
		}
	}

	return val;
}

struct token parser(void) {
	enum state parser_state = BEGIN;
	struct token tok = {REJECT, -1, -1};
	bool end_parse = false;
	char buffer[30];
	int index = 0;

	memset(buffer, 0, 30);

	char c;
	while(!end_parse) {
		c = uart_recieve();
		switch(parser_state) {
			case BEGIN:
				if(c == '%') {
					parser_state = PARAMETER;
				} else {
					tok.tok = REJECT;
					end_parse = true;
				}
				break;
			case PARAMETER:
				if(c == '\r') {
					parser_state = END;
					tok.tok = validate_parameter(buffer);
					memset(buffer,0,30);
					index = 0;
				} else if (c == ' ') {
					parser_state = VALUE;
					tok.tok = validate_parameter(buffer);
					memset(buffer,0,30);
					index = 0;
				} else if (c == '_') {
					parser_state = CHANNEL;
					tok.tok = validate_parameter(buffer);
					memset(buffer,0,30);
					index = 0;
				} else {
					buffer[index] = c;
					index++;
				}
				break;
			case CHANNEL:
				if(c >= '0' && c <= '9') {
					tok.channel = (uint8_t)(c - '0');
				} else if(c == ' ') {
					parser_state = VALUE;
				} else {
					end_parse = true;
					tok.tok = REJECT;
				}
				break;
			case VALUE:
				if(c == '\r') {
					parser_state = END;
					tok.value = validate_value(buffer);
					memset(buffer,0,30);
				} else {
					buffer[index] = c;
					index++;
				}
				break;
			case END:
				if(c == '\n') {
					end_parse = true;
				} else {
					end_parse = true;
					tok.tok = REJECT;
				}
				break;
			default:
				break;
		}
	}

	uart_flush();
	return tok;
}
*/
