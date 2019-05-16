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

	typedef enum{			//! alle states worden hier gedefineerd
		execute_state,		//! alles wat ge-prepared is wordt uitgevoerd in deze state (alles in conf)
		prepare_state,		//! alles wordt hier in conf gezet (behalve ping,info)
		start_state,		//! na stop_state komt deze state en hier kunnen commands al 1 voor 1 worden ingevoerd
		stop_state,		//! hier begint de statemachine altijd en er wordt niks gedaan hierbinnen
	}system_state;			//! naam van de enum is system_state

	system_state next_state = stop_state;	//! next_state krijgt als eerst stop_state toegekend zodat deze daar begint


	sei();

	while(1) {
		struct token tok = parser();
		if(tok.tok == REJECT){			//! kijk als eerst of het commando valid is
			uart_transmit_str("REJ\r\n");
		}
		else if(tok.tok == STOP){		//! als command stop wordt doorgegeven, ga naar stop_state
			next_state = stop_state;
		}
		else{					//! geen STOP of REJECT -> ga statemachine bekijken
			switch(next_state){		//! kijkt naar next_state en begint met stop_state
				case stop_state:	//! kijkt alleen maar of er START gegeven wordt
					if(tok.tok == START){
						next_state = start_state;
					}
					else{
						next_state = stop_state;
					}				
					break;
				case start_state:	//! hier kunnen commands 1 voor 1 gedaan worden en er kan naar prepare gegaan worden
					if(tok.tok == PREPARE){			//! als command prepare gedaan wordt ga je in prepare_state (volgende cycle)
						next_state = perpare_state;
					}
					else if(tok.tok == FREQUENCY){		//! zet freq in conf en voer gelijk uit
						Frequency_conf(&conf, tok.value, -1);
						Frequency_execute(&conf);
					}
					else if(tok.tok == PWMFREQUENCY){	//! zet pwm freq in conf en voer gelijk uit
						Pwmfrequency_conf(&conf, tok.value, -1);
						Pwmfrequency_execute(&conf);
					}
					else if(tok.tok == AMPLITUDE){		//! zet amplitude in conf en voer geliojkt uit
						Amplitude_conf(&conf, tok.value, tok.channel);	//misschien geen tok.channel, nog even naar kijken
						Amplitude_execute(&conf);
					}
					else if(tok.tok == PHASESHIFT){		//! zet phase en kanaal in conf en voer gelijk uit
						Phaseshift_conf(&conf, tok.value, tok.channel);	
						Phaseshift_execute(&conf);
					}
					else if(tok.tok == PING){		//! vraag ping op via functie Ping() 
						Ping();				/*! deze functie nog maken (of ombouwen dat het klopt)*/
					}
					else if(tok.tok == GATHER){		//! zet gather in conf met hoeveelheid samples en voer geijk uit
						Gather_conf(&conf, samples);			/*! check of dit mogelijk is*/
						Gather_execute(&conf);				/*! check of dit mogelijk is*/
					}
					else if(tok.tok == INFO){		//! vraag info op via functie Info()
						Info();				/*! deze functie nog maken (of ombouwen dat het klopt)*/
					}
					else{ 					//! mocht er wat fout gaan ga dan naar stop_state volgende cycle	(misschien niet stop state maar iets anders dat beter is)
						next_state = stop_state;
					}
					break;
	
				case prepare_state:				//! in deze state worden commands opgeslagen in conf en uitgevoerd als er naar de execute_state gegaan wordt
					if(tok.tok == FREQUENCY){		//! laad de frequentie in conf
						Frequency_conf(&conf, tok.value, -1);
					}
					else if(tok.tok == PWMFREQUENCY){	//! laad de PWM frequentie in conf
						Pwmfrequency_conf(&conf, tok.value, -1);
					}
					else if(tok.tok == AMPLITUDE){		//! laad de amplitude in conf (met kanaal)
						Amplitude_conf(&conf, tok.value, tok.channel);	/*!misschien geen tok.channel, nog even naar kijken*/
					}
					else if(tok.tok == PHASESHIFT){		//! laad de fase in conf (met channel)
						Phaseshift_conf(&conf, tok.value, tok.channel);	
					}
					else if(tok.tok == PING){		//! roep direct de ping op via functie Ping()
						Ping();
					}
					else if(tok.tok == GATHER){		//! laad gather in conf met een aantal samples (als dit lukt)
						Gather_conf(&conf, samples);	/*! check of dit mogelijk is*/
					}
					else if(tok.tok == INFO){		//! vraag direct info op via Info()	(als dit lukt)
						Info();				/*! moet nog gemaakt worden*/
					}
					else if(tok.tok == EXECUTE){		//! ga volgende cycle naar de execute_state
						next_state = execute_state;
					}
					else{					/*! als er iets gaat gaat, ga dan naar stop state (misschien nog aanpassen naar een andere state indien gewenst)*/
						next_state = stop_state;
					}
					break;

				case Execute_State:				//! voer alles wat in de conf staat uit en ga naar start_state
					Frequency_execute(&conf);
					Pwmfrequency_execute(&conf);
					Phaseshift_execute(&conf);
					Amplitude_execute(&conf);
					Gather_execute(&conf);			/*! check of dit mogelijk is*/
	
					eNextState = start_state;
				default:					//! mocht er iets fout gaan, ga naar stop_state
					next_state = stop_state;
				}
			}
		}

	}
}
