# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
import error_handler
import command

##  @package Field
#   This module is responsible for generating entry fields where the user can put in values and display fields where the data is being displayed

##  The FIELD Class is the parent class to ENTRY_FIELD and DISPLAY_FIELD. 
#
class FIELD(object):
    ##  The constructor takes a row for the geometrical location of the display. It takes a parameter which indicates the parameter of the field. tab_nr indicates in which tab the field should be generated. Field_type indicates if it should be a entry or a display field. Padding and leg_nr are additional arguments, padding creates a keepout zone between the fields if necessary and leg_nr the leg of which the argument belongs to.
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

##  The ENTRY_FIELD class inherits from FIELD. It creates a field at a specific location and tab specified.
#
class ENTRY_FIELD(FIELD):
    ##  The constructor inherits from FIELD and creates Entries and labels corresponding to the entries.
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        FIELD.__init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0)

        parameter_label = Label(self.tab_nr, text = "{}:".format(self.parameter))
        parameter_label.grid(row=self.row, column=0, pady=self.padding, sticky='E')
        self.parameter_entry = Entry(self.tab_nr, bd=5, state= 'disabled')
        self.parameter_entry.grid(row=self.row, column=2, pady=self.padding)
        if self.parameter == 'Frequency':
            value_label = Label(self.tab_nr,text = '0.5 - 80, 400').grid(row=self.row,column=3)
        if self.parameter == 'PWM frequency':
            value_label = Label(self.tab_nr,text = '1, 8, 64, 256, 1024').grid(row=self.row,column=3)
        if self.parameter == 'Amplitude legs 1-3':
            value_label = Label(self.tab_nr, text = '0 - 100').grid(row=self.row,column=3)
        if self.parameter == 'Amplitude leg 4':
            value_label = Label(self.tab_nr, text = '0 - 100').grid(row=self.row,column=3)
        if self.parameter == 'Phaseshift 1':
            value_label = Label(self.tab_nr, text = '0 - 360').grid(row=self.row,column=3)
        if self.parameter == 'Phaseshift 2':
            value_label = Label(self.tab_nr, text = '0 - 360').grid(row=self.row,column=3)
        if self.parameter == 'Phaseshift 3':
            value_label = Label(self.tab_nr, text = '0 - 360').grid(row=self.row,column=3)
        if self.parameter == 'Phaseshift 4':
            value_label = Label(self.tab_nr, text = '0 - 360').grid(row=self.row,column=3)

    ##  The start method enables a checkbutton if the checkbutton is enabled and disables it if the checkbutton is disabled.
    def start(self, checkbutton_status=0):
        self.parameter_entry['state'] = DISABLED
        if(checkbutton_status):
            self.parameter_entry['state'] = NORMAL
    ##  The get_data method returns the data which the user put into the entry if the format is correct, it displays a error message if there are prohibited characters or values put in.
    def get_data(self):
        self.new_data = self.parameter_entry.get()
        if self.new_data == '':
            self.new_data = 0
        error_handler_obj = error_handler.ERROR_HANDLER(self.parameter,self.new_data)

        self.parameter_entry.delete(0,'end')
        if error_handler_obj():
            return self.new_data
        else:
            error_handler_obj.show_error_message()
    ##  The stop method deletes the content of a entry and disables it.
    def stop(self):
        self.parameter_entry.delete(0,'end')
        self.parameter_entry['state'] = DISABLED

##  The DISPLAY_FIELD class inherits from FIELD. It creates a field at a specific location and tab specified.
#
class DISPLAY_FIELD(FIELD):
    ##  The constructor inherits from FIELD and creates parameter and data labels.
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        FIELD.__init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0)

        parameter_display_label = Label(self.tab_nr, text="Current {}:".format(self.parameter))
        parameter_display_label.grid(row=self.row, column=0, pady=self.padding,sticky='EW')
        self.set_parameter_label = Label(self.tab_nr, text="- {}".format(self.parameter_unit))
        self.set_parameter_label.grid(row=self.row, column=2, pady=self.padding, sticky='EW')
    
    ##  The update method updates the data labels with new data whenever the user succesfully updates.
    def update(self,new_parameter):
        self.new_parameter = new_parameter
        if self.new_parameter == 0 or self.new_parameter == None:
            self.set_parameter_label.configure(text = "- {}".format(self.parameter_unit))
        else:
            self.set_parameter_label.configure(text = "{} {}".format(self.new_parameter,self.parameter_unit))
    ##  The stop method deletes the content of a data label whenever the stop button is pressed.
    def stop(self):
        self.set_parameter_label.configure(text = "- {}".format(self.parameter_unit))

