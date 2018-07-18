from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from array import array
from time import ctime,sleep
import time
import threading
from datetime import datetime
from matplotlib.dates import date2num, MinuteLocator, SecondLocator, DateFormatter

X_MINUTES = 0.02
INTERVAL = 0.02
MAXCOUNTER = int(X_MINUTES * 250/ INTERVAL)

class MplCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.ax.set_xlabel("time of data generator")
        #self.ax.set_ylabel('random data value')
        #self.ax.legend()

        self.ax.set_ylim(-50,50)
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.curveObj = None # draw object



    def plot(self, datax, datay):

        if self.curveObj is None:
            #create draw object once
            self.curveObj, = self.ax.plot_date(np.array(datax), np.array(datay),'r-')
        else:
            #update data of draw object
            self.curveObj.set_data(np.array(datax), np.array(datay))
            #update limit of X axis,to make sure it can move
            self.ax.set_xlim(datax[0],datax[-1])

        ticklabels = self.ax.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)

        self.draw()

class  MplCanvasWrapper(QtGui.QWidget):
    def __init__(self , parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.ntb.hide()
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataX= []
        self.dataY= []
        self.data1 = []
        self.data2 = []
        self.count = 0
        self.flag_newdata = False
        self.initDataGenerator()

    def startPlot(self):
        self.__generating = True

    def pausePlot(self):
        self.__generating = False
        pass  

    def initDataGenerator(self):
        self.__generating = False
        self.__exit = False
        self.tData = threading.Thread(name = "dataGenerator",target = self.generateData)
        self.tData.start()

    def releasePlot(self):
         self.__exit  = True
         self.tData.join()

    def openflag_set(self):
        self.flag_newdata = True

    def openflag_clear(self):
        self.flag_newdata = False

    def generateData(self):
        counter = 0
        print('绘图线程运行中 %s' % (ctime()))
        while(True):
            if self.__exit:
                break
            if self.__generating:

                if self.count <= MAXCOUNTER:
                    self.canvas.ax.set_ylim(min(self.data1[0:MAXCOUNTER]), max(self.data1[0:MAXCOUNTER]))
                else:
                    self.canvas.ax.set_ylim(min(self.data1[(self.count - MAXCOUNTER) : self.count]), max(self.data1[(self.count - MAXCOUNTER) : self.count]))

                if self.flag_newdata and self.count <= len(self.data1):
                    newData = self.data1[self.count]
                    self.count += 1
                else:
                    self.count = 0
                    self.flag_newdata = False
                newTime = date2num(datetime.now())
                self.dataX.append(newTime)
                self.dataY.append(newData)
                self.canvas.plot(self.dataX, self.dataY)

                if counter >= MAXCOUNTER:
                    self.dataX.pop(0)
                    self.dataY.pop(0)

                else:
                    counter += 1
            time.sleep(INTERVAL)