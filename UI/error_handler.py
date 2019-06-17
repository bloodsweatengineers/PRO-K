# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


from tkinter import messagebox
import field
##  @package error_handler
#   This module is responsible for the error handling of the user interface input. Error handling includes checking if the user puts in prohibited characters or values.


##  The ERROR_HANDLER Class returns an error message whenever the user puts in prohibited characters or values.
class ERROR_HANDLER:
    ##  The constructor of the ERROR_HANDLER takes the parameter and value and stores them in variables.
    def __init__(self, parameter, value):
        self.parameter = parameter
        self.value = value
        self.error = "ERROR"
        self.message = "One or more incorrect inputs!"
        self.error_handler = False

    ##  The call method returns one of the errorchecking functions, depending on the parameter
    def __call__(self):
        if self.parameter == 'Frequency':
            return self.frequency_error()
        if self.parameter == 'PWM frequency':
            return self.pwm_frequency_error()
        if self.parameter == 'Amplitude legs 1-3':
            return self.amplitude_error()
        if self.parameter == 'Amplitude leg 4':
            return self.amplitude_error()
        if self.parameter == 'Phaseshift 1':
            return self.phase_error()
        if self.parameter == 'Phaseshift 2':
            return self.phase_error()
        if self.parameter == 'Phaseshift 3':
            return self.phase_error()
        if self.parameter == 'Phaseshift 4':
            return self.phase_error()
    ##  The frequency_error method error checks the frequency for prohibited characters and values.
    def frequency_error(self):
        error_handler = False
        try:
            self.value = float(self.value)
            if( (self.value >= 0 and self.value <= 80) or self.value == 400):
                error_handler = True
            else:
                raise
        except:
            error_handler = False
        return error_handler
    
    ##  The pwm_frequency_error method error checks the PWM frequency for prohibited characters and values. 
    def pwm_frequency_error(self):
        error_handler = False
        try:
            self.value = float(self.value)
            if( (self.value >= 1 and self.value <= 1024)):
                error_handler = True
            else:
                raise
        except:
            error_handler = False
        return error_handler

    ##  The amplitude_error method error checks the amplitude for prohibited characters and values. 
    def amplitude_error(self):
        error_handler = False
        try:
            self.value = int(self.value)
            if( (self.value >= 0 and self.value <= 100)):
                error_handler = True
            else:
                raise
        except:
            error_handler = False
        return error_handler

    ##  The phase_error method error checks the phase for prohibited characters and values.
    def phase_error(self):
        error_handler = False
        try:
            self.value = int(self.value)
            self.value = self.value%360
            if (self.value >= 0 and self.value <= 360):
                error_handler = True
            else:
                raise
        except:
            error_handler = False    
        return error_handler
    ##  The show_error_message shows an error messag whenever a prohibited character or value is given in the entry.
    def show_error_message(self):
            messagebox.showerror(self.error,self.message)
