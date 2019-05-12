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
        #tab_names = ["General", "Leg 1", "Leg 2", "Leg 3", "Leg 4"]

        #for i in range(0

        #Tab 1: General settings  
        tab1 = ttk.Frame(tabControl)
        #tabControl.pack(expand=1, fill= 'both'

        tabControl.add(tab1, text='General')
        #Tab 2: Settings Leg 1
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Leg 1')
        #tab 3: Settings Leg 2
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='leg 2')
        #tab 4: Settings Leg 3
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text='leg 3')
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
        ttk.EnableLeg1 = Checkbutton(tab1, text="Enable Leg 1", variable = ttk.var1)
        ttk.EnableLeg1.grid(row=checkbutton_row, column=0)
        #Enable Leg 2
        ttk.var2 = IntVar()
        ttk.EnableLeg2 = Checkbutton(tab1, text="Enable Leg 2", variable = ttk.var2)
        ttk.EnableLeg2.grid(row=checkbutton_row,column=1)
        #Enable Leg 3
        ttk.var3 = IntVar()
        ttk.EnableLeg3 = Checkbutton(tab1, text="Enable Leg 3", variable = ttk.var3)
        ttk.EnableLeg3.grid(row=checkbutton_row,column=2)
        #Enable Leg 4
        ttk.var4 = IntVar()
        ttk.EnableLeg4 = Checkbutton(tab1, text="Enable Leg 4", variable = ttk.var4)
        ttk.EnableLeg4.grid(row=checkbutton_row,column=3)
        #Blank Line
        ttk.blankLine1 = Label(tab1,text="").grid(row=blankline1_row,column=0)
        #Start button        
        ttk.start_button = Button(tab1, text="START", command = self.startbutton, bg = 'red')
        ttk.start_button.grid(row=button_row, column=0)
        #General update button
        update_general = Button(tab1, text="Update", command = self.updategeneral).grid(row=button_row, column=1, columnspan=2)
        #Stop button
        ttk.stop_button  = Button(tab1, text='STOP', command = self.stopbutton)
        ttk.stop_button.grid(row=button_row,column=3)
        
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
        ttk.phase2Label = Label(tab1, text="phase shift leg 2:").grid(row=phase2_row,column=0)
        ttk.phase2Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase2Entry.grid(row=phase2_row,column=2)
        #Phase3
        ttk.phase3Label = Label(tab1, text="phase shift leg 3:").grid(row=phase3_row,column=0)
        ttk.phase3Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase3Entry.grid(row=phase3_row,column=2)
        #Phase4
        ttk.phase4Label = Label(tab1, text="phase shift leg 4:").grid(row=phase4_row,column=0)
        ttk.phase4Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase4Entry.grid(row=phase4_row,column=2)
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
        frame1 = Frame(tab2)
        frame1.pack()
        frame2 = Frame(tab2)
        frame2.pack()
        frame3 = Frame(tab2)
        frame3.pack()
        frame4 = Frame(tab2)
        frame4.pack()
        frame5 = Frame(tab2)
        frame5.pack()
        frame6 = Frame(tab2)
        frame6.pack()
        ttk.titleLabel = Label(frame1, text="Leg 1 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab2setfrequencyLabel = Label(frame2, text="current Frequency:").pack(side=LEFT)
        ttk.tab2currentfrequencyLabel = Label(frame2, text="- Hz")
        ttk.tab2currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab2setPWMfrequencyLabel = Label(frame3, text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab2currentPWMfrequencyLabel = Label(frame3, text="- Hz")
        ttk.tab2currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab2setAmplitudeLabel = Label(frame4, text="Current amplitude:").pack(side=LEFT)
        ttk.tab2ampinfo = Label(frame4, text="- %")
        ttk.tab2ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab2phase1 = Label(frame5, text="Current phase shift:").pack(side=LEFT)
        ttk.tab2phase1info = Label(frame5, text="- °")
        ttk.tab2phase1info.pack(side=LEFT)


        #Tab 3 Layout
        frame1 = Frame(tab3)
        frame1.pack()
        frame2 = Frame(tab3)
        frame2.pack()
        frame3 = Frame(tab3)
        frame3.pack()
        frame4 = Frame(tab3)
        frame4.pack()
        frame5 = Frame(tab3)
        frame5.pack()
        frame6 = Frame(tab3)
        frame6.pack()
        ttk.titleLabel = Label(frame1, text="Leg 2 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab3setfrequencyLabel = Label(frame2, text="Current Frequency:").pack(side=LEFT)
        ttk.tab3currentfrequencyLabel = Label(frame2, text="- Hz")
        ttk.tab3currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab3setPWMfrequencyLabel = Label(frame3, text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab3currentPWMfrequencyLabel = Label(frame3, text="- Hz")
        ttk.tab3currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab3setAmplitudeLabel = Label(frame4, text="Current amplitude:").pack(side=LEFT)
        ttk.tab3ampinfo = Label(frame4, text="- %")
        ttk.tab3ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab3phase2 = Label(frame5, text="Current phase shift:").pack(side=LEFT)
        ttk.tab3phase2info = Label(frame5, text="- °")
        ttk.tab3phase2info.pack(side=LEFT)


        #Tab 4 Layout
        frame1 = Frame(tab4)
        frame1.pack()
        frame2 = Frame(tab4)
        frame2.pack()
        frame3 = Frame(tab4)
        frame3.pack()
        frame4 = Frame(tab4)
        frame4.pack()
        frame5 = Frame(tab4)
        frame5.pack()
        frame6 = Frame(tab4)
        frame6.pack()
        ttk.titleLabel = Label(frame1, text="Leg 3 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab4setfrequencyLabel = Label(frame2, text="Current Frequency:").pack(side=LEFT)
        ttk.tab4currentfrequencyLabel = Label(frame2, text="- Hz")
        ttk.tab4currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab4setPWMfrequencyLabel = Label(frame3, text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab4currentPWMfrequencyLabel = Label(frame3, text="- Hz")
        ttk.tab4currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab4setAmplitudeLabel = Label(frame4, text="Current amplitude:").pack(side=LEFT)
        ttk.tab4ampinfo = Label(frame4, text="- %")
        ttk.tab4ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab4phase3 = Label(frame5, text="Current phase shift:").pack(side=LEFT)
        ttk.tab4phase3info = Label(frame5, text="- °")
        ttk.tab4phase3info.pack(side=LEFT)


        #Tab 5 Layout
        frame1 = Frame(tab5)
        frame1.pack()
        frame2 = Frame(tab5)
        frame2.pack()
        frame3 = Frame(tab5)
        frame3.pack()
        frame4 = Frame(tab5)
        frame4.pack()
        frame5 = Frame(tab5)
        frame5.pack()
        frame6 = Frame(tab5)
        frame6.pack()

        ttk.titleLabel = Label(frame1, text="Leg 4 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab5setfrequencyLabel = Label(frame2, text="Current Frequency:").pack(side=LEFT)
        ttk.tab5currentfrequencyLabel = Label(frame2, text="- Hz")
        ttk.tab5currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab5setPWMfrequencyLabel = Label(frame3, text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab5currentPWMfrequencyLabel = Label(frame3, text="- Hz")
        ttk.tab5currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab5setAmplitudetab2Label = Label(frame4, text="Current amplitude:").pack(side=LEFT)
        ttk.tab5ampinfo = Label(frame4, text="- %")
        ttk.tab5ampinfo.pack(side=LEFT)
        #Current phase Leg 4
        ttk.tab5phase4 = Label(frame5, text="Current phase shift:").pack(side=LEFT)
        ttk.tab5phase4info = Label(frame5, text="- °")
        ttk.tab5phase4info.pack(side=LEFT)


    def updategeneral(self):
        newfrequency = int(ttk.FreqEntry.get())
        ttk.currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        ttk.tab2currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        ttk.tab3currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        ttk.tab4currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
        ttk.tab5currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))

        newPWMfrequency = int(ttk.PWMFreqEntry.get())
        ttk.currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        ttk.tab2currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        ttk.tab3currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        ttk.tab4currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
        ttk.tab5currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))

        newamplitude = int(ttk.AmpEntry.get())
        ttk.ampinfo.configure(text="{} %".format(newamplitude))
        ttk.tab2ampinfo.configure(text="{} %".format(newamplitude))
        ttk.tab3ampinfo.configure(text="{} %".format(newamplitude))
        ttk.tab4ampinfo.configure(text="{} %".format(newamplitude))
        ttk.tab5ampinfo.configure(text="{} %".format(newamplitude))

        newphase1 = int(ttk.phase1Entry.get())
        ttk.phase1info.configure(text="{}°".format(newphase1))
        ttk.tab2phase1info.configure(text="{}°".format(newphase1))

        newphase2 = int(ttk.phase2Entry.get())
        ttk.phase2info.configure(text="{}°".format(newphase2))
        ttk.tab3phase2info.configure(text="{}°".format(newphase2))

        newphase3 = int(ttk.phase3Entry.get())
        ttk.phase3info.configure(text="{}°".format(newphase3))
        ttk.tab4phase3info.configure(text="{}°".format(newphase3))

        newphase4 = int(ttk.phase4Entry.get())
        ttk.phase4info.configure(text="{}°".format(newphase4))
        ttk.tab5phase4info.configure(text="{}°".format(newphase4))

        ttk.FreqEntry.delete(0,'end')
        ttk.PWMFreqEntry.delete(0,'end')
        ttk.AmpEntry.delete(0,'end')
        ttk.phase1Entry.delete(0,'end')
        ttk.phase2Entry.delete(0,'end')
        ttk.phase3Entry.delete(0,'end')
        ttk.phase4Entry.delete(0,'end')

        prepare_command = command.command("prepare")
        print(prepare_command())
        #self.connection.send(prepare_command)

        freq_command = command.command("frequency", newfrequency)
        print(freq_command())
        #self.connection.send(freq_command)

        keyfreq_command = command.command("keyfrequency", newPWMfrequency)
        print(keyfreq_command())
        #self.connection.send(keyfreq_command)

        amplitude_command = command.command("amplitude", newamplitude)
        print(amplitude_command())
        #self.connection.send(keyfreq_command)
        
        #Check if channel is enabled, if channel is ennabled send phaseshift
        if (ttk.var1.get()):
            phase1_command = command.command("phaseshift",newphase1,0) 
            print(phase1_command())
            #self.connection.send(phase1_command)
        if (ttk.var2.get()):
            phase2_command = command.command("phaseshift",newphase2,1)
            print(phase2_command())
            #self.connection.send(phase2_command)
        if (ttk.var3.get()):
            phase3_command = command.command("phaseshift",newphase3,2)
            print(phase3_command())
            #self.connection.send(phase3_command)
        if (ttk.var4.get()):
            phase4_command = command.command("phaseshift",newphase4,3)
            print(phase4_command())
            #self.connection.send(phase4_command)

        execute_command = command.command("execute")
        print(execute_command())
        #self.connection.send(execute_command)
        return 0

            

    def startbutton(self):
        ttk.start_button.configure(bg = 'green')
        ttk.FreqEntry['state'] = NORMAL
        ttk.PWMFreqEntry['state'] = NORMAL
        ttk.AmpEntry['state'] = NORMAL
       
        ttk.EnableLeg1['state'] = DISABLED
        ttk.EnableLeg2['state'] = DISABLED
        ttk.EnableLeg3['state'] = DISABLED
        ttk.EnableLeg4['state'] = DISABLED

        if (ttk.var1.get()):
            ttk.phase1Entry['state'] = NORMAL
        if (ttk.var2.get()):
            ttk.phase2Entry['state'] = NORMAL
        if (ttk.var3.get()):
            ttk.phase3Entry['state'] = NORMAL
        if (ttk.var4.get()):
            ttk.phase4Entry['state'] = NORMAL

        start_command = command.command("start")
        print(start_command())
        #self.connection.send(start_command)

    def stopbutton(self):
        ttk.start_button.configure(bg = 'red')

        ttk.FreqEntry.delete(0,'end')
        ttk.FreqEntry['state'] = DISABLED
        ttk.currentfrequencyLabel.configure(text="- Hz")
        ttk.tab2currentfrequencyLabel.configure(text="- Hz")
        ttk.tab3currentfrequencyLabel.configure(text="- Hz")
        ttk.tab4currentfrequencyLabel.configure(text="- Hz")
        ttk.tab5currentfrequencyLabel.configure(text="- Hz")

        ttk.PWMFreqEntry.delete(0,'end')
        ttk.PWMFreqEntry['state'] = DISABLED
        ttk.tab2currentPWMfrequencyLabel.configure(text="- Hz")
        ttk.tab3currentPWMfrequencyLabel.configure(text="- Hz")
        ttk.tab4currentPWMfrequencyLabel.configure(text="- Hz")
        ttk.tab5currentPWMfrequencyLabel.configure(text="- Hz")
        
        ttk.AmpEntry.delete(0,'end')
        ttk.AmpEntry['state'] = DISABLED
        ttk.ampinfo.configure(text="- %")
        ttk.tab2ampinfo.configure(text="- %")
        ttk.tab3ampinfo.configure(text="- %")
        ttk.tab4ampinfo.configure(text="- %")
        ttk.tab5ampinfo.configure(text="- %")

        ttk.phase1Entry.delete(0,'end')
        ttk.phase1Entry['state'] = DISABLED
        ttk.phase1info.configure(text="- °")
        ttk.tab2phase1info.configure(text="- °")
        
        ttk.phase2Entry.delete(0,'end')
        ttk.phase2Entry['state'] = DISABLED
        ttk.phase2info.configure(text="- °")
        ttk.tab3phase2info.configure(text="- °")

        ttk.phase3Entry.delete(0,'end')
        ttk.phase3Entry['state'] = DISABLED
        ttk.phase3info.configure(text="- °")
        ttk.tab4phase3info.configure(text="- °")

        ttk.phase4Entry.delete(0,'end')
        ttk.phase4Entry['state'] = DISABLED
        ttk.phase4info.configure(text="- °")
        ttk.tab5phase4info.configure(text="- °")

        stop_command = command.command("stop")
        print(stop_command())
        #self.connection.send(stop_command)
        return 0

        


root = Tk()
this_gui = GUI(root)

while True:
    root.update_idletasks()
    root.update()
