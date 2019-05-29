#ifndef __PRO_K_WAVEFORM_H__
#define __PRO_K_WAVEFORM_H__

#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include "conf.h"

#define F_CPU_10M ((F_CPU * 100))

void frequency_conf(struct config *conf, int32_t value, int8_t channel);
void frequency_execute(struct config *conf);

void phaseshift_conf(struct config *conf, uint8_t value, int8_t channel);
void phaseshift_execute(struct config *conf);

void amplitude_conf(struct config *conf, uint8_t value, int8_t channel);
void amplitude_execute(struct config *conf);

#endif
