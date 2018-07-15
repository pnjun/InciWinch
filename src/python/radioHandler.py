import serial
import json
import binascii
from datetime import datetime
from types import SimpleNamespace
from xbee import ZigBee

from threading import Thread, Event

BAUD_RATE = 9600

class Timer(Thread):
    ''' Runs <callback> every <interval> seconds until event is triggered.
        Used to generate fake data for testing '''
    def __init__(self, stopEvent, callback, interval):
        Thread.__init__(self)
        self.callback = callback
        self.interval = interval
        self.stopEvent = stopEvent

    def run(self):
        while not self.stopEvent.wait(self.interval):
            self.callback()


class RadioHandler:
    ''' This class is responsible for reading data from a xBee conneced via serial port,
        formatting the data in a python object and calling a GUI callback with the
        formatted data. If fakeData is True, serialPort is ignored and fake data is
        generated '''

    def __init__(self, serialPort, callback, fakeData = False):
        self.callback = callback
        self.fake = fakeData

        if self.fake:
            self.interval = 0.5 #Adjust theese numbers to change fake data generation
            self.speed = 20
            self.height = 0

            self.stopFlag = Event()
            fakeThread = Timer(self.stopFlag, self._fakeCallback, self.interval)
            fakeThread.start()
        else:
            self.port = serial.Serial(serialPort, BAUD_RATE)
            self.xbee = ZigBee(self.port, callback=self._recvCallback)

    def _fakeCallback(self):
        ''' Generates fake data and sends them to GUI, called from timer thread '''
        data = {}
        data['source'] = '--FAKE----TEST--'
        data['time'] = datetime.now()
        data['IAS'] = self.speed
        data['height'] = self.height
        self.speed += 2
        self.height += 10
        # Turns a dictionary into a namespace
        self.callback(SimpleNamespace(**data))

    def _recvCallback(self, rawData):
        ''' Reads data from xBee, formats the data and calls GUI '''
        try:
            source = rawData['source_addr_long']
            payload = json.loads( rawData['rf_data'].decode('ascii') )

            # This is here to explicitly decouple JSON naming convention
            # from python internal variable names
            data = {}
            data['source'] = binascii.hexlify( source ).decode('ascii').upper()
            data['time'] = datetime.now()
            data['IAS'] = payload.pop('IAS')
            data['height'] = payload.pop('HEI')
        except Exception as e:
            print("Could not parse frame:")
            print(e)

        # Turns a dictionary into a namespace
        self.callback(SimpleNamespace(**data))

    def halt(self):
        if self.fake:
            self.stopFlag.set()
        else:
            self.xbee.halt()
            self.port.close()
