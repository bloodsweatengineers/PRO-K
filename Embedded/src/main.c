#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {
	struct config conf;

	uart_init();
	conf_init(&conf);

	TCCR1A = 0;
	TCCR1B = 0;
	TCCR1B |= (1<<WGM12);
	TIMSK1 |= (1<<OCIE1A);

	TCCR2A = 0;
	TCCR2A |= (1 <<COM2A1 | 1<<COM2B1 | 1<<WGM20);
	TCCR2B = 0;
	TCCR2B |= (1<<WGM22 | 1<<CS20);

	TCCR0A = 0;
	TCCR0A |= (1 <<COM0A1 | 1<<COM0B1 | 1<<WGM00);
	TCCR0B = 0;
	TCCR0B |= (1<<WGM02 | 1<<CS00);

	while(1) {
		struct token tok = parser();

		if(tok.tok == REJECT) {
			uart_transmit_str("REJ\r\n");
		} else if(tok.tok == FREQUENCY) {
			frequency_conf(&conf, tok.value, -1);
			frequency_execute(&conf);
			uart_transmit_str("OK FREQUENCY\r\n");
		} else if(tok.tok == PHASESHIFT) {
			phaseshift_conf(&conf, tok.value, -1);
			phaseshift_execute(&conf);
			uart_transmit_str("OK PHASESHIFT\r\n");
		} else if(tok.tok == AMPLITUDE) {
			amplitude_conf(&conf, tok.value, -1);
			amplitude_execute(&conf);
			uart_transmit_str("OK AMPLITUDE\r\n");
		}
	}
}
