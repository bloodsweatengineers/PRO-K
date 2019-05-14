# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
from random import randint

import serial
import command
import uart_connection
import serial.tools.list_ports


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
        button_row = 3
        frequency_row = 5
        PWMfrequency_row = 6
        amplitude_row = 7
        amplitude_leg4_row = 8
        phase1_row = 9
        phase2_row = 10
        phase3_row = 11
        phase4_row = 12
        current_frequency_row = 14
        current_PWMfrequency_row = 15
        current_amplitude_row = 16
        current_leg4_amplitude_row = 17
        current_phase1_row = 18
        current_phase2_row = 19
        current_phase3_row = 20
        current_phase4_row = 21

        #--Tab 1 layout--
        ttk.titletab1Label = Label(tab1, text="PWM Controller general settings", font = "Helvetica 16 bold italic").grid(row=title_row, column=0, columnspan = 4)
        
        #Enable Leg 1
        ttk.var1 = IntVar()
        ttk.EnableLeg1 = Checkbutton(tab1, text="Enable Leg 1", variable = ttk.var1)
        ttk.EnableLeg1.grid(row=checkbutton_row, column=0,pady=(10,10))
        #Enable Leg 2
        ttk.var2 = IntVar()
        ttk.EnableLeg2 = Checkbutton(tab1, text="Enable Leg 2", variable = ttk.var2)
        ttk.EnableLeg2.grid(row=checkbutton_row,column=1,pady=(10,10))
        #Enable Leg 3
        ttk.var3 = IntVar()
        ttk.EnableLeg3 = Checkbutton(tab1, text="Enable Leg 3", variable = ttk.var3)
        ttk.EnableLeg3.grid(row=checkbutton_row,column=2,pady=(10,10))
        #Enable Leg 4
        ttk.var4 = IntVar()
        ttk.EnableLeg4 = Checkbutton(tab1, text="Enable Leg 4", variable = ttk.var4)
        ttk.EnableLeg4.grid(row=checkbutton_row,column=3, pady=(10,10))
        
        #Start button        
        ttk.start_button = Button(tab1, text="START", command = self.startbutton, bg = 'red')
        ttk.start_button.grid(row=button_row, column=0,pady=(10,10))
        #General update button
        update_general = Button(tab1, text="Update", command = self.updategeneral).grid(row=button_row, column=1, columnspan=2,pady=(10,10))
        #Stop button
        ttk.stop_button  = Button(tab1, text='STOP', command = self.stopbutton)
        ttk.stop_button.grid(row=button_row,column=3,pady=(10,10))
        
        #Frequency
        ttk.FreqLabel = Label(tab1, text="Frequency:").grid(row=frequency_row, column=0,pady=(10,0), sticky='E')
        ttk.FreqEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.FreqEntry.grid(row=frequency_row, column=2,pady=(10,1))
        
        #PWM Frequency
        ttk.PWMFreqLabel = Label(tab1, text="PWM Frequency:").grid(row=PWMfrequency_row, column=0,sticky='E')
        ttk.PWMFreqEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.PWMFreqEntry.grid(row=PWMfrequency_row, column=2)
        
        #Three phase amplitude leg 1-3
        ttk.AmpLabel = Label(tab1, text="Amplitude Leg 1 - 3:").grid(row=amplitude_row,column=0,sticky='E')
        ttk.AmpEntry = Entry(tab1, bd=5, state = 'disabled')
        ttk.AmpEntry.grid(row=amplitude_row, column=2)
        
        #Amplitude leg 4
        ttk.leg4AmpLabel = Label(tab1, text="Amplitude Leg 4:").grid(row=amplitude_leg4_row,column=0,sticky='E')
        ttk.leg4AmpEntry = Entry(tab1,bd=5, state='disabled')
        ttk.leg4AmpEntry.grid(row=amplitude_leg4_row, column=2)
        
        #Phase1
        ttk.phase1Label = Label(tab1, text="phase shift leg 1:").grid(row=phase1_row,column=0,pady=(25,0),sticky='E')
        ttk.phase1Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase1Entry.grid(row=phase1_row,column=2,pady=(25,0))
        
        #phase2
        ttk.phase2Label = Label(tab1, text="phase shift leg 2:").grid(row=phase2_row,column=0,sticky='E')
        ttk.phase2Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase2Entry.grid(row=phase2_row,column=2)
        
        #Phase3
        ttk.phase3Label = Label(tab1, text="phase shift leg 3:").grid(row=phase3_row,column=0,sticky='E')
        ttk.phase3Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase3Entry.grid(row=phase3_row,column=2)
        
        #Phase4
        ttk.phase4Label = Label(tab1, text="phase shift leg 4:").grid(row=phase4_row,column=0,sticky='E')
        ttk.phase4Entry = Entry(tab1, bd=5, state='disabled')
        ttk.phase4Entry.grid(row=phase4_row,column=2)
        
        #Current frequency setting
        ttk.setfrequencyLabel = Label(tab1, text="Current Frequency:").grid(row=current_frequency_row, column = 0,pady=(25,0),sticky='EW')
        ttk.currentfrequencyLabel = Label(tab1, text="- Hz")
        ttk.currentfrequencyLabel.grid(row=current_frequency_row, column = 2,pady=(25,0),sticky='EW')
        #Current PWM frequency setting
        ttk.setPWMfrequencyLabel = Label(tab1, text="Current PWM Frequency:").grid(row=current_PWMfrequency_row, column = 0,sticky='EW')
        ttk.currentPWMfrequencyLabel = Label(tab1, text="- Hz")
        ttk.currentPWMfrequencyLabel.grid(row=current_PWMfrequency_row, column=2,sticky='EW')
        
        #Current amplitude setting leg 1 - 3
        ttk.setAmplitudeLabel = Label(tab1, text="Current amplitude leg 1 - 3:").grid(row = current_amplitude_row, column=0,sticky='EW')
        ttk.ampinfo = Label(tab1, text="- %")
        ttk.ampinfo.grid(row=current_amplitude_row,column=2,sticky='EW')
        
        #Current amplitude setting leg 4
        ttk.leg4setAmplitudeLabel = Label(tab1, text="Current amplitude leg 4:").grid(row = current_leg4_amplitude_row, column=0,sticky='EW')
        ttk.leg4ampinfo = Label(tab1, text="- %")
        ttk.leg4ampinfo.grid(row=current_leg4_amplitude_row, column=2,sticky='EW')

        #Current phase Leg 1
        ttk.phase1 = Label(tab1, text="Current phase shift leg 1:").grid(row=current_phase1_row,column=0,pady=(25,0),sticky='EW')
        ttk.phase1info = Label(tab1, text="- °")
        ttk.phase1info.grid(row=current_phase1_row,column=2,pady=(25,0),sticky='EW')
        
        #Current Phase Leg 2
        ttk.phase2 = Label(tab1, text="Current phase shift leg 2:").grid(row=current_phase2_row,column=0,sticky='EW')
        ttk.phase2info = Label(tab1, text="- °")
        ttk.phase2info.grid(row=current_phase2_row,column=2,sticky='EW')
        
        #Current Phase Leg 3
        ttk.phase3 = Label(tab1, text="Current phase shift leg 3:").grid(row=current_phase3_row,column=0,sticky='EW')
        ttk.phase3info = Label(tab1, text="- °")
        ttk.phase3info.grid(row=current_phase3_row,column=2,sticky='EW')
        
        #Current Phase Leg 4
        ttk.phase4 = Label(tab1, text="Current phase shift leg 4:").grid(row=current_phase4_row,column=0,sticky='EW')
        ttk.phase4info = Label(tab1, text="- °")
        ttk.phase4info.grid(row=current_phase4_row,column=2,sticky='EW')



        #--Tab 2 Layout--
        frame = []
        for i in range(6):
            frame.append(Frame(tab2))
            frame[i].pack()

        ttk.titleLabel = Label(frame[0], text="Leg 1 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab2setfrequencyLabel = Label(frame[1], text="current Frequency:").pack(side=LEFT)
        ttk.tab2currentfrequencyLabel = Label(frame[1], text="- Hz")
        ttk.tab2currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab2setPWMfrequencyLabel = Label(frame[2], text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab2currentPWMfrequencyLabel = Label(frame[2], text="- Hz")
        ttk.tab2currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab2setAmplitudeLabel = Label(frame[3], text="Current amplitude:").pack(side=LEFT)
        ttk.tab2ampinfo = Label(frame[3], text="- %")
        ttk.tab2ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab2phase1 = Label(frame[4], text="Current phase shift:").pack(side=LEFT)
        ttk.tab2phase1info = Label(frame[4], text="- °")
        ttk.tab2phase1info.pack(side=LEFT)


        #Tab 3 Layout
        frame = []
        for i in range(6):
            frame.append(Frame(tab3))
            frame[i].pack(
                    )
        ttk.titleLabel = Label(frame[0], text="Leg 2 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab3setfrequencyLabel = Label(frame[1], text="Current Frequency:").pack(side=LEFT)
        ttk.tab3currentfrequencyLabel = Label(frame[1], text="- Hz")
        ttk.tab3currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab3setPWMfrequencyLabel = Label(frame[2], text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab3currentPWMfrequencyLabel = Label(frame[2], text="- Hz")
        ttk.tab3currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab3setAmplitudeLabel = Label(frame[3], text="Current amplitude:").pack(side=LEFT)
        ttk.tab3ampinfo = Label(frame[3], text="- %")
        ttk.tab3ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab3phase2 = Label(frame[4], text="Current phase shift:").pack(side=LEFT)
        ttk.tab3phase2info = Label(frame[4], text="- °")
        ttk.tab3phase2info.pack(side=LEFT)


        #Tab 4 Layout
        frame = []
        for i in range(6):
            frame.append(Frame(tab4))
            frame[i].pack()

        ttk.titleLabel = Label(frame[0], text="Leg 3 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab4setfrequencyLabel = Label(frame[1], text="Current Frequency:").pack(side=LEFT)
        ttk.tab4currentfrequencyLabel = Label(frame[1], text="- Hz")
        ttk.tab4currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab4setPWMfrequencyLabel = Label(frame[2], text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab4currentPWMfrequencyLabel = Label(frame[2], text="- Hz")
        ttk.tab4currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab4setAmplitudeLabel = Label(frame[3], text="Current amplitude:").pack(side=LEFT)
        ttk.tab4ampinfo = Label(frame[3], text="- %")
        ttk.tab4ampinfo.pack(side=LEFT)
        #Current phase Leg 1
        ttk.tab4phase3 = Label(frame[4], text="Current phase shift:").pack(side=LEFT)
        ttk.tab4phase3info = Label(frame[4], text="- °")
        ttk.tab4phase3info.pack(side=LEFT)


        #Tab 5 Layout
        frame = []
        for i in range(6):
            frame.append(Frame(tab5))
            frame[i].pack()

        ttk.titleLabel = Label(frame[0], text="Leg 4 settings", font = "Helvetica 16 bold italic").pack()
        #Leg settings
        #Current frequency setting
        ttk.tab5setfrequencyLabel = Label(frame[1], text="Current Frequency:").pack(side=LEFT)
        ttk.tab5currentfrequencyLabel = Label(frame[1], text="- Hz")
        ttk.tab4currentfrequencyLabel.pack(side=LEFT)
        #Current PWM frequency setting
        ttk.tab5setPWMfrequencyLabel = Label(frame[2], text="Current PWM Frequency:").pack(side=LEFT)
        ttk.tab5currentPWMfrequencyLabel = Label(frame[2], text="- Hz")
        ttk.tab5currentPWMfrequencyLabel.pack(side=LEFT)
        #Current amplitude setting
        ttk.tab5setAmplitudetab2Label = Label(frame[3], text="Current amplitude:").pack(side=LEFT)
        ttk.tab5ampinfo = Label(frame[3], text="- %")
        ttk.tab5ampinfo.pack(side=LEFT)
        #show_current_data(tab5)
        #Current phase Leg 4
        ttk.tab5phase4 = Label(frame[4], text="Current phase shift:").pack(side=LEFT)
        ttk.tab5phase4info = Label(frame[4], text="- °")
        ttk.tab5phase4info.pack(side=LEFT)
    
    def updategeneral(self):
        error = "ERROR"
        message = "One or more incorrect inputs"
        
        prepare_command = command.command("prepare")
        print(prepare_command())
        #self.connection.send(prepare_command)

        try:
            newfrequency = float(ttk.FreqEntry.get())
            if( (newfrequency >= 0 and newfrequency <=80) or newfrequency == 400):
                ttk.currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
                ttk.tab2currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
                ttk.tab3currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
                ttk.tab4currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
                ttk.tab5currentfrequencyLabel.configure(text="{} Hz".format(newfrequency))
                
                newfrequency = int(newfrequency*100)
                freq_command = command.command("frequency", newfrequency)
                print(freq_command())
                #self.connection.send(freq_command)
                ttk.FreqEntry.delete(0,'end')
            else:
                raise
        except:
            messagebox.showerror(error,message)

        try:
            newPWMfrequency = float(ttk.PWMFreqEntry.get())
            if( newPWMfrequency >= 0 and newPWMfrequency <= 62500):
                ttk.currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
                ttk.tab2currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
                ttk.tab3currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
                ttk.tab4currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
                ttk.tab5currentPWMfrequencyLabel.configure(text="{} Hz".format(newPWMfrequency))
                
                newPWMfrequency = int(newPWMfrequency)
                keyfreq_command = command.command("keyfrequency", newPWMfrequency)
                print(keyfreq_command())
                #self.connection.send(keyfreq_command)
                ttk.PWMFreqEntry.delete(0,'end')
            else:
                raise
        except:
            messagebox.showerror(error,message)
        
        try:
            newamplitude = int(ttk.AmpEntry.get())
            if( newamplitude >= 0 and newamplitude <= 100):
                ttk.ampinfo.configure(text="{} %".format(newamplitude))
                ttk.tab2ampinfo.configure(text="{} %".format(newamplitude))
                ttk.tab3ampinfo.configure(text="{} %".format(newamplitude))
                ttk.tab4ampinfo.configure(text="{} %".format(newamplitude))

                amplitude_command_leg1 = command.command("amplitude", newamplitude,0)
                amplitude_command_leg2 = command.command("amplitude", newamplitude,1)
                amplitude_command_leg3 = command.command("amplitude", newamplitude,2)
                print(amplitude_command_leg1())
                print(amplitude_command_leg2())
                print(amplitude_command_leg3())
                #self.connection.send(amplitude_command_leg1)
                #self.connection.send(amplitude_command_leg2)
                #self.connection.send(amplitude_command_leg3)
                ttk.AmpEntry.delete(0,'end')
            else:
                raise
        except:
            messagebox.showerror(error,message)

        try:
            newamplitudeleg4 = int(ttk.leg4AmpEntry.get())
            if( newamplitudeleg4 >= 0 and newamplitudeleg4 <= 100):
                ttk.leg4ampinfo.configure(text="{} %".format(newamplitudeleg4))
                ttk.tab5ampinfo.configure(text="{} %".format(newamplitudeleg4))
                amplitude_command_leg4 = command.command("amplitude", newamplitudeleg4,3)
                print(amplitude_command_leg4())
                #self.connection.send(amplitude_command_leg4)
                ttk.leg4AmpEntry.delete(0,'end')
            else:
                raise
        except:
            messagebox.showerror(error,message)


        if (ttk.var1.get()):
            try:
                newphase1 = int(ttk.phase1Entry.get())
                newphase1 = newphase1%360
                if (newphase1 >= 0 and newphase1 <= 360):
                    ttk.phase1info.configure(text="{}°".format(newphase1))
                    ttk.tab2phase1info.configure(text="{}°".format(newphase1))
                    phase1_command = command.command("phaseshift",newphase1,0)
                    print(phase1_command())
                    #self.connection.send(phase1_command)
                    ttk.phase1Entry.delete(0,'end')
                else:
                    raise
            except:
                messagebox.showerror(error,message)


        newphase2 = int(ttk.phase2Entry.get())
        ttk.phase2info.configure(text="{}°".format(newphase2))
        ttk.tab3phase2info.configure(text="{}°".format(newphase2))

        newphase3 = int(ttk.phase3Entry.get())
        ttk.phase3info.configure(text="{}°".format(newphase3))
        ttk.tab4phase3info.configure(text="{}°".format(newphase3))

        newphase4 = int(ttk.phase4Entry.get())
        ttk.phase4info.configure(text="{}°".format(newphase4))
        ttk.tab5phase4info.configure(text="{}°".format(newphase4))

        ttk.phase2Entry.delete(0,'end')
        ttk.phase3Entry.delete(0,'end')
        ttk.phase4Entry.delete(0,'end')

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
        if((ttk.var1.get()) or ttk.var2.get() or ttk.var3.get() or ttk.var4.get()):  
            ttk.start_button.configure(bg = 'green')
            ttk.FreqEntry['state'] = NORMAL
            ttk.PWMFreqEntry['state'] = NORMAL
            ttk.AmpEntry['state'] = NORMAL
            ttk.leg4AmpEntry['state'] = NORMAL

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
        
        #Enable buttons
        ttk.EnableLeg1['state'] = NORMAL
        ttk.EnableLeg2['state'] = NORMAL
        ttk.EnableLeg3['state'] = NORMAL
        ttk.EnableLeg4['state'] = NORMAL

        ttk.FreqEntry.delete(0,'end')
        ttk.FreqEntry['state'] = DISABLED
        ttk.currentfrequencyLabel.configure(text="- Hz")
        ttk.tab2currentfrequencyLabel.configure(text="- Hz")
        ttk.tab3currentfrequencyLabel.configure(text="- Hz")
        ttk.tab4currentfrequencyLabel.configure(text="- Hz")
        ttk.tab5currentfrequencyLabel.configure(text="- Hz")
        ttk.currentPWMfrequencyLabel.configure(text="- Hz")

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
        
        ttk.leg4AmpEntry['state'] = DISABLED
        ttk.leg4ampinfo.configure(text="- %")

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

