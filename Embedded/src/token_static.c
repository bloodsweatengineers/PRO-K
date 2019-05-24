#include "token.h"

struct token token_reject() {
	return (struct token) {REJECT, -1, -1};
}

int check_bin_value(uint8_t command, int32_t value) {
	return 0;
}

int32_t get_str_value(char *buffer) {
	int32_t value = 0;
	for(int i=0; i<strlen(buffer); i++) {
		if( buffer[i] >= '0' && buffer[i] <= '9') {
			value *= 10;
			value += buffer[i] - '0';
		} else {
			return -2;
		}
	}
}
