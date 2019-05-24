#ifndef __PRO_K_CONF_H__
#define __PRO_K_CONF_H__

#include <stdint.h>

struct config {
	uint32_t	frequency;
	uint8_t		frequency_prescaler_index;
	uint16_t	frequency_clicks;
	uint8_t		amplitude[4];
	uint8_t		phaseshift[4];
	uint8_t		phaseshift_clicks[4];
};

void conf_init(struct config *conf);

#endif
