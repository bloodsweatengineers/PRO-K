/*! \file token.h
 *  \brief Holds all the information for the tokenizer
 *
 */

#ifndef __PRO_K_TOKEN_H__
#define __RRO_K_TOKEN_H__

#include <stdint.h>
#include <token_table.h>
#include <string.h>
#include "uart.h"
#include "utils.h"

/*! \struct token
 *  \brief The main return of the tokenizer
 *
 */
struct token {
	enum tok_t	tok;
	int32_t		value;
	int8_t		channel;
	int8_t		get;
};

/*!
 *  \brief Returns a struct token with the reject options
 *
 *  This function returns a struct token with all the member
 *  values set to invalid values. This ensures the command is rejected.
 *  It is mainly used as a shorthand for rejecting an input.
 *
 *  \return A token
 */
struct token token_reject();

/*!
 *  \brief Checks the value given with a BINARY command.
 *
 *  Checks the value given with a BINARY command.
 *
 *  \param tok A enumeration of valid tokens
 *  \param value the value that needs to be checked.
 */
int check_bin_value(enum tok_t tok, uint32_t value);

/*!
 *  \brief Converts a string with a numerical value to
 *  an int32_t
 *
 *  \param buffer A string containing the value
 */
int32_t get_str_value(char *buffer);

/*!
 *  \brief retrieves the command in the form of a tok_t enumeration from
 *  a 1-byte integer
 *
 *  \param c An 1-byte integer holding the command and channel.
 */
enum tok_t retrieve_bin_command(unsigned char c);

/*!
 *  \brief retrieves the channel in the from of a int8_t from
 *  an 1-byte integer.
 *
 *  \param c An 1-byte integer holding the command and channel
 */
int8_t retrieve_bin_channel(unsigned char c);

/*!
 *  \brief Retrieves a command in the from of a tok_t enumeration from
 *  a string
 *
 *  \param buffer A string holding the command
 */
enum tok_t retrieve_str_command(char *buffer);

#endif
