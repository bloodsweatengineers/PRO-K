#include "token.h"

struct token token_reject() {
	return (struct token) {REJECT, -1, -1};
}

int check_bin_value(enum tok_t tok, uint32_t value) {
	if (value == 0x00FFFFFF) {
		return 1;
	} else {
		return 0;
	}
}

int32_t get_str_value(char *buffer) {
	uint32_t value = 0;
	for(int i=0; i<strlen(buffer); i++) {
		if( buffer[i] >= '0' && buffer[i] <= '9') {
			value *= 10;
			value += buffer[i] - '0';
		} else {
			return -2;
		}
	}
	return (int32_t) value;
}
