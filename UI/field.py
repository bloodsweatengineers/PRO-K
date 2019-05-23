from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
import error_handler

class FIELD(object):
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        self.leg_nr = leg_nr
        self.row = row
        self.parameter = parameter
        self.tab_nr = tab_nr
        self.field_type = field_type
        self.padding = padding
        unit = {'Frequency': 'Hz', 'PWM frequency': 'Hz', 'Amplitude legs 1-3': '%', 'Amplitude leg 4': '%',
                'Phaseshift 1': '°',
                'Phaseshift 2': '°',
                'Phaseshift 3': '°',
                'Phaseshift 4': '°'}
        self.parameter_unit = unit[self.parameter]

class ENTRY_FIELD(FIELD):
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        FIELD.__init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0)

        parameter_label = Label(self.tab_nr, text = "{}:".format(self.parameter))
        parameter_label.grid(row=self.row, column=0, pady=self.padding, sticky='E')
        self.parameter_entry = Entry(self.tab_nr, bd=5, state= 'disabled')
        self.parameter_entry.grid(row=self.row, column=2, pady=self.padding)

    def start(self, checkbutton_status=0):
        self.parameter_entry['state'] = DISABLED
        if(checkbutton_status):
            self.parameter_entry['state'] = NORMAL
    def get_data(self):
        self.new_data = self.parameter_entry.get()
        #error_handler_obj = ERROR_HANDLER(self.parameter, self.new_data)
        error_handler_obj = error_handler.ERROR_HANDLER(self.parameter,self.new_data)

        self.parameter_entry.delete(0,'end')
        if error_handler_obj():
            return self.new_data

    def stop(self):
        self.parameter_entry.delete(0,'end')
        self.parameter_entry['state'] = DISABLED

class DISPLAY_FIELD(FIELD):
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        FIELD.__init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0)

        parameter_display_label = Label(self.tab_nr, text="Current {}:".format(self.parameter))
        parameter_display_label.grid(row=self.row, column=0, pady=self.padding,sticky='EW')
        self.set_parameter_label = Label(self.tab_nr, text="- {}".format(self.parameter_unit))
        self.set_parameter_label.grid(row=self.row, column=2, pady=self.padding, sticky='EW')

    def update(self,new_parameter):
        self.new_parameter = new_parameter
        self.set_parameter_label.configure(text = "{} {}".format(self.new_parameter,self.parameter_unit))
    def stop(self):
        self.set_parameter_label.configure(text = "- {}".format(self.parameter_unit))

