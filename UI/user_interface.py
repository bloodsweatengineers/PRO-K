#   Kerim Kilic
#   16024141
#   De Haagse Hogeschool
#   PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter

import serial
import command
import uart_connection
import serial.tools.list_ports

class FIELD(object):
    def __init__(self, row, parameter, tab_nr,field_type,padding=(0,0),leg_nr=0):
        self.leg_nr = leg_nr
        self.row = row
        self.parameter = parameter
        self.tab_nr = tab_nr
        self.field_type = field_type
        self.padding = padding
        unit = {'Frequency': 'Hz', 'PWM frequency': 'Hz', 'Amplitude legs': '%', 'Amplitude leg 4': '%', 'Phaseshift': '°'}
        self.value = unit[self.parameter]
        
        if (field_type == 'entry'):
            parameter_entry_label = Label(self.tab_nr, text = "{}:".format(self.parameter))
            parameter_entry_label.grid(row=self.row, column=0, pady=self.padding, sticky='E')
            self.parameter_entry = Entry(self.tab_nr, bd=5, state= 'disabled')
            self.parameter_entry.grid(row=self.row, column=2, pady=self.padding)
        elif (field_type == 'display'):
            parameter_display_label = Label(self.tab_nr, text="Current {}:".format(self.parameter))
            parameter_display_label.grid(row=self.row, column=0, pady=self.padding,sticky='EW')
            self.set_parameter_label = Label(self.tab_nr, text="- {}".format(unit[self.parameter]))
            self.set_parameter_label.grid(row=self.row, column=2, pady=padding, sticky='EW')

    def start(self):
        self.parameter_entry['state'] = NORMAL

    def get_data(self):
        return self.parameter_entry.get()

    def update(self,new_parameter):
        new_parameter = float(new_parameter)
        print(self.new_parameter)

        self.set_parameter_label.configure(text="{}".format(new_parameter))

    def stop(self):
        self.parameter_entry['state'] = DISABLED


class ENABLE_LEG:
    def __init__(self, row, column, tab_nr, ID):
        self.tab_nr = tab_nr
        self.row = row
        self.column = column
        self.ID = ID
        checkbutton_var = IntVar()
        self.checkbutton = Checkbutton(self.tab_nr, text = "Enable {}".format(ID), variable = checkbutton_var)
        self.checkbutton.grid(row = self.row, column = self.column ,pady=(10,10))
    
    def start(self):
        self.checkbutton['state'] = DISABLED
    
    def update(self):
        return 0

    def stop(self):
        self.checkbutton['state'] = NORMAL        

        


class GUI:
    def __init__(self,master):
        self.master = master
        self.master.title("Universal Four Leg")

        tab_control = ttk.Notebook(self.master)
        tabs = []
        tabnames = ['general', 'leg 1', 'leg 2', 'leg 3', 'leg 4']
        for x in range(5):
            tabs.append(ttk.Frame(tab_control))
            tab_control.add(tabs[x], text = tabnames[x])
        tab_control.pack(expand = 1, fill = 'both')

        #tab 1
        ttk.title_tab1 = Label(tabs[0], text = "Universal Four Leg General Settings", font = "Helvetica 16 bold italic").grid(row = 0, column = 0, columnspan = 4)
        
        self.enable_leg_1 = ENABLE_LEG(1,0,tabs[0],"leg 1")
        self.enable_leg_2 = ENABLE_LEG(1,1,tabs[0],"leg 2")
        self.enable_leg_3 = ENABLE_LEG(1,2,tabs[0],"leg 3")
        self.enable_leg_4 = ENABLE_LEG(1,3,tabs[0],"leg 4")

        #startbutton
        self.start_button = Button(tabs[0], text = "START", command = self.start_button_event, bg = 'red')
        self.start_button.grid(row = 2, column = 0, pady=(10,10))
        #updatebutton
        self.update_button = Button(tabs[0], text = "UPDATE", command = self.update_button_event)
        self.update_button.grid(row = 2, column = 1, columnspan = 2, pady=(10,10))
        #stopbutton
        self.stop_button = Button(tabs[0], text = "STOP", command = self.stop_button_event)
        self.stop_button.grid(row = 2, column = 3, pady=(10,10))

        self.frequency_entry = FIELD(3,'Frequency',tabs[0],'entry',(10,0))
        self.pwm_frequency_entry = FIELD(4,'PWM frequency',tabs[0],'entry')
        self.amplitude_entry = FIELD(5,'Amplitude legs',tabs[0],'entry')
        self.amplitude_leg_4_entry = FIELD(6, 'Amplitude leg 4', tabs[0], 'entry')
        self.phase_1_entry = FIELD(7,'Phaseshift',tabs[0],'entry',(25,0))
        self.phase_2_entry = FIELD(8,'Phaseshift',tabs[0],'entry')
        self.phase_3_entry = FIELD(9,'Phaseshift',tabs[0],'entry')
        self.phase_4_entry = FIELD(10, 'Phaseshift',tabs[0],'entry')

        self.frequency_display = FIELD(11, 'Frequency',tabs[0],'display',(25,0))
        self.pwm_frequency_display = FIELD(12,'PWM frequency',tabs[0],'display')
        self.amplitude_display = FIELD(13,'Amplitude legs',tabs[0],'display')
        self.amplitude_leg_4_display = FIELD(14,'Amplitude leg 4',tabs[0],'display')
        self.phase_1_display = FIELD(15,'Phaseshift',tabs[0],'display',(25,0))
        self.phase_2_display = FIELD(16,'Phaseshift',tabs[0],'display')
        self.phase_3_display = FIELD(17,'Phaseshift',tabs[0],'display')
        self.phase_4_display = FIELD(18,'Phaseshift',tabs[0],'display')

        #tab 2
        

    def start_button_event(self):
        self.enable_all()
    
    def stop_button_event(self):
        self.disable_all()

    def update_button_event(self):
        new_frequency = self.frequency_entry.get_data()
        self.frequency_entry.update(new_frequency)

    def enable_all(self):
        print("hallo")
        self.start_button.configure(bg = 'green')
        self.enable_leg_1.start()
        self.enable_leg_2.start()
        self.enable_leg_3.start()
        self.enable_leg_4.start()
        self.frequency_entry.start()
        self.pwm_frequency_entry.start()
        self.amplitude_entry.start()
        self.amplitude_leg_4_entry.start()
        self.phase_1_entry.start()
        self.phase_2_entry.start()
        self.phase_3_entry.start()
        self.phase_4_entry.start()

    def disable_all(self):
        self.start_button.configure(bg = 'red')
        self.enable_leg_1.stop()
        self.enable_leg_2.stop()
        self.enable_leg_3.stop()
        self.enable_leg_4.stop()
        self.frequency_entry.stop()
        self.pwm_frequency_entry.stop()
        self.amplitude_entry.stop()
        self.amplitude_leg_4_entry.stop()
        self.phase_1_entry.stop()
        self.phase_2_entry.stop()
        self.phase_3_entry.stop()
        self.phase_4_entry.stop()

