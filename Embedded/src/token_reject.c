#include "token.h"

struct token token_reject() {
	return {REJECT, -1, -1};
}
