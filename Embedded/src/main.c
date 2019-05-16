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

	typedef enum{
		execute_state,
		prepare_state,
		start_state,
		stop_state,
	}system_state;

	system_state next_state = stop_state;


	sei();

	while(1) {
		struct token tok = parser();
		struct token new_event = tok.tok;
		if(eNewEvent == REJECT){
			uart_transmit_str("REJ\r\n");
		}
		else if(eNewEvent == STOP){
			eNextState = Stop();
		}
		else{
			switch(eNextState){
				case Stop_State:
					if(eNewEvent == START){
						eNextState = Start();
					}				
					break;
				case Start_State:
					if(eNewEvent == PREPARE){
						eNextState = Prepare();
					}
					else if(eNewEvent == FREQUENCY){
						Frequency_conf(&conf, tok.value, -1);
						Frequency_execute(&conf);
					}
					else if(eNewEvent == PWMFREQUENCY){
						Pwmfrequency_conf(&conf, tok.value, -1);
						Pwmfrequency_execute(&conf);
					}
					else if(eNewEvent == AMPLITUDE){
						Amplitude_conf(&conf, tok.value, tok.channel);	//misschien geen tok.channel, nog even naar kijken
						Amplitude_execute(&conf);
					}
					else if(eNewEvent == PHASESHIFT){
						Phaseshift_conf(&conf, tok.value, tok.channel);	
						Phaseshift_execute(&conf);
					}
					else if(eNewEvent == PING){
						Ping();		// deze functie nog maken (of ombouwen dat het klopt)
					}
					else if(eNewEvent == GATHER){
						Gather_conf(&conf, samples);			// check of dit mogelijk is
						Gather_execute(&conf);				// check of dit mogelijk is
					}
					else if(eNewEvent == INFO){
						Info();		// deze functie nog maken (of ombouwen dat het klopt)
					}
					break;
	
				case Prepare_State:
					if(eNewEvent == FREQUENCY){
						Frequency_conf(&conf, tok.value, -1);
					}
					else if(eNewEvent == PWMFREQUENCY){
						Pwmfrequency_conf(&conf, tok.value, -1);
					}
					else if(eNewEvent == AMPLITUDE){
						Amplitude_conf(&conf, tok.value, tok.channel);	//misschien geen tok.channel, nog even naar kijken
					}
					else if(eNewEvent == PHASESHIFT){
						Phaseshift_conf(&conf, tok.value, tok.channel);	
					}
					else if(eNewEvent == PING){
						Ping();
					}
					else if(eNewEvent == GATHER){
						Gather_conf(&conf, samples);		// check of dit mogelijk is
					}
					else if(eNewEvent == INFO){
						Info();
					}
					else if(eNewEvent == EXECUTE){
						eNextState = Execute();
					}
					break;
				case Execute_State:
					Frequency_execute(&conf);
					Pwmfrequency_execute(&conf);
					Phaseshift_execute(&conf);
					Amplitude_execute(&conf);
					Gather_execute(&conf);				// check of dit mogelijk is
	
					eNextState = Start();
					break;
				default:
					eNextState = Stop();
				}
			}
		}

	}
}
