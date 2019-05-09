#include "waveform.h"

static uint8_t wave[256] = {
	128,131,134,137,140,143,146,149,152,156,159,162,165,168,
	171,174,176,179,182,185,188,191,193,196,199,201,204,206,
	209,211,213,216,218,220,222,224,226,228,230,232,234,236,
	237,239,240,242,243,245,246,247,248,249,250,251,252,252,
	253,254,254,255,255,255,255,255,255,255,255,255,255,255,
	254,254,253,252,252,251,250,249,248,247,246,245,243,242,
	240,239,237,236,234,232,230,228,226,224,222,220,218,216,
	213,211,209,206,204,201,199,196,193,191,188,185,182,179,
	176,174,171,168,165,162,159,156,152,149,146,143,140,137,
	134,131,128,124,121,118,115,112,109,106,103,99,96,93,90,
	87,84,81,79,76,73,70,67,64,62,59,56,54,51,49,46,44,42,39,
	36,35,33,31,29,27,25,23,21,19,18,16,15,13,12,10,9,8,7,6,5,
	4,3,2,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,2,3,3,4,5,6,7,8,9,10,
	12,13,15,16,18,19,21,23,25,27,29,31,35,37,39,42,44,46,49,
	51,54,56,59,62,64,67,70,73,76,79,81,84,87,90,93,96,99,103,
	106,109,112,115,118,121,124
};

uint8_t static amplitude[4] = {100, 100, 100, 100};
uint8_t static phaseshift[4] = {0, 0, 0, 0};

ISR(TIMER1_COMPA_vect) {
	volatile static uint8_t index = 0;
	uint8_t leg1 = wave[index + phaseshift[0]];
	uint8_t leg2 = wave[index + phaseshift[1]];
	uint8_t leg3 = wave[index + phaseshift[2]];
	uint8_t leg4 = wave[index + phaseshift[3]];

	int8_t amp1 = (int8_t)((leg1 * amplitude[0]) / 100);
	int8_t amp2 = (int8_t)((leg2 * amplitude[1]) / 100);
	int8_t amp3 = (int8_t)((leg3 * amplitude[2]) / 100);
	int8_t amp4 = (int8_t)((leg4 * amplitude[3]) / 100);

	OCR0A = leg1 - amp1;
	OCR0B = leg2 - amp2;
	OCR1A = leg3 - amp3;
	OCR1B = leg4 - amp4;

	index++;
}

void frequency_conf(struct config *conf, uint32_t value, int8_t channel) {

	uint8_t possible_prescalers[] = {0,3,6,8,10};
	uint8_t size = sizeof(possible_prescalers)/sizeof(uint8_t);

	uint8_t index = 0;
	uint32_t clicks = F_CPU_10M / (value << 8);

	while (clicks > UINT16_MAX) {
		clicks >>= possible_prescalers[index];
		index++;
	}

	conf->frequency = value;
	conf->frequency_prescaler_index = index;
	conf->frequency_clicks = clicks;
}

void frequency_execute(struct config *conf) {
	OCR1A = conf->frequency_clicks;
	TCCR1B &= 0xF8;
	TCCR1B |= (conf->frequency_prescaler_index & 0x07);
}

void phaseshift_conf(struct config *conf, uint8_t value, int8_t channel) {
	if(channel < 0) {
		for(int i=0; i<4; i++) {
			conf->phaseshift[i] = value;
			conf->phaseshift_clicks[i] = ((uint16_t)value<<8) / 360;
		}
	} else {
		conf->phaseshift[channel] = value;
		conf->phaseshift_clicks[channel] = ((uint16_t)value<<8) / 360;
	}
}

void phaseshift_execute(struct config *conf) {
	for(int i=0; i<4; i++) {
		phaseshift[i] = conf->phaseshift_clicks[i];
	}
}

void amplitude_conf(struct config *conf, uint8_t value, int8_t channel) {
	if( channel < 0) {
		for(int i=0; i<4; i++) {
			conf->amplitude[i] = value;
		}
	} else {
		conf->amplitude[channel] = value;
	}
}

void amplitude_execute(struct config *conf) {
	for(int i=0; i<4; i++) {
		amplitude[i] = conf->amplitude[i];
	}
}
