#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {

	cli();
	struct config conf;

	uart_init();
	conf_init(&conf);

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

	sei();

	while(1) {
		struct token tok = parser();

		if(tok.tok == REJECT) {
			uart_transmit_str("REJ\r\n");
		} else if(tok.tok == FREQUENCY) {
			frequency_conf(&conf, tok.value, -1);
			frequency_execute(&conf);
			uart_transmit_str("OK FREQUENCY\r\n");
		} else if(tok.tok == PHASESHIFT) {
			phaseshift_conf(&conf, tok.value, tok.channel);
			phaseshift_execute(&conf);
			char buffer[10];
			memset(buffer, 0, 10);
			int32_to_str(buffer, tok.channel);
			uart_transmit_str("OK ");
			uart_transmit_str(buffer);
			uart_transmit_str(" PHASESHIFT\r\n");
		} else if(tok.tok == AMPLITUDE) {
			amplitude_conf(&conf, tok.value, tok.channel);
			amplitude_execute(&conf);
			uart_transmit_str("OK AMPLITUDE\r\n");
		}
	}
}
