#include "parser.h"
#include "utils.h"
#include "conf.h"
#include "waveform.h"

void main(void) {

	cli();
	struct config conf;
	struct parser parser;		// deze erbij gemaakt voor parser_init
	enum command_type command_type;	// deze erbij gemaakt voor parser_init
	
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

	typedef enum{			//! alle states worden hier gedefineerd
		execute_state,		//! alles wat ge-prepared is wordt uitgevoerd in deze state (alles in conf)
		prepare_state,		//! alles wordt hier in conf gezet (behalve ping,info)
		start_state,		//! na stop_state komt deze state en hier kunnen commands al 1 voor 1 worden ingevoerd
		stop_state,		//! hier begint de statemachine altijd en er wordt niks gedaan hierbinnen
	}system_state;			//! naam van de enum is system_state

	system_state next_state = stop_state;	//! next_state krijgt als eerst stop_state toegekend zodat deze daar begint
	parser_init(&parser, &command_type);

	sei();

	while(1) {
		struct token tok = parser_parse_command(&parser);
		if(tok.tok == STOP){		//! als command stop wordt doorgegeven, ga naar stop_state
			next_state = stop_state;
		}
		else{					//! geen STOP of REJECT -> ga statemachine bekijken
			switch(next_state){		//! kijkt naar next_state en begint met stop_state
				case stop_state:	//! kijkt alleen maar of er START gegeven wordt
					switch(tok.tok){
						case START:
							next_state = start_state;
							break;
						default:
							next_state = stop_state;
					}				
					break;
				case start_state:	//! hier kunnen commands 1 voor 1 gedaan worden en er kan naar prepare gegaan worden
					switch(tok.tok){
						case PREPARE:			//! als command prepare gedaan wordt ga je in prepare_state (volgende cycle)
							next_state = prepare_state;
							break;

						case FREQUENCY:		//! zet freq in conf en voer gelijk uit
							frequency_conf(&conf, tok.value, -1);
							frequency_execute(&conf);
							break;

						case PWM_FREQUENCY:	//! zet pwm freq in conf en voer gelijk uit
		//					pwmfrequency_conf(&conf, tok.value, -1);
		//					pwmfrequency_execute(&conf);
							break;

						case AMPLITUDE:		//! zet amplitude in conf en voer geliojkt uit
							amplitude_conf(&conf, tok.value, tok.channel);	//misschien geen tok.channel, nog even naar kijken
							amplitude_execute(&conf);
							break;

						case PHASESHIFT:		//! zet phase en kanaal in conf en voer gelijk uit
							phaseshift_conf(&conf, tok.value, tok.channel);	
							phaseshift_execute(&conf);
							break;
						case PING: 		//! vraag ping op via functie Ping() 
		//					Ping();				/*! deze functie nog maken (of ombouwen dat het klopt)*)/
							break;

						case GATHER:		//! zet gather in conf met hoeveelheid samples en voer geijk uit
		//					Gather_conf(&conf, samples);			/*! check of dit mogelijk is*)/
		//					Gather_execute(&conf);				/*! check of dit mogelijk is*)/
							break;

						case INFO:		//! vraag info op via functie Info()
		//					Info();				/*! deze functie nog maken (of ombouwen dat het klopt)*)/
							break;

						default: 					//! mocht er wat fout gaan ga dan naar stop_state volgende cycle	(misschien niet stop state maar iets anders dat beter is)
							next_state = stop_state;
					}
					break;
				case prepare_state:				//! in deze state worden commands opgeslagen in conf en uitgevoerd als er naar de execute_state gegaan wordt
					switch(tok.tok){
						case FREQUENCY:		//! laad de frequentie in conf
							frequency_conf(&conf, tok.value, -1);
							break;

						case PWM_FREQUENCY:	//! laad de PWM frequentie in conf
		//					pwmfrequency_conf(&conf, tok.value, -1);
							break;

						case AMPLITUDE:		//! laad de amplitude in conf (met kanaal)
							amplitude_conf(&conf, tok.value, tok.channel);	/*!misschien geen tok.channel, nog even naar kijken*/
							break;

						case PHASESHIFT:		//! laad de fase in conf (met channel)
							phaseshift_conf(&conf, tok.value, tok.channel);	
							break;

						case PING:		//! roep direct de ping op via functie Ping()
		//					Ping();
							break;

						case GATHER:		//! laad gather in conf met een aantal samples (als dit lukt)
		//					Gather_conf(&conf, samples);	/*! check of dit mogelijk is*)/
							break;

						case INFO:		//! vraag direct info op via Info()	(als dit lukt)
		//					Info();				/*! moet nog gemaakt worden*)/
							break;

						case EXECUTE: 		//! ga volgende cycle naar de execute_state
		//					next_state = execute_state;
							break;

						default:					/*! als er iets gaat gaat, ga dan naar stop state (misschien nog aanpassen naar een andere state indien gewenst)*/
							next_state = stop_state;
					}
					break;

				case execute_state:				//! voer alles wat in de conf staat uit en ga naar start_state
					frequency_execute(&conf);
		//			pwmfrequency_execute(&conf);
					phaseshift_execute(&conf);
					amplitude_execute(&conf);
			//		Gather_execute(&conf);			/*! check of dit mogelijk is*/
	
					next_state = start_state;
					break;
				default:					//! mocht er iets fout gaan, ga naar stop_state
					next_state = stop_state;
			}
		}
	}
}
