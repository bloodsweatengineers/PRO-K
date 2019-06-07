/*! \file parser.h
 *  \brief Holds all information pertaining the parsing of input over uart
 *
 *  The parser can both parse STRING and BINARY commands.
 */
#ifndef __PRO_K_PARSER_H__
#define __PRO_K_PARSER_H__

#include "token.h"
#include "uart.h"
#include "command_type.h"
#include <util/crc16.h>

/*! \struct parser
 *  \brief Holds the enumeration command_type
 */
struct parser {
	enum command_type *command_type;
}; 

/*! \fn parser_init
 *  \brief Initializes the parser
 *
 *  \param parser A pointer to the a parser object
 *  \param command_type A pointer to a command_type object.
 */
void parser_init(struct parser *parser, enum command_type *command_type);

//void parser_switch(struct parser *parser, enum command_type *command_type);

/*! \enum parser_state
 *  \brief Holds the state for the string input parser
 */
enum parser_state {
	BEGIN,
	PARAMETER,
	CHANNEL,
	VALUE,
	END
};

/*! \fn parser_parse_command
 *  \brief Main entry of the parsing API.
 *
 *  \param parser A pointer to a parser object
 *
 *  parser_parse_command is the main entry point to the
 *  parser API. Functionality requiring the parsing of
 *  uart input, should use this.
 */
struct token parser_parse_command(struct parser *parser);

/*! \fn parser_parse_str_command
 *  \brief Entry for str commands
 *
 *  \param parser A pointer to a parser object
 *
 *  This function is usually not called directly as the 
 *  function parser_parse_command will call this function
 *  if the command_type has been set to STRING.
 */
struct token parser_parse_str_command(struct parser *parser);

/*! \fn parser_parse_bin_command
 *  \brief Entry for bin commands
 *
 *  \param parser A pointer to a parser object
 *
 *  This function is usually not called directly as the
 *  function parser_parse_command will call this function
 *  if the comannd_type has been set to BINARY.
 */
struct token parser_parse_bin_command(struct parser *parser);

#endif
