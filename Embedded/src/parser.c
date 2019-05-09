#include "parser.h"

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
