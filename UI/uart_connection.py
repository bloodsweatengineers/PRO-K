import serial
import command

class connection:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=.5)
    
    def send(self, command):
        message = bytearray(command())
        print(message)
        self.ser.write(message)
        a = self.ser.read_until("\r\n")
        print(a)
    def receive(self, message):
        return 0
