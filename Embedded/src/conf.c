#include "conf.h"
#include "uart.h"

void conf_init(struct config *conf) {
	conf->frequency = 5000;
	conf->frequency_prescaler_index = 1;
	conf->frequency_clicks = 1250;
	conf->pwm_frequency_prescaler_index = 0;
	conf->vfd_enable = 0;
	
	for(int i=0; i<4; i++) {
		conf->amplitude[i] = 100;
		conf->phaseshift[i] = 0;
		conf->phaseshift_clicks[i] = 0;
		conf->enable[i] = 0;
	}
}

int frequency_conf(struct config *conf, int32_t value, int8_t channel) {
	if((value < 1 || value > 8000) && value != 40000) {
		return -1;
	}

	if(channel != -1) {
		return -1;
	}

	uint8_t possible_prescalers[] = {0,3,6,8,10};
	uint8_t size = 5;

	uint8_t index = 1;
	uint32_t clicks = F_CPU_10M / (value << 8);

	while(clicks > (uint32_t) UINT16_MAX) {
		clicks >>= possible_prescalers[index];
		index++;
	}

	conf->frequency = value;
	conf->frequency_prescaler_index = index;
	conf->frequency_clicks = clicks;

	return 0;
}

int phaseshift_conf(struct config *conf, int32_t value, int8_t channel) {
	
	if(value < 0 || value > 360) {
		return -1;
	}

	if(channel == -1) {
		for(int i=0; i<4; i++) {
			conf->phaseshift[i] = value;
			conf->phaseshift_clicks[i] = ((uint16_t)value<<8) / 360;
		}
	} else if(channel >= 0 || channel <= 3) {
		conf->phaseshift[channel] = value;
		conf->phaseshift_clicks[channel] = ((uint16_t)value<<8) / 360;
	} else {
		return -1;
	}

	return 0;
}

int amplitude_conf(struct config *conf, int32_t value, int8_t channel) {
	if(value < 0 || value > 100) {
		return -1;
	}

	if(channel == -1) {
		conf->amplitude[0] = value;
		conf->amplitude[1] = value;
	} else if(channel >= 0 && channel <= 1) {
		conf->amplitude[channel] = value;
	} else {
		return -1;
	}

	return 0;
}

int pwm_frequency_conf(struct config *conf, int32_t value, int8_t channel) {
	if(channel != -1) {
		return -1;
	}

	uint8_t index = 1;
	switch((uint16_t)value) {
		case 1024:
			index++;
		case 256:
			index++;
		case 64:
			index++;
		case 8:
			index++;
		case 1:
			break;
		default:
			return -1;
	}

	conf->pwm_frequency_prescaler_index = index;

	return 0;
}

int enable_conf(struct config *conf, int32_t value, int8_t channel) {
	
	if(value < 0 || value > 1 || channel < 0 || channel > 4) {
		return -1;
	}

	if(channel == 0) {
		for(int i=0; i<4; i++) {
			conf->enable[i] = value;
		}
	} else {
		uart_transmit_str("enabling single conf");
		conf->enable[channel-1] = value;
	}
}

int vfd_conf(struct config *conf, int32_t value, int8_t channel) {

	if(channel != -1) {
		uart_transmit_str("Wrong channel");
		return -1;
	}

	conf->vfd_enable ^= 1;
	return 0;
}
