#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {

	cli();
	struct config conf;
	struct parser parser;		
	enum command_type command_type;	
	
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
		execute_state,		
		prepare_state,		
		start_state,		
		stop_state,		
	}system_state;			

	system_state next_state = stop_state;	//! next_state starts at stop_state
	parser_init(&parser, &command_type);

	sei();

	/*!Statemachine
	 * the switch(next_state) looks for current state
	 * the switch(tok.tok) looks for event
	 */
	while(1) {
		struct token tok = parser_parse_command(&parser);
		if(tok.tok == STOP){			//! if command = STOP, always go to stop_state
			next_state = stop_state;
		}
		else{					
			switch(next_state){	
				//! this state looks only for START	
				case stop_state:	
					switch(tok.tok){
						case START:
							next_state = start_state;
							break;
						default:
							next_state = stop_state;
					}				
					break;
				//! commands can be send 1 by 1 and it's possible to go to prepare_state
				case start_state:
					switch(tok.tok){	
						//! go to prepare_state
						case PREPARE:
							next_state = prepare_state;
							break;
						//! sets frequency directly
						case FREQUENCY:		
							frequency_conf(&conf, tok.value, -1);
							frequency_execute(&conf);
							break;
						//! sets PWM frequency directly
			/*			case PWM_FREQUENCY:	
							pwmfrequency_conf(&conf, tok.value, -1);
							pwmfrequency_execute(&conf);
							break;
			*/			//! sets amplitude directly
						case AMPLITUDE:		
							amplitude_conf(&conf, tok.value, tok.channel);	
							amplitude_execute(&conf);
							break;
						//! sets phaseshift directly
						case PHASESHIFT:		
							phaseshift_conf(&conf, tok.value, tok.channel);	
							phaseshift_execute(&conf);
							break;
						//! gives ping back
						case PING: 		 
		//					ping();		/* deze functie nog maken (of ombouwen dat het klopt)*)/
							break;
						//! gather the data
						case GATHER:	
		//					gather_conf(&conf, samples);			/*! check of dit mogelijk is*)/
		//					gather_execute(&conf);				/*! check of dit mogelijk is*)/
							break;
						//! gives some info back
						case INFO:		
		//					info();		/* deze functie nog maken (of ombouwen dat het klopt)*)/
							break;
						//! if something else, go to stop_state
						default: 		// mocht er wat fout gaan ga dan naar stop_state volgende cycle
							next_state = stop_state;
					}
					break;
				//! This state saves all parameters in conf
				case prepare_state:			
					switch(tok.tok){
						//! loads frequency in conf
						case FREQUENCY:		
							frequency_conf(&conf, tok.value, -1);
							break;
						//! loads PWM frequency in conf
			/*			case PWM_FREQUENCY:	
							pwmfrequency_conf(&conf, tok.value, -1);
							break;
			*/			//! loads amplitude in conf
						case AMPLITUDE:		
							amplitude_conf(&conf, tok.value, tok.channel);	
							break;
						//! loads phaseshift in conf
						case PHASESHIFT:	
							phaseshift_conf(&conf, tok.value, tok.channel);	
							break;
						//! gives a ping back
						case PING:	
		//					ping();
							break;
						//! gather some data if going to execute
						case GATHER:		
		//					gather_conf(&conf, samples);	/* check of dit mogelijk is*)/
							break;
						//! gives some info
						case INFO:	
		//					info();				/* moet nog gemaakt worden*)/
							break;
						//! going to the execute state
						case EXECUTE: 		
							next_state = execute_state;
							break;
						//! if something else, go to stop_state
						default:			
							next_state = stop_state;
					}
					break;

					//! the execute_state executes all parameters from conf and goes to start_state
				case execute_state:			
					frequency_execute(&conf);
			//		pwmfrequency_execute(&conf);
					phaseshift_execute(&conf);
					amplitude_execute(&conf);
			//		gather_execute(&conf);			/* check of dit mogelijk is*/
			//
					next_state = start_state;
					break;
				default:					// mocht er iets fout gaan, ga naar stop_state
					next_state = stop_state;
			}
		}
	}
}
