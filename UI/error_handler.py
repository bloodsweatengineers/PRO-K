from tkinter import messagebox
import field

class ERROR_HANDLER:
    def __init__(self, parameter, value):
        self.parameter = parameter
        self.value = value
        self.error = "ERROR"
        self.message = "One or more incorrect inputs!"
        self.error_handler = False

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

    def frequency_error(self):
        error_handler = False
        try:
            self.value = float(self.value)
            if( (self.value >= 0 and self.value <= 80) or self.value == 400):
                error_handler = True
            else:
                raise
        except:
            messagebox.showerror(self.error,self.message)

        return error_handler

    def pwm_frequency_error(self):
        error_handler = False
        try:
            self.value = float(self.value)
            if( (self.value >= 0 and self.value <= 65200)):
                error_handler = True
            else:
                raise
        except:
            messagebox.showerror(self.error,self.message)

        return error_handler

    def amplitude_error(self):
        error_handler = False
        try:
            self.value = int(self.value)
            if( (self.value >= 0 and self.value <= 100)):
                error_handler = True
            else:
                raise
        except:
            messagebox.showerror(self.error,self.message)
        return error_handler

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
            messagebox.showerror(self.error,self.message)
        return error_handler
