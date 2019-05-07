# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

# syntax sender
# start : 0x 24 ($)
# end   : CRC (1 byte)
# syntax: <start><command><value><end>
# Value : 3 Byte integer

# Commandlist sender
# Info          : 0x 24 00 FF FF FF (CRC)
# Ping          : 0x 24 FF FF FF FF (CRC)
# Frequency     : 0x 24 01 XX XX XX (CRC) - [With XX XX XX being the frequency in mHz]
# Amplitude     : 0x 24 1X 00 00 YY (CRC) - [With X being the channel and YY being the value]
# KeyFrequency  : 0x 24 2X 00 YY YY (CRC) - [With X being the channel and YY YY being the value]
# PhaseShift    : 0x 24 3X 00 YY YY (CRC) - [With X being the channel and YY YY being the value]
# Prepare       : 0x 24 02 FF FF FF (CRC)
# Execute       : 0x 24 03 FF FF FF (CRC)
# Start         : 0x 24 04 FF FF FF (CRC)
# Stop          : 0x 24 05 FF FF FF (CRC)
# Gather        : 0x 24 4X 00 00 YY (CRC) - With X being the channel and YY being the amount of samples

# Syntax receiver
# syntax    : <ux_command><type><length_response><response><CRC>
# type      : info <00>; Ping <FF>; Gather <40>; OK <01>; REJ <02>
# Example receiver
# 0x 24 01 00 00 00 (CRC) 01 00 00 (CRC) - [Frequency OK]
# 0x 24 41 00 00 FF (CRC ) 40 02 00 (CRC
from tkinter import Label, Entry, Button, Tk

import serial
import crc8

#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=.5)

#todo: toevoegen commandovertalen en CRC check

class command:
    command_type = {'frequency'     : [0x01,0],
                    'amplitude'     : [0x10,1],
                    'keyfrequency'  : [0x20,0],
                    'phaseshift'    : [0x30,1],
                    'info'          : [0x00,0],
                    'ping'          : [0xFF,0],
                    'prepare'       : [0x02,0],
                    'execute'       : [0x03,0],
                    'start'         : [0x04,0],
                    'gather'        : [0x40,1]
                    }

    def __init__(self, com, value=0, channel=0):
        self.value = value
        self.type = command.command_type[com]
        self.command = self.type[0]
        if self.type[1]:
            self.command += channel


    def __call__(self):
        packet = list()
        packet.append(ord("$"))
        packet.append(self.command)
        packet.extend(self.calc_value())
        packet.append(self.crc(packet))
        return packet


    def calc_value(self):
        value = self.value
        result = list()
        if not value:
            return [0,0,0]
        for i in range(0,3):
            result.append(value % 256)
            value = int(value/256)
        result.reverse()
        return result

    def crc(self,message):
        hash = crc8.crc8()
        hash.update(bytearray(message))
        return int.from_bytes(hash.digest(),'little')

InfoA = command("frequency", 1000) 
print(InfoA())
