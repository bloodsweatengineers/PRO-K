/*! \file waveform.h
 *
 *  \brief This file contains all the definitions for the waveform
 *  generation
 */

#ifndef __PRO_K_WAVEFORM_H__
#define __PRO_K_WAVEFORM_H__

#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include "conf.h"

#define F_CPU_10M ((F_CPU * 100))

void frequency_execute(struct config *conf);

void phaseshift_execute(struct config *conf);

void amplitude_execute(struct config *conf);

void pwm_frequency_execute(struct config *conf);

void enable_execute(struct config *conf);

void execute_all(struct config *conf);

#endif
