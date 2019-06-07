/*! \file conf.h
 *  \brief Configuration header
 *
 */
#ifndef __PRO_K_CONF_H__
#define __PRO_K_CONF_H__

#include <stdint.h>

/*! \struct config
 *  \brief Holds the runtime configuration options that pertain to
 *  parameter execution
 *
 *  The config structure holds both the parameters used for execution
 *  and the parameters given to the config functions. The config can therefore
 *  be used both for the execution of parameters and the returning of config
 *  data
 */
struct config {
	uint32_t	frequency;
	uint8_t		frequency_prescaler_index;
	uint16_t	frequency_clicks;
	uint8_t		amplitude[4];
	uint8_t		phaseshift[4];
	uint8_t		phaseshift_clicks[4];
};

/*! \fn conf_init
 *  \brief Initializes a given configuration.
 *
 *  \param conf a pointer to a configuration structure
 */
void conf_init(struct config *conf);

#endif
