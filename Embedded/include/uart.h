#ifndef __PRO_K_UART_H__
#define __PRO_K_UART_H__

#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define _BAUD 9600
#define _UBRR ((((F_CPU>>2)/_BAUD) -1) >> 1)

void uart_init(void);

void uart_flush(void);

char uart_recieve(void);

void uart_transmit(char c);
void uart_transmit_str(char *c);

#endif
