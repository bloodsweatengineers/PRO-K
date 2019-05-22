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
        self.parameter_entry.delete(0,'end')
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
    
    def start(self):
        FIELD.start(self)
    def get_data(self):
        FIELD.get_data(self)
    def update(self,new_parameter):
        self.new_parameter = new_parameter
        self.set_parameter_label.configure(text = "{} {}".format(self.new_parameter,self.parameter_unit))
    def stop(self):
        self.set_parameter_label.configure(text = "- {}".format(self.parameter_unit))

class ENABLE_LEG:
    def __init__(self, row, column, tab_nr, ID):
        self.tab_nr = tab_nr
        self.row = row
        self.column = column
        self.ID = ID
        self.checkbutton_var = IntVar()
        self.checkbutton = Checkbutton(self.tab_nr, text = "Enable {}".format(ID), variable = self.checkbutton_var)
        self.checkbutton.grid(row = self.row, column = self.column ,pady=(10,10))

    def get_data(self):
        return self.checkbutton_var.get()

    def start(self):
        self.checkbutton['state'] = DISABLED
    
    def update(self):
        return 0

    def stop(self):
        self.checkbutton['state'] = NORMAL        

class LEG_DATA_TAB:
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
        self.pwm_frequency_label = Label(self.frame[2], text = "Current PWM frequency:").pack(side=LEFT)
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

    def stop(self):
            self.frequency_data_label.configure(text="- Hz")
            self.pwm_frequency_data_label.configure(text="- Hz")
            self.amplitude_data_label.configure(text="- %")
            self.phase_data_label.configure(text ="- °")

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

        self.frequency_entry = ENTRY_FIELD(3,'Frequency',tabs[0],'entry',(10,0))
        self.pwm_frequency_entry = ENTRY_FIELD(4,'PWM frequency',tabs[0],'entry')
        self.amplitude_entry = ENTRY_FIELD(5,'Amplitude legs 1-3',tabs[0],'entry')
        self.amplitude_leg_4_entry = ENTRY_FIELD(6, 'Amplitude leg 4', tabs[0], 'entry')
        self.phase_1_entry = ENTRY_FIELD(7,'Phaseshift 1',tabs[0],'entry',(25,0))
        self.phase_2_entry = ENTRY_FIELD(8,'Phaseshift 2',tabs[0],'entry')
        self.phase_3_entry = ENTRY_FIELD(9,'Phaseshift 3',tabs[0],'entry')
        self.phase_4_entry = ENTRY_FIELD(10, 'Phaseshift 4',tabs[0],'entry')

        self.frequency_display = DISPLAY_FIELD(11, 'Frequency',tabs[0],'display',(25,25))
        self.pwm_frequency_display = DISPLAY_FIELD(12,'PWM frequency',tabs[0],'display')
        self.amplitude_display = DISPLAY_FIELD(13,'Amplitude legs 1-3',tabs[0],'display')
        self.amplitude_leg_4_display = DISPLAY_FIELD(14,'Amplitude leg 4',tabs[0],'display')
        self.phase_1_display = DISPLAY_FIELD(15,'Phaseshift 1',tabs[0],'display',(25,0))
        self.phase_2_display = DISPLAY_FIELD(16,'Phaseshift 2',tabs[0],'display')
        self.phase_3_display = DISPLAY_FIELD(17,'Phaseshift 3',tabs[0],'display')
        self.phase_4_display = DISPLAY_FIELD(18,'Phaseshift 4',tabs[0],'display')

        #tab 2 leg 1
        self.tab_2 = LEG_DATA_TAB(tabs[1],1)
        #tab 3 leg 2
        self.tab_3 = LEG_DATA_TAB(tabs[2],2)
        #tab 4 leg 3
        self.tab_4 = LEG_DATA_TAB(tabs[3],3)
        #tab 5 leg 4
        self.tab_5 = LEG_DATA_TAB(tabs[4],4)


    def start_button_event(self):
        self.enable_all()
    
    def stop_button_event(self):
        self.disable_all()

    def update_button_event(self):
        self.update_all_fields()
    
    def error_handler(self):
        return 0

    def update_all_fields(self):
        if(self.enable_leg_1.get_data() or self.enable_leg_2.get_data() or self.enable_leg_3.get_data() or self.enable_leg_4.get_data()):
            new_frequency = self.frequency_entry.get_data()
            new_pwm_frequency = self.pwm_frequency_entry.get_data()
            
            self.frequency_display.update(new_frequency)
            self.tab_2.update('Frequency',new_frequency)
            self.tab_3.update('Frequency',new_frequency)
            self.tab_4.update('Frequency',new_frequency)
            self.tab_5.update('Frequency',new_frequency)

            self.pwm_frequency_display.update(new_pwm_frequency)
            self.tab_2.update('PWM Frequency',new_pwm_frequency)
            self.tab_3.update('PWM Frequency',new_pwm_frequency)
            self.tab_4.update('PWM Frequency',new_pwm_frequency)
            self.tab_5.update('PWM Frequency',new_pwm_frequency)

        if(self.enable_leg_1.get_data() or self.enable_leg_2.get_data() or self.enable_leg_3.get_data()):
            new_amplitude = self.amplitude_entry.get_data()

            self.amplitude_display.update(new_amplitude)
            self.tab_2.update('Amplitude',new_amplitude)
            self.tab_3.update('Amplitude',new_amplitude)
            self.tab_4.update('Amplitude',new_amplitude)

        if(self.enable_leg_4.get_data()):
            new_amplitude_leg_4 = self.amplitude_leg_4_entry.get_data()
            self.amplitude_leg_4_display.update(new_amplitude_leg_4)
            self.tab_5.update('Amplitude',new_amplitude_leg_4)
        if(self.enable_leg_1.get_data()):
            new_phase_1 = self.phase_1_entry.get_data()
            self.phase_1_display.update(new_phase_1)
            self.tab_2.update('Phaseshift',new_phase_1)
        if(self.enable_leg_2.get_data()):
            new_phase_2 = self.phase_2_entry.get_data()
            self.phase_2_display.update(new_phase_2)
            self.tab_3.update('Phaseshift',new_phase_2)
        if(self.enable_leg_3.get_data()):
            new_phase_3 = self.phase_3_entry.get_data()
            self.phase_3_display.update(new_phase_3)
            self.tab_4.update('Phaseshift',new_phase_3)
        if(self.enable_leg_4.get_data()):
            new_phase_4 = self.phase_4_entry.get_data()
            self.phase_4_display.update(new_phase_4)
            self.tab_5.update('Phaseshift',new_phase_4)


    def enable_all(self):
        if(self.enable_leg_1.get_data() or self.enable_leg_2.get_data() or self.enable_leg_3.get_data() or self.enable_leg_4.get_data()):
            self.start_button.configure(bg = 'green')
            self.enable_leg_1.start()
            self.enable_leg_2.start()
            self.enable_leg_3.start()
            self.enable_leg_4.start()
            self.frequency_entry.start(1)
            self.pwm_frequency_entry.start(1)
        if(self.enable_leg_1.get_data() or self.enable_leg_2.get_data() or self.enable_leg_3.get_data()):
            self.amplitude_entry.start(1)
        if(self.enable_leg_4.get_data()):
            self.amplitude_leg_4_entry.start(1)
        
        self.phase_1_entry.start(self.enable_leg_1.get_data())
        self.phase_2_entry.start(self.enable_leg_2.get_data())
        self.phase_3_entry.start(self.enable_leg_3.get_data())
        self.phase_4_entry.start(self.enable_leg_4.get_data())

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
        self.frequency_display.stop()
        self.pwm_frequency_display.stop()
        self.amplitude_display.stop()
        self.amplitude_leg_4_display.stop()
        self.phase_1_display.stop()
        self.phase_2_display.stop()
        self.phase_3_display.stop()
        self.phase_4_display.stop()
        self.disable_tabs()

    def disable_tabs(self):
        self.tab_2.stop()
        self.tab_3.stop()
        self.tab_4.stop()
        self.tab_5.stop()
