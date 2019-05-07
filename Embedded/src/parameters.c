#include "parameters.h"

bool set_frequency(uint32_t freq, struct config *conf) {
	uint8_t possible_prescalers[] = {0,3,6,8,10};
	uint8_t list_size = sizeof(possible_prescalers) / sizeof(uint8_t);

	uint32_t clicks = F_CPU_10M / (freq << 8);
	uint8_t index = 0;

	while(clicks > BIT_16) {
		if(index >= list_size) {
			return false;
		}
		clicks >>= possible_prescalers[index];
		index++;
	}

	conf->freq_prescaler_index = index;
	conf->freq_clicks = clicks;

	return true;
}

void set_amplitude(uint8_t amp, uint8_t channel, struct config *conf) {
	conf->amplitude[channel] = amp;
}

void set_phaseshift(uint8_t shift, uint8_t channel, struct config *conf) {
	conf->phaseshift[channel] = shift;
}
