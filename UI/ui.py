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
           
        tabControl=ttk.Notebook(self.master)
        #Tab1  
        tab1=ttk.Frame(tabControl)
        tabControl.add(tab1, text='General')
        #Tab2  
        tab2=ttk.Frame(tabControl)
        tabControl.add(tab2, text='Leg 1')
        tabControl.pack(expand=1, fill="both")
        #tab3
        tab3=ttk.Frame(tabControl)
        tabControl.add(tab3, text='leg 2')
        tabControl.pack(expand=1, fill='both')
        #tab4
        tab4=ttk.Frame(tabControl)
        tabControl.add(tab4, text='leg 3')
        tabControl.pack(expand=1, fill='both')
        #tab5
        tab5=ttk.Frame(tabControl)
        tabControl.add(tab5, text='leg 4')
        tabControl.pack(expand=1, fill='both')
       

        #labels
        ttk.titletab1Label = Label(tab1, text="PWM Controller general settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 3)
        ttk.titletab2Label = Label(tab2, text="Leg 1 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        ttk.titletab3Label = Label(tab3, text="Leg 2 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        ttk.titletab4Label = Label(tab4, text="Leg 3 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)
        ttk.titletab5Label = Label(tab5, text="Leg 4 settings", font = "Helvetica 16 bold italic").grid(row=0, column=0, columnspan = 2)

        #DataLabels
        ttk.witregel = Label(tab1, text="")
        ttk.witregel1 = Label(tab1, text="")
        ttk.witregel2 = Label(tab1, text="")
        ttk.witregel3 = Label(tab1, text="")
        ttk.witregel4 = Label(tab1, text="")

        ttk.witregel5 = Label(tab1, text="").grid(row=2,column=0)

        ttk.witregel.grid(row = 5, column=0, columnspan=4)

        ttk.setfrequencyLabel = Label(tab1, text="Current Frequency:").grid(row=6, column = 0)
        ttk.currentfrequencyLabel = Label(tab1, text="-")
        ttk.currentfrequencyLabel.grid(row=6, column = 1)

        ttk.setPWMfrequencyLabel = Label(tab1, text="Current PWM Frequency:").grid(row=7, column = 0)
        ttk.currentPWMfrequencyLabel = Label(tab1, text="-")
        ttk.currentPWMfrequencyLabel.grid(row=7, column=1)

        ttk.witregel1.grid(row=8,column=0)
        ttk.leg1settings = Label(tab1, text="Leg 1",font="helvetica 14 bold italic").grid(row=9,column=0)
        ttk.amp1 = Label(tab1, text="Amplitude:").grid(row=10,column=0)
        ttk.amp1info = Label(tab1, text="-")
        ttk.amp1info.grid(row=10,column=1)
        ttk.phase1 = Label(tab1, text="Phaseshift:").grid(row=11,column=0)
        ttk.phase1info = Label(tab1, text="-")
        ttk.phase1info.grid(row=11,column=1)
        
        ttk.witregel2.grid(row=12,column=0)
        ttk.leg2ettings = Label(tab1, text="Leg 2",font="helvetica 14 bold italic").grid(row=13,column=0)
        ttk.amp2 = Label(tab1, text="Amplitude:").grid(row=14,column=0)
        ttk.amp2info = Label(tab1, text="-")
        ttk.amp2info.grid(row=14,column=1)
        ttk.phase2 = Label(tab1, text="Phaseshift:").grid(row=15,column=0)
        ttk.phase2info = Label(tab1, text="-")
        ttk.phase2info.grid(row=15,column=1)
        
        ttk.witregel3.grid(row=16,column=0)
        ttk.leg3settings = Label(tab1, text="Leg 3",font="helvetica 14 bold italic").grid(row=17,column=0)
        ttk.amp3 = Label(tab1, text="Amplitude:").grid(row=18,column=0)
        ttk.amp3info = Label(tab1, text="-")
        ttk.amp3info.grid(row=18,column=1)
        ttk.phase3 = Label(tab1, text="Phaseshift:").grid(row=19,column=0)
        ttk.phase3info = Label(tab1, text="-")
        ttk.phase3info.grid(row=19,column=1)

        ttk.witregel4.grid(row=20,column=0)
        ttk.leg4settings = Label(tab1, text="Leg 4",font="helvetica 14 bold italic").grid(row=21,column=0)
        ttk.amp4 = Label(tab1, text="Amplitude:").grid(row=22,column=0)
        ttk.amp4info = Label(tab1, text="-")
        ttk.amp4info.grid(row=22,column=1)
        ttk.phase4 = Label(tab1, text="Phaseshift:").grid(row=23,column=0)
        ttk.phase4info = Label(tab1, text="-")
        ttk.phase4info.grid(row=23,column=1)


        ttk.FreqLabel = Label(tab1, text="Frequency:").grid(row=3, column=0)
        ttk.Amp1Label = Label(tab2, text="Amplitude:").grid(row=2, column=0)
        ttk.Amp2Label = Label(tab3, text="Amplitude:").grid(row=2, column=0)
        ttk.Amp3Label = Label(tab4, text="Amplitude:").grid(row=2, column=0)
        ttk.Amp4Label = Label(tab5, text="Amplitude:").grid(row=2, column=0)
        ttk.Phase1Label = Label(tab2, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase2Label = Label(tab3, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase3Label = Label(tab4, text="Phaseshift:").grid(row=3, column=0)
        ttk.Phase4Label = Label(tab5, text="Phaseshift:").grid(row=3, column=0)
        ttk.pwmfreqLabel = Label(tab1, text="PWM Frequency:").grid(row=4, column=0)

        #Parameter Entries
        ttk.FreqEntry = Entry(tab1, bd=5)
        ttk.Amp1Entry = Entry(tab2, bd=5)
        ttk.Amp2Entry = Entry(tab3, bd=5)
        ttk.Amp3Entry = Entry(tab4, bd=5)
        ttk.Amp4Entry = Entry(tab5, bd=5)
        ttk.Phase1Entry = Entry(tab2, bd=5)
        ttk.Phase2Entry = Entry(tab3, bd=5)
        ttk.Phase3Entry = Entry(tab4, bd=5)
        ttk.Phase4Entry = Entry(tab5, bd=5)
        ttk.PWMFreqEntry = Entry(tab1, bd=5)

        #Buttons
        self.start_button = Button(tab1, text="START", command = self.startbutton, bg = 'red')
        self.start_button.grid(row=1, column=0)
        self.stop_button  = Button(tab1, text='STOP', command = self.stopbutton)
        self.stop_button.grid(row=1,column=2)
        leg1_button = Button(tab2, text="Update Leg 1").grid(row=0, column=2)
        leg2_button = Button(tab3, text="Update Leg 2").grid(row=0, column=2)
        leg3_button = Button(tab4, text="Update Leg 3").grid(row=0, column=2)
        leg4_button = Button(tab5, text="Update Leg 4").grid(row=0, column=2)

        update_general = Button(tab1, text="Update", command = self.updategeneral).grid(row=1, column=1)

        #Entry Location
        ttk.FreqEntry.grid(row=3, column=1)
        ttk.Amp1Entry.grid(row=2, column=1)
        ttk.Amp2Entry.grid(row=2, column=1)
        ttk.Amp3Entry.grid(row=2, column=1)
        ttk.Amp4Entry.grid(row=2, column=1)
        ttk.Phase1Entry.grid(row=3, column=1)
        ttk.Phase2Entry.grid(row=3, column=1)
        ttk.Phase3Entry.grid(row=3, column=1)
        ttk.Phase4Entry.grid(row=3, column=1)
        ttk.PWMFreqEntry.grid(row=4, column=1)
        
    def updategeneral(self):
        newfrequency = ttk.FreqEntry.get()
        newPWMfrequency = ttk.PWMFreqEntry.get()
        newamp1 = ttk.Amp1Entry.get()
        ttk.currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        ttk.currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        ttk.amp1info.configure(text="{} %".format(newamp1))
        return 0

            

    def startbutton(self):
        hallo1 = command.command("frequency",int(ttk.FreqEntry.get())*100)
        print(hallo1())
        self.connection.send(hallo1)
        hallo2 = command.command("amplitude",int(ttk.Amp1Entry.get()),0)
        print(hallo2())
        #parameters = self.collectdata()
        #prepare = command.command("prepare")
        #frequencyupdate = command.command("frequency",parameters[0])
        #amplitudeupdate = command.command("amplitude",parameters[1])
        #phase1update    = command.command("phaseshift",parameters[2])
        #phase2update    = command.command("phaseshift",parameters[3])
        #pwmfrequpdate   = command.command("keyfrequency",parameters[4])
        #print(prepare())
        #print(frequencyupdate())
        #print(amplitudeupdate())
        #print(phase1update())
        #print(phase2update())
        #print(pwmfrequpdate())
        self.start_button.configure(bg = 'green')
        return 0

    def stopbutton(self):
        self.start_button.configure(bg = 'red')
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
