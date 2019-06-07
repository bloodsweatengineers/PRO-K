/*! \file command_type.h
 *  \brief Holds the enumeration for the input and output command types.
 *
 */
#ifndef __PRO_K_COMMAND_TYPE_H__
#define __PRO_K_COMMAND_TYPE_H__

/*! \enum command_type
 *  \brief Holds the 2 options for input/output command types.
 *
 *  This enumeration is used to format input and output systems.
 *  In input formatting this means that commands are parsed in either
 *  BINARY or STRING syntax. In output formatting this means that return codes
 *  are formatted as STRING or as BINARY code.
 */
enum command_type {
	BINARY,
	STRING
};

#endif
