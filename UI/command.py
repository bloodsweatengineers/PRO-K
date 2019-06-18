# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

##  @package command
#   This module is responsible to encode commands, which are being created in different parts in the user interface code into the right format.

import crc8

##  The command class encodes binary commands into the correct format according to the syntax of the communication protocol.
#
class command:
    ##  command_type is a dictionary with the binary representation of the command, including if it is channel dependent or not.
    command_type = {'frequency'     : [0x01,0],
                    'amplitude'     : [0x10,1],
                    'keyfrequency'  : [0x20,0],
                    'phaseshift'    : [0x30,1],
                    'info'          : [0x00,0],
                    'ping'          : [0xFF,0],
                    'prepare'       : [0x02,0],
                    'execute'       : [0x03,0],
                    'start'         : [0x04,0],
                    'gather'        : [0x40,1],
                    'stop'          : [0x05,0],
                    'VFD'           : [0x06,0],
                    'enable'        : [0x50,1]
                    }

    ##  The constructor can take three arguments. Com being the command, value being the value which is set to 0 if there is no value and channel being the channel, which is set to 0 if there is no channel.
    def __init__(self, com, value=0, channel=0):
        self.value = int(value)
        self.type = command.command_type[com]
        self.command = self.type[0]
        if self.type[1]:
            self.command += channel

    ##  The call method creates the message with the startbyte being $ and the binary representation of the command, value and the CRC checksum.
    def __call__(self):
        packet = list()
        packet.append(ord("$"))
        packet.append(self.command)
        packet.extend(self.calc_value())
        packet.append(self.crc(packet))
        return packet

    ##  The calc_value method creates a representation of the value in bytes.
    def calc_value(self):
        value = self.value
        result = list()
        if value == None:
            return [0xFF,0xFF,0xFF]
        for i in range(0,3):
            result.append(value % 256)
            value = int(value/256)
        result.reverse()
        return result
    ##  The CRC method calculates the CRC checksum
    def crc(self,message):
        hash = crc8.crc8()
        hash.update(bytearray(message))
        return int.from_bytes(hash.digest(),'little')
