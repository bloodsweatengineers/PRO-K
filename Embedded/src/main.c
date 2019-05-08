#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <util/delay.h>

#define _BAUD 9600

void Init_UART(void) {

	DDRD |= (1<<PD1);
	DDRD &= ~(1<<PD0);

	uint16_t setting = (((F_CPU>>2)/_BAUD)-1)>>1;
	UCSR0A = 1 << U2X0;

	UBRR0H = setting >> 8;
	UBRR0L = setting;

	UCSR0B |= (1<<RXEN0) | (1<<TXEN0);

	UCSR0C = (3<<UCSZ00);
}

void flush(void) {
	unsigned char dummy;
	while(UCSR0A & (1<<RXC0)) dummy = UDR0;
}

char recieve(void) {
	while(!(UCSR0A & (1<<RXC0)));
	return (char) UDR0;
}

void transmit(char c) {

	while (!(UCSR0A & (1<<UDRE0)));
	UDR0 = c;
} 
 
void transmit_str(char *c) { 
	for(int i=0; i<strlen(c); i++) {
		transmit(c[i]);
	}
}

enum tok_t {
	REJECT,
	FREQUENCY 
};

struct token {
	enum tok_t	tok;
	int32_t		value;
};

enum state {
	BEGIN,
	PARAMETER,
	VALUE,
	END 
};

enum tok_t validate_parameter(char *c) {
	return FREQUENCY;
}

int32_t validate_value(char *c) {
	int32_t val = 0;
	uint32_t multiplier = 1;

	for(int i=0; i<strlen(c); i++) {
		if((c[i] >= '0') && (c[i] <= '9')) {
			val *= multiplier;
			val += c[i] - '0';
			multiplier *= 10;
		} else {
			return -1;
		}
	}

	return val;
}

struct token parser(void) {
	enum state parser_state = BEGIN;
	struct token tok;
	bool end_parse = false;
	char buffer[30];
	int index = 0;

	char c;
	while(!end_parse) {
		c = recieve();
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
				} else if (c == ' ') {
					parser_state = VALUE;
					tok.tok = validate_parameter(buffer);
					index = 0;
				} else {
					buffer[index] = c;
					index++;
				}
				break;
			case VALUE:
				if(c == '\r') {
					parser_state = END;
					tok.value = validate_value(buffer);
				} else {
					buffer[index] = c;
					index++;
				}
			case END:
				if(c == '\n') {
					end_parse = true;
				} else {
					end_parse = true;
					tok.tok = REJECT;
				}
				break;
		}
	}
	flush();
	return tok;
}

void main(void) {

	Init_UART();

	while(1) {
		struct token tok = parser();

		if(tok.tok == REJECT) {
			transmit_str("REJ\r\n");
		} else if(tok.tok == FREQUENCY) {
			transmit_str("OK FREQUENCY \r\n");
		} else {
			transmit_str("ERROR\r\n");
		}
	}
}
