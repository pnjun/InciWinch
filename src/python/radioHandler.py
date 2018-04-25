import serial
import json
import binascii
from datetime import datetime
from types import SimpleNamespace
from xbee import ZigBee

BAUD_RATE = 9600

class RadioHandler:
    def __init__(self, serialPort, callback):
        self.port = serial.Serial(serialPort, BAUD_RATE)
        self.xbee = ZigBee(self.port, callback=self._recvCallback)
        self.callback = callback

    def _recvCallback(self, rawData):
        source = rawData['source_addr_long']
        payload = json.loads( rawData['rf_data'].decode('ascii') )

        # This is here to explicitly decouple JSON naming convention
        # from python internal variable names
        data = {}
        data['source'] = binascii.hexlify( source ).decode('ascii').upper()
        data['time'] = datetime.now()
        data['IAS'] = payload.pop('IAS')
        data['height'] = payload.pop('HEI')

        # Turns a dictionary into a namespace
        self.callback(SimpleNamespace(**data))

    def halt(self):
        self.xbee.halt()
        self.port.close()
