# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


import serial
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
            for i in serial.tools.list_ports.comports(True):
                if(i.product == "Arduino Uno"):
                    A=i.device
            self.ser = serial.Serial(A,9600, timeout = 0.5)
            self.var = True
        except:
            messagebox.showerror("ERROR","Please connect a microcontroller and press refresh!")
            self.var = False
    ##  The call method returns a boolean which represents if the microcontrolller is connected.
    def __call__(self):
        return self.var
    ##  The send method sends a binary formatted command over serial communication to the microcontroller.
    def send(self, command):
        message = bytearray(command())
        print(message)
        self.ser.write(message)
        a = self.ser.readline()
        print(a)
