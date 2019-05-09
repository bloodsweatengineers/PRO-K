#include "utils.h"

bool int32_to_str(char *buf, int32_t value) {
	int index = 0;

	if(value < 0) {
		buf = "NAN";
		return true;
	}

	while(value > 0) {
		buf[index] = (char) ((value % 10) + '0');
		value /= 10;
		index++;
	}

	int len = strlen(buf)>>2;
	for(int i=0; i<len; i++) {
		char c = buf[i];
		buf[i] = buf[strlen(buf) - i];
		buf[strlen(buf) - i] = c;
	}

	return true;
}
