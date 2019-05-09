#ifndef __PRO_K_PARSER_H__
#define __PRO_K_PARSER_H__

#include "token.h"
#include "uart.h"

enum state {
	BEGIN,
	PARAMETER,
	VALUE,
	END
};

enum tok_t validate_parameter(char *c);
int32_t validate_value(char *c);

struct token parser(void);

#endif
