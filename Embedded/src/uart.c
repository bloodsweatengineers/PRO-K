#include "uart.h"

void uart_init(void) {
	DDRD |= (1<<PD1);
	DDRD &= ~(1<<PD0);

	UCSR0A = 1 << U2X0;

	UBRR0H = (uint16_t)(_UBRR) >> 8;
	UBRR0L = (uint16_t)(_UBRR);

	UCSR0B |= (1<<RXEN0) | (1<<TXEN0);
	UCSR0C = (3<<UCSZ00);
}

void uart_flush(void) {
	unsigned char dummy;
	while(UCSR0A & (1<<RXC0)) dummy = UDR0;
}

char uart_recieve(void) {
	while(!(UCSR0A & (1<<RXC0)));
	return (char) UDR0;
}

void uart_transmit(char c) {
	while(!(UCSR0A & (1<<UDRE0)));
	UDR0 = c;
}

void uart_transmit_str(char *c) {
	for(int i=0; i<strlen(c); i++) {
		uart_transmit(c[i]);
	}
}
