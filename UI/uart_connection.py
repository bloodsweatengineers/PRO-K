import serial
import command
import serial.tools.list_ports

class connection:
    def __init__(self):
        for i in serial.tools.list_ports.comports(True):
            if(i.product == "Arduino Uno"):
                A=i.device
        self.ser = serial.Serial(A, 9600, timeout=.5)
    
    def send(self, command):
        message = bytearray(command())
        print(message)
        self.ser.write(message)
        a = self.ser.readline()
        print(a)
    def receive(self, message):
        return 0
