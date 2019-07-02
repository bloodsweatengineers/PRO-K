# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


import serial
import re
import command
import serial.tools.list_ports
from tkinter import messagebox

##  @package uart_communication
#   This module sets up the serial communication between the PC and the microcontroller. It also sends data over the serial connection.

class connection:
    ##  The destructor destroys objects if they are not being used anymore.
    def __del__(self):
        return 0
    ##  The constructors checks if there is a arduino present and connects to it if it is. If there is no Arduino present it displays a error message.
    def __init__(self):
        try:
            FTDI = re.compile("USB Serial Port")
            FTDI_linux = re.compile("FT232R USB UART")
            Arduino = re.compile("Arduino Uno")
            for i in serial.tools.list_ports.comports(True):
                if(FTDI.match(i.description)):
                    A=i.device
                if(FTDI_linux.match(i.description)):
                    A=i.device
                if(Arduino.match(i.description)):
                    A=i.device
            self.ser = serial.Serial(A,9600, timeout = 0.5)
            self.var = True
        except:
            messagebox.showerror("ERROR","Please connect a microcontroller and press Start!")
            self.var = False
    ##  The call method returns a boolean which represents if the microcontrolller is connected.
    def __call__(self):
        return self.var
    ##  The send method sends a binary formatted command over serial communication to the microcontroller.
    def send(self, command):
        message = bytearray(command())
        self.ser.write(message)
        a = self.ser.readline()
