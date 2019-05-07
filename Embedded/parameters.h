#ifndef __PRO_K_PARAMETERS_H__
#define __PRO_K_PARAMETERS_H__

#include "config.h"

bool set_frequency(uint32_t freq, struct config *conf);
void set_amplitude(uint8_t amp, uint8_t channel, struct config *conf);
void set_phaseshift(uint8_t shift, uint8_t channel, struct config *conf);

#endif
