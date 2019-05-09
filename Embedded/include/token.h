#ifndef __PRO_K_TOKEN_H__
#define __RRO_K_TOKEN_H__

#include <stdint.h>

enum tok_t {
	REJECT,
	FREQUENCY,
	PHASESHIFT,
	AMPLITUDE,
	PWM_FREQUENCY
};

struct token {
	enum tok_t	tok;
	int32_t		value;
	int8_t		channel;
};

#endif
