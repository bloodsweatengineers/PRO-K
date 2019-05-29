#include "conf.h"

void conf_init(struct config *conf) {
	conf->frequency = 0;
	conf->frequency_prescaler_index = 1;
	conf->frequency_clicks = 1250;
}
