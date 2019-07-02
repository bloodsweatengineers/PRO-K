import csv
import sys
import serial
import time
import crc8
import serial.tools.list_ports
import re

string = list()
command = list()

with open("Gen/token.csv", "r") as File:
    reader = csv.DictReader(File)
    for row in reader:
        string.append(row['string'])
        command.append(row['binary'])

def read_REPL():

    while True:
        print(ser.readline())

def string_REPL():
    start = "%"
    end = "\r\n"
    while True:
        In = input("Command: ")
        In = In.split(" ")
    
        command = In[0]

        if command == "exit":
            break

        value = ""
        if len(In) > 1:
            value = " " + In[1]

        message = start + command + value + end
        print("Running command: {}".format(message.encode('ascii')))
        ser.write(message.encode('ascii'))
        print(ser.readline())

def binary_REPL():
    base = 0x24

    while True:
        send = list()
        send.append(base) 
        com_str = input("command: ")
    
        if com_str == "exit":
            break

        chan = input("channel(optional): ")
        val = input("value(optional): ")

        try:
            index = string.index(com_str)
            com = int(command[index], 0)
        except:
            print("command not found");
            continue

        if chan:
            com += int(chan)

        send.append(com)

        if not val:
            send.extend([0xFF,0xFF,0xFF])
        else:
            val = int(val)
            result = list()
            for i in range(0,3):
                result.append(val % 256)
                val = int(val/256)
            result.reverse()
            send.extend(result)

        hash = crc8.crc8()
        hash.update(bytearray(send))
        send.append(int.from_bytes(hash.digest(), 'little'))

        print("Running command: {}".format(bytearray(send)))
        ser.write(bytearray(send))
        print(ser.readline())

def print_help():
    print("Options --")
    print("\tbinary - Send binary commands to firmware")
    print("\tstring - Send terminal commands to firmware")
    print("\thelp - print this message")

connected = False
device = None
FTDI = re.compile("USB Serial Port")
FTDI_linux = re.compile("FT232R USB UART")
Arduino = re.compile("Arduino Uno")
while connected == False:
        a = serial.tools.list_ports.comports(True)
        for i in a:
            if(FTDI.match(i.description)):
                connected = True
                device = i.device
                continue
            if(FTDI_linux.match(i.description)):
                connected = True
                device = i.device
                continue
            if(Arduino.match(i.description)):
                connected = True
                device = i.device
                continue

        if connected == False:
            print("Please connect arduino and press enter")
            In = input("")

ser = serial.Serial(device, 9600, timeout=0.5)

if not ser.is_open:
    print("Error failed to open serial device")

while True:
    Choose = input("Choose option: ")
    if Choose.lower() == "binary":
        binary_REPL()
    elif Choose.lower() == "string":
        string_REPL()
    elif Choose.lower() == "read":
        read_REPL()
    elif Choose.lower() == "help":
        print_help()
    elif Choose.lower() == "exit":
        break
