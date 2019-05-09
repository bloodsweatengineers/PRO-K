# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter

import command
import uart_connection

class GUI:
    def __init__(self,master):
        self.master = master
        self.master.title("PWM Controller")
        
        #Create Tab Control  
        tabControl=ttk.Notebook(self.master)  
        #Tab1  
        tab1=ttk.Frame(tabControl)  
        tabControl.add(tab1, text='Tab 1')  
        #Tab2  
        tab2=ttk.Frame(tabControl)  
        tabControl.add(tab2, text='Tab 2')  
        tabControl.pack(expand=1, fill="both")  
        #Tab Name Labels  
        ttk.Label(tab1, text="This is Tab 1").grid(column=0,row=0,padx=10,pady=10)  
        ttk.Label(tab2, text="This is Tab 2").grid(column=0,row=0,padx=10,pady=10)  
        #Calling Main()  
        #labels

        self.FreqLabel = Label(tab1, text="Frequency:").grid(row=3, column=0)
        #self.Amp1Label = Label(self.master, text="Amplitude channel 1:").grid(row=4, column=0)
        #self.Amp2Label = Label(self.master, text="Amplitude channel 2:").grid(row=5, column=0)
        #self.Amp3Label = Label(self.master, text="Amplitude channel 3:").grid(row=6, column=0)
        #self.Amp4Label = Label(self.master, text="Amplitude channel 4:").grid(row=7, column=0)
        #self.Phase1Label = Label(self.master, text="Phase channel 1:").grid(row=8, column=0)
        #self.Phase2Label = Label(self.master, text="Phase channel 2:").grid(row=9, column=0)
        #self.Phase3Label = Label(self.master, text="Phase channel 3:").grid(row=10, column=0)
        #self.Phase4Label = Label(self.master, text="Phase channel 4:").grid(row=11, column=0)
        #self.pwmfreqLabel = Label(self.master, text="PWM Frequency:").grid(row=12, column=0)

root = Tk()
this_gui = GUI(root)
while True:
    root.update_idletasks()
    root.update()

