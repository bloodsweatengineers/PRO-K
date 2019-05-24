# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

# syntax sender
# start : 0x 24 ($)
# end   : CRC (1 byte)
# syntax: <start><command><value><end>
# Value : 3 Byte integer

# Commandlist sender
# Info          : 0x 24 00 FF FF FF (CRC)
# Ping          : 0x 24 FF FF FF FF (CRC)
# Frequency     : 0x 24 01 XX XX XX (CRC) - [With XX XX XX being the frequency in mHz]
# Amplitude     : 0x 24 1X 00 00 YY (CRC) - [With X being the channel and YY being the value]
# KeyFrequency  : 0x 24 2X 00 YY YY (CRC) - [With X being the channel and YY YY being the value]
# PhaseShift    : 0x 24 3X 00 YY YY (CRC) - [With X being the channel and YY YY being the value]
# Prepare       : 0x 24 02 FF FF FF (CRC)
# Execute       : 0x 24 03 FF FF FF (CRC)
# Start         : 0x 24 04 FF FF FF (CRC)
# Stop          : 0x 24 05 FF FF FF (CRC)
# Gather        : 0x 24 4X 00 00 YY (CRC) - With X being the channel and YY being the amount of samples

# Syntax receiver
# syntax    : <ux_command><type><length_response><response><CRC>
# type      : info <00>; Ping <FF>; Gather <40>; OK <01>; REJ <02>
# Example receiver
# 0x 24 01 00 00 00 (CRC) 01 00 00 (CRC) - [Frequency OK]
# 0x 24 41 00 00 FF (CRC ) 40 02 00

# .csv schrijven toevoegen

from tkinter import Label, Entry, Button, Tk

import serial

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PWM Controller")

        
        #labels
        self.FreqLabel = Label(self.master, text="Frequency:").grid(row=0, column=0)
        self.AmpLabel = Label(self.master, text="Amplitude:").grid(row=1, column=0)
        self.Phase1Label = Label(self.master, text="Phase 1:").grid(row=2, column=0)
        self.Phase2Label = Label(self.master, text="Phase 2:").grid(row=3, column=0)
        self.pwmfreqLabel = Label(self.master, text="PWM Frequency:").grid(row=4, column=0)
        self.maxpowerLabel = Label(self.master, text="Maximum Power:").grid(row=5,column=0)

#        self.currentleg1 = Label(self.master).grid(row=5, column=0)

        #Entries
        self.FreqEntry = Entry(self.master, bd=5)
        self.AmpEntry = Entry(self.master, bd=5)
        self.Phase1Entry = Entry(self.master, bd=5)
        self.Phase2Entry = Entry(self.master, bd=5)
        self.PWMFreqEntry = Entry(self.master, bd=5)
        self.maxpowerEntry = Entry(self.master, bd=5)

        #Buttons
        FreqButton = Button(self.master, text="Update", command = self.FreqUpdate).grid(row=0, column=2)
        AmpButton = Button(self.master, text="Update", command = self.AmpUpdate).grid(row=1, column=2)
        Phase1Button = Button(self.master, text="Update", command = self.Phase1Update).grid(row=2, column=2)
        Phase2Button = Button(self.master, text="Update", command = self.Phase2Update).grid(row=3, column=2)
        pwmfreqButton = Button(self.master, text="Update").grid(row=4, column=2)
        maxpowerButton = Button(self.master, text= "Update").grid(row=5, column=2)

        #Location
        self.FreqEntry.grid(row=0, column=1)
        self.AmpEntry.grid(row=1, column=1)
        self.Phase1Entry.grid(row=2, column=1)
        self.Phase2Entry.grid(row=3, column=1)
        self.PWMFreqEntry.grid(row=4, column=1)
        self.maxpowerEntry.grid(row=5, column=1)

    def FreqUpdate(self):
        A = self.FreqEntry.get()
        try:
            P = float(A)
       #     print(type(P))
            if( P >= 0 and P <= 80):
                C = int(P)
                B = C*5
      #          print(B)
      #          print(type(B))

                freqstring = command_string.format(36,01,00,00,00)
                print(freqstring)
                encodedfreqstring = freqstring.encode()
                print(encodedfreqstring)
 #               ser.write(encodedfreqstring)
            else:
                raise
        except:
            print("ERROR")

    def AmpUpdate(self):
        amplitude = self.AmpEntry.get()
        try:
            if( float(amplitude) >= 0 and float(amplitude) <= 1):

                print("Amplitude is equal to: ", amplitude)
                
                ampstring = command_string.format("s", "a", amplitude)
                encodedampstring = ampstring.encode()
                print(encodedampstring)
#                ser.write(encodedampstring)
            else:
                raise
        except:
            print("ERROR")

    def Phase1Update(self):
        try:
            phase1 = int(self.Phase1Entry.get())
            phase1 = phase1%360
            phase1 = int((256/360)*phase1)
            if phase1 >= 0 and phase1 <=360:
                phase1 = bin(phase1)
                print("Phase 1 is equal to", phase1)
                
                phase1string = command_string.format("s", "p1", phase1)
                encodedphase1string = phase1string.encode()
                print(encodedphase1string)
#                ser.write(encodedphase1string)
            else:
                raise
        except:
            print("ERROR")

    def Phase2Update(self):
        try:
            phase2 = int(self.Phase2Entry.get())
            phase2 = phase2%360
            phase2 = int((256/360)*phase2)
            if phase2 >= 0 and phase2 <=360:
                phase2 = bin(phase2)
                print("Phase 2 is equal to", phase2)
                
                phase2string = command_string.format("s", "p2", phase2)
                encodedphase2string = phase2string.encode()
                print(encodedphase2string)
#                ser.write(encodedphase2string)

            else:
                raise
        except:
            print("ERROR")

    def pwmFreqUpdate(self):
        PWMFreq = self.PWMFreqEntry.get()
        try:
            if( float(PWMFreq) >= 0 and float(PWMFreq) <= 80):
                PWMFreqA = int(PWMFreq)
                PWMFreqB = PWMFreqA*5
                PWMFreqstring = command_string.format("s", "f", PWMFreqB)
                encodedPWMFreqstring = PWMFreqstring.encode()
                print(encodedPWMFreqstring)
#                ser.write(encodedPWMFreqstring)
            else:
                raise
        except:
            print("ERROR")



root = Tk()
this_gui = GUI(root)

while True:
    root.update_idletasks()
    root.update()

