import serial
import command
import serial.tools.list_ports
from tkinter import messagebox

class connection:
    def __init__(self):
        try:
            for i in serial.tools.list_ports.comports(True):
                if(i.product == "Arduino Uno"):
                    A=i.device
            self.ser = serial.Serial(A, 9600, timeout=.5)
        except:
            messagebox.showerror('ERROR','Please connect a microcontroller and press the refresh button')

    def send(self, command):
        message = bytearray(command())
        print(message)
        self.ser.write(message)
        a = self.ser.readline()
        print(a)
    def receive(self, message):
        return 0
