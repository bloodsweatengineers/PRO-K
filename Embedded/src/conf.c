#include "conf.h"

void conf_init(struct config *conf) {

	conf->frequency = 50000;
	conf->frequency_prescaler_index = 0;
	conf->frequency_clicks = 1250;

	conf->amplitude[0] = 100;
	conf->amplitude[1] = 100;
	conf->amplitude[2] = 100;
	conf->amplitude[3] = 100;

	conf->phaseshift[0] = 0;
	conf->phaseshift[1] = 0;
	conf->phaseshift[2] = 0;
	conf->phaseshift[3] = 0;

	conf->phaseshift_clicks[0] = 0;
	conf->phaseshift_clicks[1] = 0;
	conf->phaseshift_clicks[2] = 0;
	conf->phaseshift_clicks[3] = 0;
}
