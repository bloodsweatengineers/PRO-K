import csv
import sys
import serial
import time 

def string_REPL():
    start = "%"
    end = "\r\n"
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

def binary_REPL():

    while True:
    
        In = input("Input command(6 bytes): ")
        In = In.split(" ")

        if len(In) != 6:
            print("Wrong number of arguments")
            continue

        command = list()
        for i in In:
            command.append(int(i, 0))

        send = bytearray(command)
        print("Running command : {}".format(send))
        ser.write(send)
        print(ser.readline())

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

if not ser.is_open:
    print("Error failed to open serial device")

Choose = input("Choose command type: ")
if Choose.lower() == "binary":
    binary_REPL()
elif Choose.lower() == "string":
    string_REPL()
