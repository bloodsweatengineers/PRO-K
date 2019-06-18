#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {

	cli();
	struct config conf;
	struct parser parser;		
	enum command_type command_type = BINARY;	
	
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

	//!define all states
	/*!
	 * execute_state takes all prepared values
	 * prepare_state saves all values, they execute all at ones
	 * start_state means that parameters can be send over
	 * stop_state needs a start, stop_state is "waiting" 
	 */
	typedef enum{			
		start_state,
		prepare_state,
		stop_state
	}system_state;			

	system_state next_state = stop_state;	//! next_state starts at stop_state
	parser_init(&parser, &command_type);

	sei();

	while(1) {

		struct token tok = parser_parse_command(&parser);

		switch(next_state) {
			case start_state:
				switch(tok.tok) {
					case FREQUENCY:
						if(frequency_conf(&conf, tok.value, tok.channel) == -1){
							uart_transmit_str("REJ \r\n");
						}
						else{
							frequency_execute(&conf);
							uart_transmit_str("OK \r\n");
						}
						break;
					case AMPLITUDE:
						if(amplitude_conf(&conf, tok.value, tok.channel) == -1)
						{
							uart_transmit_str("REJ \r\n");
						}else{
							amplitude_execute(&conf);
							uart_transmit_str("OK \r\n");
						}
						break;
					case PHASESHIFT:
						if(phaseshift_conf(&conf, tok.value, tok.channel) == -1)
						{
							uart_transmit_str("REJ \r\n");
						}else{
							phaseshift_execute(&conf);
							uart_transmit_str("OK \r\n");
						}
						break;
					case PWM_FREQUENCY:
						if(pwm_frequency_conf(&conf, tok.value, tok.channel) == -1)
						{
							uart_transmit_str("REJ \r\n");
						}else{
							pwm_frequency_execute(&conf);
							uart_transmit_str("OK \r\n");
						}
						break;
					case STOP:
						next_state = stop_state;
						uart_transmit_str("OK \r\n");
						break;
					case INFO:
						uart_transmit_str("OK \r\n");
						break;
					case PING:
						uart_transmit_str("OK START STATE\r\n");
						break;
					case PREPARE:
						next_state = prepare_state;
						uart_transmit_str("OK \r\n");
						break;
					case EXECUTE:
						execute_all(&conf);
						uart_transmit_str("OK \r\n");
						break;
					case ENABLE:
						if(enable_conf(&conf, tok.value, tok.channel) == -1)
						{
							uart_transmit_str("REJ \r\n");
						}else{
							enable_execute(&conf);
							uart_transmit_str("OK \r\n");
						}
						break;
					default:
						uart_transmit_str("REJ \r\n");
					}
					break;
				case prepare_state:
					switch(tok.tok) {
						case FREQUENCY:
							if(frequency_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						case AMPLITUDE:
							if(amplitude_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						case PHASESHIFT:
							if(phaseshift_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						case PWM_FREQUENCY:
							if(pwm_frequency_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						case STOP:
							next_state = stop_state;
							uart_transmit_str("OK \r\n");
							break;
						case INFO:
							uart_transmit_str("OK \r\n");
							break;
						case PING:
							uart_transmit_str("OK PREPARE STATE \r\n");
							break;
						case PREPARE:
							uart_transmit_str("REJ \r\n");
							break;
						case EXECUTE:
							next_state = start_state;
							execute_all(&conf);
							uart_transmit_str("OK \r\n");
							break;
						case ENABLE:
							if(enable_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						case VFD:
							if(vfd_conf(&conf, tok.value, tok.channel) == -1)
							{
								uart_transmit_str("REJ \r\n");
							}else{
								uart_transmit_str("OK \r\n");
							}
							break;
						default:
							uart_transmit_str("REJ \r\n");
					}
					break;
				case stop_state:
					if(tok.tok == START) {
						next_state = start_state;
						uart_transmit_str("OK \r\n");
					} else if(tok.tok == PING) {
						uart_transmit_str("OK STOP STATE \r\n");
					} else {
						uart_transmit_str("REJ \r\n");
					}
					break;
			}
		}
}
