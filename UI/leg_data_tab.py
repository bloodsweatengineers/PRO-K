# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter

##  @package leg_data_tab
#   This module creates the data which is displayed in the different tabs.   


##  LEG_DATA_TAB creates the labels corresponding to the data which is displayed into the different tabs.
class LEG_DATA_TAB:
    ##  The constructor takes tabnr and legnr as arguments. It creates the data labels in the tab specified and for the leg specified.
    def __init__(self, tabnr, legnr):
        self.tabnr = tabnr
        self.legnr = legnr
        self.frame = []
        for i in range(6):
            self.frame.append(Frame(self.tabnr))
            self.frame[i].pack()

        title_label = Label(self.frame[0], text="leg {} settings".format(self.legnr), font="Helvetica 16 bold italic").pack()

        #Current frequency setting
        self.frequency_label = Label(self.frame[1], text = "Current frequency:").pack(side=LEFT)
        self.frequency_data_label = Label(self.frame[1], text = "- Hz")
        self.frequency_data_label.pack(side=LEFT)
        #Current PWM frequency setting
        self.pwm_frequency_label = Label(self.frame[2], text = "Current PWM frequency prescaler:").pack(side=LEFT)
        self.pwm_frequency_data_label = Label(self.frame[2], text="- Hz")
        self.pwm_frequency_data_label.pack(side=LEFT)
        #current amplitude setting
        self.amplitude_label = Label(self.frame[3], text = "Current amplitude:").pack(side=LEFT)
        self.amplitude_data_label = Label(self.frame[3], text = "- %")
        self.amplitude_data_label.pack(side=LEFT)
        #current phase setting
        self.phase_label = Label(self.frame[4], text= "Current phase shift:").pack(side=LEFT)
        self.phase_data_label = Label(self.frame[4], text="- °")
        self.phase_data_label.pack(side=LEFT)
    
    ##  The update method updates datalabels if the update button is succesfully processed.
    def update(self, parameter, value):
        self.new_value = value
        self.parameter = parameter
        if parameter == 'Frequency':
            self.frequency_data_label.configure(text="{} Hz".format(self.new_value))
        elif parameter == 'PWM Frequency':
            self.pwm_frequency_data_label.configure(text="{} Hz".format(self.new_value))
        elif parameter == 'Amplitude':
            self.amplitude_data_label.configure(text="{} %".format(self.new_value))
        elif parameter == 'Phaseshift':
            self.phase_data_label.configure(text ="{} °".format(self.new_value))
    ##  The stop method deletes the contents of data labels whenever the stop button is pressed.
    def stop(self):
            self.frequency_data_label.configure(text="- Hz")
            self.pwm_frequency_data_label.configure(text="- Hz")
            self.amplitude_data_label.configure(text="- %")
            self.phase_data_label.configure(text ="- °")
