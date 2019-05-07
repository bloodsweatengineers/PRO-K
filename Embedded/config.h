#ifndef __PRO_K_CONFIG_H__
#define __PRO_K_CONFIG_H_

#ifndef F_CPU
	#error F_CPU needs to be defined
#endif
#define F_CPU_10M F_CPU * 100

#define BIT_16 65536UL

#include <stdbool.h>
#include <stdint.h>
#include <avr/io.h>
#include <avr/interrupt.h>

struct config {
	uint16_t	freq_clicks;
	uint8_t		freq_prescaler_index;
	uint8_t		amplitude[4];
	uint8_t		phaseshift[4];
};

#endif
