/*! \file uart.h
 *  \brief This file contains all the definitions
 *  of the uart connection
 */

#ifndef __PRO_K_UART_H__
#define __PRO_K_UART_H__

#include <avr/io.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define _BAUD 9600
#define _UBRR ((((F_CPU>>2)/_BAUD) -1) >> 1)

/*!
 *  \brief initializes the uart peripheral
 *
 *  This function initializes the uart peripheral to serve
 *  as a non-interrupt based system running on 9600 BAUD
 */
void uart_init(void);

/*!
 *
 *  \brief flushes the remaining recieved message
 *
 *  This function flushes all the bytes in the buffer. It is used
 *  after a faulty or rejected message has been sent to the system.
 *
 */
void uart_flush(void);

/*!
 *
 *  \brief Recieves a single character
 */
char uart_recieve(void);

/*!
 *
 *  \brief transmits a single character
 *
 */
void uart_transmit(char c);

/*!
 *
 *  \brief transmits a string
 *
 */
void uart_transmit_str(char *c);

#endif
