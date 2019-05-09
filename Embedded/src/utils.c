#include "utils.h"

bool int32_to_str(char *buf, int32_t value) {
	int index = 0;

	if(value < 0) {
		buf[0] = 'N';
		buf[1] = 'a';
		buf[2] = 'N';
		return true;
	} else if(value == 0) {
		buf[0] = '0';
		return true;
	}

	while(value > 0) {
		buf[index] = (char) ((value % 10) + '0');
		value /= 10;
		index++;
	}

	return true;
}
