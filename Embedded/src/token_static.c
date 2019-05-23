#include "token.h"

struct token token_reject() {
	return (struct token) {REJECT, -1, -1};
}

int check_bin_value(uint8_t command, int32_t value) {
	return 0;
}
