#ifndef __PRO_K_PARSER_H__
#define __PRO_K_PARSER_H__

#include "token.h"
#include "uart.h"
#include "command_type.h"

struct parser {
	enum command_type *command_type;
}; 

void parser_init(struct parser *parser, enum command_type *command_type);

void parser_switch(struct parser *parser, enum command_type *command_type);

struct token parser_parse_command(struct parser *parser);
struct token parser_parse_str_command(struct parser *parser);
struct token parser_parse_bin_command(struct parser *parser);

#endif
