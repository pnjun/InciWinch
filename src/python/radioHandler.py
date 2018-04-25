import serial
import time
import json
from collections import namedtuple
from tornado import ioloop, gen
from xbee import ZigBee

BAUD_RATE = 9600

class RadioHandler:
    def __init__(self, serialPort, callback):
        self.port = serial.Serial(serialPort, BAUD_RATE)
        xb = ZigBee(self.port, callback=self._recvCallback)
        self.callback = callback

    def _recvCallback(self, rawData):
        data = json.loads(rawData, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.callback(data)
