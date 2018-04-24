import serial
import time
from tornado import ioloop, gen
from xbee import ZigBee

BAUD_RATE = 9600

class RadioHandler:
    def __init__(self, serialPort):
        self.port = serial.Serial(serialPort, BAUD_RATE)
        xb = ZigBee(self.port, callback=self._recvCallback)

    def _recvCallback(self, data):
        print('af')
        print(data)
