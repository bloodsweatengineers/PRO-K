import sys
import serial
import time 

start = "%"
end = "\r\n"

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

if not ser.is_open:
    print("Error failed to open serial device")

while True:
    In = input("Command: ")
    In = In.split(" ")
    
    command = In[0]
    value = ""
    if len(In) > 0:
        value = " " + In[1]

    message = start + command + value + end
    print("Running command: {}".format(message.encode('ascii')))
    ser.write(message.encode('ascii'))
    print(ser.readline())
