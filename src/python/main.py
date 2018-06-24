# -*- coding: utf-8 -*-
#General Imports
from radioHandler import RadioHandler
from serial.serialutil import SerialException
from queue import Queue

#Kivy Imports
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.tabs import MDTab

from Launch import Launch

class InciWinchApp(App):
    theme_cls = ThemeManager()
    title = "InciWinch"

    #FIFO queue for frames received over the radio that must be processed.
    #The queue is filled by the radiomodule thread and emptied by the GUI thread
    radioFrames = Queue()

    def build(self):
        return Builder.load_file('gui.kv')

    def on_start(self):
        try:
            self.radio = RadioHandler("/dev/tty.usbserial-DN03FTBY", self.radioCallback, fakeData=True)
        except SerialException:
            self.radio = None

        #Radio frames processing is scheduled to run at every GUI loop cycle
        #Increase kivy maxfps if needed (default is 60Hz)
        Clock.schedule_interval(self.processFrames, 0)

    def on_stop(self):
        self.radio.halt()

    #This function is called from the xBee thread, do not call from GUI thread
    def radioCallback(self, data):
        self.radioFrames.put(data)


    # This loop might freeze the UI if frames arrive faster
    # than they can be processed. This could be solved by adding a
    # max number of frames to processed per cicle, but that would not
    # solve the problem of frames not beeing processed as soon as they arrrive.
    # I want the app to crash if its overwhelmed, so that someone notices
    # the problem instead of failing silently
    def processFrames(self, dt):
        while not self.radioFrames.empty():
            frame = self.radioFrames.get(block=False)
            tablist = self.root.ids.launchList.ids.tab_manager.screens

            #Search if there is already a matching launch, if not create one
            for launch in tablist:
                if launch.name == frame.source:
                    launch.update(frame)
                    break
            else:
                newLaunch = Launch(frame)
                self.root.ids.launchList.add_widget(newLaunch)
                newLaunch.update(frame)

if __name__ == '__main__':
    InciWinchApp().run()
