from kivymd.tabs import MDTab
from kivymd.snackbar import Snackbar
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib.pyplot as plt
import os
import json

#Plot paramters
GRAPH_MAXT = 60
GRAPH_MAXSPEED = 150
GRAPH_MAXHEIGHT = 600

SAVE_DIR = 'savedLaunches'

class Launch(MDTab):
    def __init__(self, firstFrame):
        super(Launch, self).__init__()

        # Setup launch identifiers
        self.name = firstFrame.source
        self.text = firstFrame.source[8:] #use address low as tab title

        # Arrays to store data from incoming frames
        self.startTime = firstFrame.time
        self.times = []
        self.heights = []
        self.speeds = []

        # Set up canvas for graph. Figure, Axes and datalines are stored in launch object
        # All plotting paramters are here
        self.figure = plt.figure()

        self.speedAx = self.figure.add_subplot(111)
        self.speedAx.set_ylim(0, GRAPH_MAXSPEED)
        self.speedAx.set_xlabel('time [s]')
        self.speedAx.set_ylabel('speed [km/h]', color='tab:blue' ,size='large')
        self.speedAx.tick_params('y', colors='tab:blue', labelsize='large')
        self.speedLine, = self.speedAx.plot([],[], 'tab:blue', linewidth=4)

        self.heightAx = self.speedAx.twinx()
        self.heightAx.set_ylim(0, GRAPH_MAXHEIGHT)
        self.heightAx.set_ylabel('height [m]', color='tab:orange', size='large')
        self.heightAx.tick_params('y', colors='tab:orange', labelsize='large')
        self.heightLine, = self.heightAx.plot([],[], 'tab:orange', linewidth=4)

        self.ids.GraphDisplay.add_widget(FigureCanvasKivyAgg(self.figure))

    def update(self, frame):
        # update plot
        self.times.append( (frame.time - self.startTime).total_seconds() )
        self.speeds.append(frame.IAS)
        self.heights.append(frame.height)

        self.speedLine.set_xdata(self.times)
        self.speedLine.set_ydata(self.speeds)
        self.heightLine.set_xdata(self.times)
        self.heightLine.set_ydata(self.heights)

        self.speedAx.set_xlim(self.times[-1] - GRAPH_MAXT, self.times[-1])
        self.figure.canvas.draw()

        # update info
        self.ids.launchTitle.text    = frame.source
        self.ids.TimeDisplay.text    = str(frame.time)
        self.ids.IASDisplay.text     = "IAS = " + str(frame.IAS)
        self.ids.HeightDisplay.text  = "HEIGHT = " + str(frame.height)

    def save(self):
        data = {}
        data['source'] = self.name
        data['date'] = self.startTime.strftime('%Y.%m.%d-%H.%M')
        data['time'] = self.times
        data['speed'] = self.speeds
        data['height'] = self.heights

        filename = '%s-%s.json' % (self.name, self.startTime.strftime('%y%m%d%H%M'))

        with open(os.path.join(SAVE_DIR, filename), 'w') as file:
            json.dump(data, file)

        Snackbar(text="Launch saved as %s" % filename).show()

    def close(self):
        self.parent.remove_widget(self)
