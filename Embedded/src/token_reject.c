#include "token.h"

struct token token_reject() {
	return (struct token) {REJECT, -1, -1};
}
