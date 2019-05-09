#include <stdio.h>
#include <avr/io.h>

//Different state of ATM machine
typedef enum{
	Execute_State,
	Prepare_State,
	Start_State,
	Stop_State,
}eSystemState;

//Different type events
typedef enum{
	Ping_Event,
	Freq_Event,
	Ampl_Event,
	PWM_Freq_Event,
	Phase_Event,
	Start_Event,
	Stop_Event,
	Prepare_Event,
	Execute_Event,
	Gather_Event,
	Info_Event,
}eSystemEvent;

struct lag {
	uint8_t Amplitude;
	uint16_t PWM_Frequentie;
	uint16_t Phaseshift;
};

eSystemState Info(void);
eSystemState Ping(void);
eSystemState Gather(void);
eSystemState Prepare(void);
eSystemState Execute(void);
eSystemState Start(void);
eSystemState Stop(void);
struct lag PWM_Freq(uint16_t PWM_Frequentie);
uint64_t Freq(uint64_t Frequentie);
struct lag Ampl(uint8_t Ampiltude);
struct lag Phase(uint16_t PhaseShift);
eSystemEvent ReadEvent();


int main(void) {
	eSystemState eNextState = Stop_State;
	eSystemEvent eNewEvent = ReadEvent();
	struct lag Welke_Lag[3];
	int i;
	uint8_t LagNummer; //welke lag variable van folkert
	uint8_t Amplitude; //welke amplitude variable van folkert
	uint16_t PWM_Frequentie; //welke frequentie variable van folkert
	uint16_t PhaseShift; // Faseverandering van folkert
	uint64_t Frequentie;
	
	uint64_t Pre_Freq;
	
	//printf("Enter Phaseshift: ");
	//scanf("%i", lag.Phaseshift); //hhi als het niet lukt 1 v/d 2
	while(1){
		eNewEvent = ReadEvent(); 		//Read system Events
		if(eNewEvent == Stop_Event){
			eNextState = Stop();
		}
		switch(eNextState){
			case Stop_State:
				if(eNewEvent == Start_Event){
					eNextState = Start();
				}				
				break;
			case Start_State:
				if(eNewEvent == Prepare_Event){
					eNextState = Prepare();
				}
				break;
			case Prepare_State:
				if(eNewEvent == Freq_Event){
					Pre_Freq = Freq(Frequentie);
				}
				else if(eNewEvent == PWM_Freq_Event){
					i = LagNummer;
					Welke_Lag[i] = PWM_Freq(PWM_Frequentie);
				}
				else if(eNewEvent == Ampl_Event){
					i = LagNummer;
					Welke_Lag[i] = Ampl(Amplitude);
				}
				else if(eNewEvent == Phase_Event){
					i = LagNummer;
					Welke_Lag[i] = Phase(PhaseShift);
				}
				else if(eNewEvent == Ping_Event){
					eNextState = Ping();
				}
				else if(eNewEvent == Gather_Event){
					eNextState = Gather();
				}
				else if(eNewEvent == Info_Event){
					eNextState = Info();
				}
				else if(eNewEvent == Execute_Event){
					eNextState = Execute();
				}
				break;
			case Execute_State:
				eNextState = Start();
				//////////////////////////// hier moeten nog shits gebeuren
			default:
				eNextState = Stop();
		}
	}
	return 0;
}

//Prototype of eventhandlers
eSystemState Info(void){
	return Prepare_State;
}

eSystemState Ping(void){
	return Prepare_State;
}

eSystemState Gather(void){
	return Prepare_State;
}

eSystemState Prepare(void){
	return Prepare_State;
}

eSystemState Execute(void){
	return Start_State;
}

eSystemState Start(void){
	return Start_State;
}

eSystemState Stop(void){
	return Stop_State;
}

struct lag PWM_Freq(uint16_t PWM_Frequentie){
	struct lag std;
	std.PWM_Frequentie = PWM_Frequentie;
	return std;
}

uint64_t Freq(uint64_t Frequentie){
	uint64_t Pre_Freq = Frequentie;
	return Pre_Freq;
}

struct lag Ampl(uint8_t Ampiltude){
	struct lag std;
	std.Amplitude = Ampiltude;
	return std;
}

struct lag Phase(uint16_t PhaseShift){
	struct lag std;
	std.Phaseshift = PhaseShift;
	return std;
}

eSystemEvent ReadEvent(){
	eSystemEvent Event;
	static int i;
		if(i < 2){
			Event = Start_Event;
		}
		else if(i < 3){
			Event = Prepare_Event;
		}
		else if(i < 4){
			Event = Ampl_Event;
		}
		else if(i < 5){
			Event = Freq_Event;
		}
		else{i =0;}
		i++;
	return Event; //aanpassen, moet elke loop de commando's checken
}
