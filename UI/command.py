# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

import crc8

class command:
    command_type = {'frequency'     : [0x01,0],
                    'amplitude'     : [0x10,0],
                    'keyfrequency'  : [0x20,0],
                    'phaseshift'    : [0x30,1],
                    'info'          : [0x00,0],
                    'ping'          : [0xFF,0],
                    'prepare'       : [0x02,0],
                    'execute'       : [0x03,0],
                    'start'         : [0x04,0],
                    'gather'        : [0x40,1],
                    'stop'          : [0x05,0]
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
            return [0xFF,0xFF,0xFF]
        for i in range(0,3):
            result.append(value % 256)
            value = int(value/256)
        result.reverse()
        return result

    def crc(self,message):
        hash = crc8.crc8()
        hash.update(bytearray(message))
        return int.from_bytes(hash.digest(),'little')
