#   Kerim Kilic
#   16024141
#   De Haagse Hogeschool
#   PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
import serial
import serial.tools.list_ports

import command
import uart_connection
import error_handler
import field
import leg_data_tab
import enable_leg


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
        
        menu_bar = Menu(self.master)
        menu_bar.add_command(label='Help')
        menu_bar.add_command(label='About')
        self.master.config(menu = menu_bar)

        #tab 1
        ttk.title_tab1 = Label(tabs[0], text = "Universal Four Leg General Settings", font = "Helvetica 16 bold italic").grid(row = 0, column = 0, columnspan = 4)
       
        #Refresh button
        self.refresh_button = Button(tabs[0], text="Refresh Arduino", command = self.refresh_button_event)
        self.refresh_button.grid(row = 1, column = 0)
        self.connection_label = Label(tabs[0],text="Unconnected")
        self.connection_label.grid(row=1,column=3)

        self.enable_leg_1 = enable_leg.ENABLE_LEG(2,0,tabs[0],"leg 1")
        self.enable_leg_2 = enable_leg.ENABLE_LEG(2,1,tabs[0],"leg 2")
        self.enable_leg_3 = enable_leg.ENABLE_LEG(2,2,tabs[0],"leg 3")
        self.enable_leg_4 = enable_leg.ENABLE_LEG(2,3,tabs[0],"leg 4")

        #startbutton
        self.start_button = Button(tabs[0], text = "START", command = self.start_button_event, bg = 'red')
        self.start_button.grid(row = 3, column = 0, pady=(10,10))
        #updatebutton
        self.update_button = Button(tabs[0], text = "UPDATE", command = self.update_button_event)
        self.update_button.grid(row = 3, column = 1, columnspan = 2, pady=(10,10))
        #stopbutton
        self.stop_button = Button(tabs[0], text = "STOP", command = self.stop_button_event)
        self.stop_button.grid(row = 3, column = 3, pady=(10,10))

        self.frequency_entry = field.ENTRY_FIELD(4,'Frequency',tabs[0],'entry',(10,0))
        self.pwm_frequency_entry = field.ENTRY_FIELD(5,'PWM frequency',tabs[0],'entry')
        self.amplitude_entry = field.ENTRY_FIELD(6,'Amplitude legs 1-3',tabs[0],'entry')
        self.amplitude_leg_4_entry = field.ENTRY_FIELD(7, 'Amplitude leg 4', tabs[0], 'entry')
        self.phase_1_entry = field.ENTRY_FIELD(8,'Phaseshift 1',tabs[0],'entry',(25,0))
        self.phase_2_entry = field.ENTRY_FIELD(9,'Phaseshift 2',tabs[0],'entry')
        self.phase_3_entry = field.ENTRY_FIELD(10,'Phaseshift 3',tabs[0],'entry')
        self.phase_4_entry = field.ENTRY_FIELD(11, 'Phaseshift 4',tabs[0],'entry')

        self.frequency_display = field.DISPLAY_FIELD(12, 'Frequency',tabs[0],'display',(25,25))
        self.pwm_frequency_display = field.DISPLAY_FIELD(13,'PWM frequency',tabs[0],'display')
        self.amplitude_display = field.DISPLAY_FIELD(14,'Amplitude legs 1-3',tabs[0],'display')
        self.amplitude_leg_4_display = field.DISPLAY_FIELD(15,'Amplitude leg 4',tabs[0],'display')
        self.phase_1_display = field.DISPLAY_FIELD(16,'Phaseshift 1',tabs[0],'display',(25,0))
        self.phase_2_display = field.DISPLAY_FIELD(17,'Phaseshift 2',tabs[0],'display')
        self.phase_3_display = field.DISPLAY_FIELD(18,'Phaseshift 3',tabs[0],'display')
        self.phase_4_display = field.DISPLAY_FIELD(19,'Phaseshift 4',tabs[0],'display')

        #tab 2 leg 1
        self.tab_2 = leg_data_tab.LEG_DATA_TAB(tabs[1],1)
        #tab 3 leg 2
        self.tab_3 = leg_data_tab.LEG_DATA_TAB(tabs[2],2)
        #tab 4 leg 3
        self.tab_4 = leg_data_tab.LEG_DATA_TAB(tabs[3],3)
        #tab 5 leg 4
        self.tab_5 = leg_data_tab.LEG_DATA_TAB(tabs[4],4)



        self.connection = uart_connection.connection()
        if self.connection():
            self.connection_label.configure(text="Connected")
        
    def refresh_button_event(self):
        self.connection = uart_connection.connection()
        if self.connection():
            self.connection_label.configure(text="Connected")

    def start_button_event(self):
        self.enable_all()
    
    def stop_button_event(self):
        self.disable_all()

    def update_button_event(self):
        self.update_all_fields()
        freq_command = command.command("frequency",int(self.new_frequency))
        print(freq_command())
        self.connection.send(freq_command)

    def update_all_fields(self):
        if(self.enable_leg_1.get_data() or self.enable_leg_2.get_data() or self.enable_leg_3.get_data() or self.enable_leg_4.get_data()):
            self.new_frequency = self.frequency_entry.get_data()
            new_pwm_frequency = self.pwm_frequency_entry.get_data()
            
            self.frequency_display.update(self.new_frequency)
            self.tab_2.update('Frequency',self.new_frequency)
            self.tab_3.update('Frequency',self.new_frequency)
            self.tab_4.update('Frequency',self.new_frequency)
            self.tab_5.update('Frequency',self.new_frequency)

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
