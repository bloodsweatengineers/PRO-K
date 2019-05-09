#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define _BAUD 9600
#define _UBRR ((((F_CPU>>2)/_BAUD) -1)>>1)

void init(void) {
	DDRD |= (1<<PD1);
	DDRD &= ~(1<<PD0);

	UCSR0A = 1 << U2X0;

	UBRR0H = (uint16_t)(_UBRR) >> 8;
	UBRR0L = (uint16_t)(_UBRR);

	UCSR0B |= (1<<RXEN0) | (1<<TXEN0);
	UCSR0C = (3<<UCSZ00);
}

char read(void) {
	while(!(UCSR0A & (1<<RXC0)));
	return (char) UDR0;
}

void flush(void) {
	unsigned char dummy;
	while(UCSR0A & (1<<RXC0)) dummy = UDR0;
}

void transmit(char c) {
	while(!(UCSR0A & (1<<UDRE0)));
	UDR0 = c;
}

void transmit_str(char *c) {
	for(int i=0; i<strlen(c); i++) {
		transmit(c[i]);
	}
}

void main(void) {

	init();

	while(1) {
		bool worked = true;
		if((unsigned char) read() != 0x24) {
			transmit_str("REJ start\r\n");
			worked = false;
			flush();
		}

		if((unsigned char) read() != 0x01) {
			transmit_str("REJ command\r\n");
			worked = false;
			flush();
		}

		uint32_t nr = 0;
		for(int i=0; i<3; i++) {
			nr <<= 8;
			nr |= (unsigned char) read();
		}

		if(nr != 100) {
			transmit_str("REJ value\r\n");
			worked = false;
			flush();
		}

		if((unsigned char) read() != 198) {
			transmit_str("REJ crc\r\n");
			worked = false;
			flush();
		}

		if(worked == true) {
			transmit_str("OK\r\n");
			flush();
		}
	}
}
