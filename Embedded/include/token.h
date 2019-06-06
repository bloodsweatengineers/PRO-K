#ifndef __PRO_K_TOKEN_H__
#define __RRO_K_TOKEN_H__

#include <stdint.h>
#include <token_table.h>
#include <string.h>

struct token {
	enum tok_t	tok;
	int32_t		value;
	int8_t		channel;
};

struct token token_reject();

int check_bin_value(uint8_t command, int32_t value);

enum tok_t retrieve_bin_command(unsigned char c);
int8_t retrieve_bin_channel(unsigned char c);

//enum tok_t retrieve_str_command(char *buffer);
//int32_t retrieve_str_value(char *buffer);

#endif
