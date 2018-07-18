import binascii
import struct
import time

class Paras(object):
    def __init__(self):

        self.Paras_init()

    def Paras_init(self):
        self.ceffinal = 0
        self.Speed = 0
        self.localtime = "xxxx"
        self.injecting = False
        self.autoControl = False
        self.manControl = False

    def SpeedCommand(self, speed):
        self.speedcommond = binascii.b2a_hex(struct.pack('h', int(speed * 10))).decode('ascii').upper()
        self.check_speed1 = "0x" + str(self.speedcommond)[0:2]
        self.check_speed2 = "0x" + str(self.speedcommond)[2:4]
        self.check_sum = (str(hex((int(self.check_speed1, 16) + int(self.check_speed2, 16) + 497)^65535))[-2::]).upper()
        self.speedcommond = '55AA0504011608C8000001' + str(self.speedcommond) + "0001" + self.check_sum
        return self.speedcommond






