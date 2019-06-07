#include "conf.h"

void conf_init(struct config *conf) {
	conf->frequency = 0;
	conf->frequency_prescaler_index = 1;
	conf->frequency_clicks = 1250;
	
	for(int i=0; i<4; i++) {
		conf->amplitude[i] = 100;
		conf->phaseshift[i] = 0;
		conf->phaseshift_clicks[i] = 0;
	}
}
