import csv
import sys
import serial
import time
import crc8

string = list()
command = list()

with open("Gen/token.csv", "r") as File:
    reader = csv.DictReader(File)
    for row in reader:
        string.append(row['string'])
        command.append(row['binary'])

print(string)
print(command)


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
        value = ""
        if len(In) > 0:
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
        chan = input("channel(optional): ")
        val = input("value(optional): ")

        index = string.index(com_str)
        com = int(command[index], 0)

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

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

if not ser.is_open:
    print("Error failed to open serial device")

Choose = input("Choose command type: ")
if Choose.lower() == "binary":
    binary_REPL()
elif Choose.lower() == "string":
    string_REPL()
elif Choose.lower() == "read":
    read_REPL()
