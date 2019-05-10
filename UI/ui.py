# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
from random import randint


import command
import uart_connection

class GUI:
    def __init__(self,master):
        self.connection = uart_connection.connection()
        self.master = master
        self.master.title("PWM Controller")
        
        #Creation of tabs
        tabControl = ttk.Notebook(self.master)
        #Tab 1: General settings  
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='General')
        #Tab 2: Settings Leg 1
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Leg 1')
        #tabControl.pack(expand=1, fill="both")
        #tab 3: Settings Leg 2
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='leg 2')
        tabControl.pack(expand=1, fill='both')
        #tab 4: Settings Leg 3
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text='leg 3')
        tabControl.pack(expand=1, fill='both')
        #tab 5: Settings Leg 4
        tab5 = ttk.Frame(tabControl)
        tabControl.add(tab5, text='leg 4')
        tabControl.pack(expand=1, fill='both')
       
        #Tab 1 Layout
        title_row = 0
        checkbutton_row = 1
        blankline1_row = 2
        button_row = 3
        blankline2_row = 4
        frequency_row = 5
        PWMfrequency_row = 6
        amplitude_row = 7
        blankline3_row = 8
        phase1_row = 9
        phase2_row = 10
        phase3_row = 11
        phase4_row = 12
        blankline4_row = 13
        current_frequency_row = 14
        current_PWMfrequency_row = 15
        current_amplitude_row = 16
        blankline5_row = 17
        current_phase1_row = 18
        current_phase2_row = 19
        current_phase3_row = 20
        current_phase4_row = 21


        ttk.titletab1Label = Label(tab1, text="PWM Controller general settings", font = "Helvetica 16 bold italic").grid(row=title_row, column=0, columnspan = 4)
        #Enable Leg 1
        ttk.var1 = IntVar()
        EnableLeg1 = Checkbutton(tab1, text="Enable Leg 1", variable = ttk.var1)
        EnableLeg1.grid(row=checkbutton_row, column=0)
        #Enable Leg 2
        ttk.var2 = IntVar()
        EnableLeg2 = Checkbutton(tab1, text="Enable Leg 2", variable = ttk.var2)
        EnableLeg2.grid(row=checkbutton_row,column=1)
        #Enable Leg 3
        ttk.var3 = IntVar()
        EnableLeg3 = Checkbutton(tab1, text="Enable Leg 3", variable = ttk.var3)
        EnableLeg3.grid(row=checkbutton_row,column=2)
        #Enable Leg 4
        ttk.var4 = IntVar()
        EnableLeg4 = Checkbutton(tab1, text="Enable Leg 4", variable = ttk.var4)
        EnableLeg4.grid(row=checkbutton_row,column=3)
        #Blank Line
        ttk.blankLine1 = Label(tab1,text="").grid(row=blankline1_row,column=0)
        #Start button        
        self.start_button = Button(tab1, text="START", command = self.startbutton, bg = 'red')
        self.start_button.grid(row=button_row, column=0)
        #General update button
        update_general = Button(tab1, text="Update", command = self.updategeneral).grid(row=button_row, column=1, columnspan=2)
        #Stop button
        self.stop_button  = Button(tab1, text='STOP', command = self.stopbutton)
        self.stop_button.grid(row=button_row,column=3)
        
        #Blank line
        ttk.blankLine2 = Label(tab1, text="").grid(row=blankline2_row,column=0)
        
        #Frequency
        ttk.FreqLabel = Label(tab1, text="Frequency:").grid(row=frequency_row, column=0)
        ttk.FreqEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.FreqEntry.grid(row=frequency_row, column=2)
        #PWM Frequency
        ttk.PWMFreqLabel = Label(tab1, text="PWM Frequency:").grid(row=PWMfrequency_row, column=0)
        ttk.PWMFreqEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.PWMFreqEntry.grid(row=PWMfrequency_row, column=2)
        #Amplitude
        ttk.AmpLabel = Label(tab1, text="Amplitude:").grid(row=amplitude_row,column=0)
        ttk.AmpEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.AmpEntry.grid(row=amplitude_row, column=2)
        
        #Blank line
        ttk.witregel = Label(tab1,text = "").grid(row = blankline3_row, column=0, columnspan=4)
        #Phase1
        ttk.phase1Label = Label(tab1, text="phase shift leg 1:").grid(row=phase1_row,column=0)
        ttk.phase1Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase1Entry.grid(row=phase1_row,column=2)
        #phase2
        ttk.phase1Label = Label(tab1, text="phase shift leg 2:").grid(row=phase2_row,column=0)
        ttk.phase1Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase1Entry.grid(row=phase2_row,column=2)
        #Phase3
        ttk.phase1Label = Label(tab1, text="phase shift leg 3:").grid(row=phase3_row,column=0)
        ttk.phase1Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase1Entry.grid(row=phase3_row,column=2)
        #Phase4
        ttk.phase1Label = Label(tab1, text="phase shift leg 4:").grid(row=phase4_row,column=0)
        ttk.phase1Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase1Entry.grid(row=phase4_row,column=2)
        #blank line
        ttk.witregel = Label(tab1,text = "").grid(row = blankline4_row, column=0, columnspan=4)
        #Current frequency setting
        ttk.setfrequencyLabel = Label(tab1, text="Current Frequency:").grid(row=current_frequency_row, column = 0)
        ttk.currentfrequencyLabel = Label(tab1, text="- Hz")
        ttk.currentfrequencyLabel.grid(row=current_frequency_row, column = 2)
        #Current PWM frequency setting
        ttk.setPWMfrequencyLabel = Label(tab1, text="Current PWM Frequency:").grid(row=current_PWMfrequency_row, column = 0)
        ttk.currentPWMfrequencyLabel = Label(tab1, text="- Hz")
        ttk.currentPWMfrequencyLabel.grid(row=current_PWMfrequency_row, column=2)
        #Current amplitude setting
        ttk.setAmplitudeLabel = Label(tab1, text="Current amplitude:").grid(row = current_amplitude_row, column=0)
        ttk.ampinfo = Label(tab1, text="- %")
        ttk.ampinfo.grid(row=current_amplitude_row,column=2)
        #blank line
        ttk.blankLine5 = Label(tab1, text="").grid(row=blankline5_row,column=0)
        #Current phase Leg 1
        ttk.phase1 = Label(tab1, text="Current phase shift leg 1:").grid(row=current_phase1_row,column=0)
        ttk.phase1info = Label(tab1, text="- °")
        ttk.phase1info.grid(row=current_phase1_row,column=2)
        #Current Phase Leg 2
        ttk.phase2 = Label(tab1, text="Current phase shift leg 2:").grid(row=current_phase2_row,column=0)
        ttk.phase2info = Label(tab1, text="- °")
        ttk.phase2info.grid(row=current_phase2_row,column=2)
        #Current Phase Leg 3
        ttk.phase3 = Label(tab1, text="Current phase shift leg 3:").grid(row=current_phase3_row,column=0)
        ttk.phase3info = Label(tab1, text="- °")
        ttk.phase3info.grid(row=current_phase3_row,column=2)
        #Current Phase Leg 4
        ttk.phase4 = Label(tab1, text="Current phase shift leg 4:").grid(row=current_phase4_row,column=0)
        ttk.phase4info = Label(tab1, text="- °")
        ttk.phase4info.grid(row=current_phase4_row,column=2)

        #Tab 2 Layout
        ttk.titletab2Label = Label(tab2, text="Leg 1 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 3)
        #Update leg 1
        leg1_button = Button(tab2, text="Update Leg 1").grid(row=0, column=4)
        #Leg 1 Phase setting
        ttk.Phase1Label = Label(tab2, text="Phaseshift:").grid(row=1, column=0)
        ttk.Phase1Entry = Entry(tab2, bd=5)
        ttk.Phase1Entry.grid(row=1, column=1)

        #Tab 3 Layout
        ttk.titletab3Label = Label(tab3, text="Leg 2 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        #Update leg 2
        leg2_button = Button(tab3, text="Update Leg 2").grid(row=0, column=2)
        #Leg 2 phase setting
        ttk.Phase2Label = Label(tab3, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase2Entry = Entry(tab3, bd=5)
        ttk.Phase2Entry.grid(row=3, column=1)

        #Tab 4 Layout
        ttk.titletab4Label = Label(tab4, text="Leg 3 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        #Update leg 3
        leg3_button = Button(tab4, text="Update Leg 3").grid(row=0, column=2)
        #Leg 3 phase setting
        ttk.Phase3Label = Label(tab4, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase3Entry = Entry(tab4, bd=5)
        ttk.Phase3Entry.grid(row=3, column=1)

        #Tab 5 Layout
        ttk.titletab5Label = Label(tab5, text="Leg 4 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        #Update leg 4        
        leg4_button = Button(tab5, text="Update Leg 4").grid(row=0, column=2)
        #Leg 4 phase setting
        ttk.Phase4Label = Label(tab5, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase4Entry = Entry(tab5, bd=5)
        ttk.Phase4Entry.grid(row=3, column=1)


    def updategeneral(self):
        newfrequency = int(ttk.FreqEntry.get())
        ttk.currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        
        newPWMfrequency = int(ttk.PWMFreqEntry.get())
        ttk.currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        
        newamplitude = int(ttk.AmpEntry.get())
        ttk.ampinfo.configure(text="{} %".format(newamplitude))

        ttk.FreqEntry.delete(0,'end')
        ttk.PWMFreqEntry.delete(0,'end')
        ttk.AmpEntry.delete(0,'end')

        hallo1 = command.command("frequency",newfrequency*100)
        print(hallo1())
        self.connection.send(hallo1)
        return 0

            

    def startbutton(self):
        self.start_button.configure(bg = 'green')
        ttk.FreqEntry['state'] = NORMAL
        ttk.PWMFreqEntry['state'] = NORMAL
        ttk.AmpEntry['state'] = NORMAL

        start_command = command.command("start")
        print(start_command())
        self.connection.send(start_command)

    def stopbutton(self):
        self.start_button.configure(bg = 'red')

        ttk.FreqEntry.delete(0,'end')
        ttk.FreqEntry['state'] = DISABLED
        
        ttk.PWMFreqEntry.delete(0,'end')
        ttk.PWMFreqEntry['state'] = DISABLED

        ttk.AmpEntry.delete(0,'end')
        ttk.AmpEntry['state'] = DISABLED

        ttk.currentfrequencyLabel.configure(text="- Hz")
        ttk.currentPWMfrequencyLabel.configure(text="- Hz")
        return 0

    def update_leg_1(self):
        #data = []
        #data.append(int(self.FreqEntry.get())*100)
        #data.append(int(self.Amp1Entry.get()))
        #data.append(int(self.Phase1Entry.get()))
        #data.append(int(self.Phase2Entry.get()))
        #data.append(int(self.PWMFreqEntry.get()))
        #return data
        return 0

    def update_leg_2(self):
        return 0

    def update_leg_3(self):
        return 0

    def update_leg_4(self):
        return 0

    def update_labels(self):
        return 0
        


root = Tk()
this_gui = GUI(root)

while True:
    root.update_idletasks()
    root.update()
