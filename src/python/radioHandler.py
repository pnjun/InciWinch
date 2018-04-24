import serial
import time
from xbee import ZigBee

PORT = "/dev/tty.usbserial-DN03FTBY" #change the port if you are not using Windows to whatever port you are using
BAUD_RATE = 9600
serial = serial.Serial(PORT, BAUD_RATE)

# Create API object
xb = ZigBee(serial)

# Continuously read and print packets
while True:
    try:
        response = xb.wait_read_frame()

        print("\nPacket received at %s : %s" %(time.time(), response))

    except KeyboardInterrupt:
        serial.close()
        break
