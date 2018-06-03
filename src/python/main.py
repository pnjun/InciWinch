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
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.theming import ThemeManager
from kivymd.tabs import MDTab

import matplotlib.pyplot as plt

GRAPH_MAXT = 60
GRAPH_MAXSPEED = 150
GRAPH_MAXHEIGHT = 600

class Launch(MDTab):
    pass

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
            self.radio = RadioHandler("/dev/tty.usbserial-DN03FTBY", self.radioCallback, fakeData=False)
        except SerialException:
            self.radio = None

        #Radio frames processing is scheduled to run at every GUI loop cycle
        #Increase kivy maxfps if needed (default is 60Hz)
        Clock.schedule_interval(self.processFrames, 0)

    def on_stop(self):
        self.radio.halt()

    def updateLaunch(self,launch, frame):
        # save new frame data
        launch.frames.append(frame)

        # update graph
        startTime = launch.frames[0].time
        times = [(f.time - startTime).total_seconds() for f in launch.frames]
        speeds = [f.IAS for f in launch.frames]
        heights = [f.height for f in launch.frames]

        print((frame.time - startTime).total_seconds(), frame.IAS, frame.height)

        launch.speedLine.set_xdata(times)
        launch.speedLine.set_ydata(speeds)
        launch.heightLine.set_xdata(times)
        launch.heightLine.set_ydata(heights)
        launch.speedAx.set_xlim(times[-1] - GRAPH_MAXT, times[-1])



        launch.figure.canvas.draw()

        # update info
        launch.ids.launchTitle.text    = frame.source
        launch.ids.TimeDisplay.text    = str(frame.time)
        launch.ids.IASDisplay.text     = "IAS = " + str(frame.IAS)
        launch.ids.HeightDisplay.text  = "HEIGHT = " + str(frame.height)

    def newLaunch(self, sourceID):
        launch = Launch()

        # Setup launch identifiers
        launch.name = sourceID
        launch.text = sourceID[8:] #use address low as tab title

        # Array where all launch data frames will be stored.
        launch.frames = []

        # Set up canvas for graph. Figure, Axes and datalines are stored in launch object
        # All plotting paramters are here
        launch.figure = plt.figure()

        launch.speedAx = launch.figure.add_subplot(111)
        launch.speedAx.set_ylim(0, GRAPH_MAXSPEED)
        launch.speedAx.set_xlabel('time [s]')
        launch.speedAx.set_ylabel('speed [km/h]', color='tab:blue' ,size='large')
        launch.speedAx.tick_params('y', colors='tab:blue', labelsize='large')
        launch.speedLine, = launch.speedAx.plot([],[], 'tab:blue', linewidth=4)

        launch.heightAx = launch.speedAx.twinx()
        launch.heightAx.set_ylim(0, GRAPH_MAXHEIGHT)
        launch.heightAx.set_ylabel('height [m]', color='tab:orange', size='large')
        launch.heightAx.tick_params('y', colors='tab:orange', labelsize='large')
        launch.heightLine, = launch.heightAx.plot([],[], 'tab:orange', linewidth=4)

        launch.ids.GraphDisplay.add_widget(FigureCanvasKivyAgg(launch.figure))

        # Add the widget and update data
        self.root.ids.launchList.add_widget(launch)
        return launch

    #This function is called from the xBee thread, do not call from GUI thread
    def radioCallback(self, data):
        self.radioFrames.put(data)

    def processFrames(self, dt):
        # This loop might freeze the UI if frames arrive faster
        # than they can be processed. This could be solved by adding a
        # max number of frames to processed per cicle, but that would not
        # solve the problem of frames not beeing processed as soon as they arrrive.
        # I want the app to crash if its overwhelmed, so that someone notices
        # the problem instead of failing silently
        while not self.radioFrames.empty():
            frame = self.radioFrames.get(block=False)

            tablist = self.root.ids.launchList.ids.tab_manager.screens

            #Search if there is already a matching launch, if not create one
            for launch in tablist:
                if launch.name == frame.source:
                    self.updateLaunch(launch, frame)
                    break
            else:
                newLaunch = self.newLaunch(frame.source)
                self.updateLaunch(newLaunch, frame)

if __name__ == '__main__':
    InciWinchApp().run()
