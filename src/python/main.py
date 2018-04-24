from gui import InciWinchApp
from radioHandler import RadioHandler

def main():
    radio = RadioHandler("/dev/tty.usbserial-DN03FTBY")
    #InciWinchApp().run()

if __name__ == '__main__':
    main()
