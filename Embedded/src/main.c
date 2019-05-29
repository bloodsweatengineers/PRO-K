#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {

	cli();
	struct config conf;
	struct parser parser;		// deze erbij gemaakt voor parser_init
	enum command_type command_type = BINARY;	// deze erbij gemaakt voor parser_init
	
	uart_init();
	parser_init(&parser, &command_type);

	DDRD = 0;
	DDRB = 0;
	DDRD |= (1<<6 | 1<<3 | 1<<5);
	DDRB |= (1<<1 | 1<<3);

	TCCR1A = 0;
	TCCR1A |= (1<<COM1A0);
	TCCR1B = 0;
	TCCR1B |= (1<<WGM12) | (1<<CS10);
	TIMSK1 |= (1<<OCIE1A);
	OCR1A = 1250;

	TCCR2A = 0;
	TCCR2A |= (1 <<COM2A1 | 1<<COM2B1 | 1<<WGM20 | 1<<WGM21);
	TCCR2B = 0;
	TCCR2B |= 1<<CS20;

	TCCR0A = 0;
	TCCR0A |= (1 <<COM0A1 | 1<<COM0B1 | 1<<WGM00 | 1<<WGM01);
	TCCR0B = 0;
	TCCR0B |= 1<<CS00;

	DDRB |= (1<<0);

	sei();

	while(1) {
		if((PINB&(1<<0)) == 0 && command_type == BINARY) {
			command_type = STRING;
		} else if((PINB&(1<<0)) > 0 && command_type == STRING) {
			command_type = BINARY;
		}

		if(UCSR0A & (1<<RXC0)) {
			struct token token = parser_parse_command(&parser);

			switch(token.tok) {
				case FREQUENCY:
					frequency_conf(&conf, token.value, token.channel);
					frequency_execute(&conf);
					uart_transmit_str("OK\r\n");
					break;
				case AMPLITUDE:
					amplitude_conf(&conf, token.value, token.channel);
					amplitude_execute(&conf);
					uart_transmit_str("OK\r\n");
					break;
				case PHASESHIFT:
					phaseshift_conf(&conf, token.value, token.channel);
					phaseshift_execute(&conf);
					uart_transmit_str("OK\r\n");
					break;
				case REJECT:
					uart_transmit_str("REJ\r\n");
					break;
			}
		}
	}
}
