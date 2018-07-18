from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import time
from time import ctime
import threading
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


INTERVAL_online = 0.03
INTERVAL_offline = 0.03
MAXCOUNTER = 200

class SetPlot(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax.set_xlabel('Point')
        self.ax.set_ylabel('EEG')

        self.ax.set_ylim(-3000, 3000)

        xmajorLocator = MultipleLocator(100)
        xmajorFormatter = FormatStrFormatter('%1.1f')
        xminorLocator = MultipleLocator(50)


        self.ax.xaxis.set_major_locator(xmajorLocator)
        self.ax.xaxis.set_minor_locator(xminorLocator)
        self.ax.xaxis.set_major_formatter(xmajorFormatter)
        self.curveObj = None # draw object



    def plot(self, datax, datay):

        if self.curveObj is None:
            #create draw object once
            self.curveObj, = self.ax.plot_date(np.array(datax), np.array(datay), 'r-')
        else:
            self.curveObj.set_data(np.array(datax), np.array(datay))
            self.ax.set_xlim(datax[0], datax[-1])

        ticklabels = self.ax.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)

        self.draw()


class BISPlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.canvas = SetPlot()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.ntb.hide()
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.flag_Zero = True
        self.flag_onlinedata = False
        self.flag_online = False
        self.flag_offline = False

        self.dataX_online = []
        self.dataY_online = []
        self.dataX_offline = []
        self.dataY_offline = []
        self.offlinedata = []
        self.onlinedata = []
        self.count_online = 0
        self.count_offline = 0
        self.count_onlinedata = 0
        self.initDataGenerator()

    def startPlot(self):
        self.__generating = True

    def pausePlot(self):
        self.__generating = False
        pass  

    def initDataGenerator(self):
        self.__generating = False
        self.__exit = False
        self.tData = threading.Thread(name='dataGenerator', target=self.generateData)
        self.tData.start()

    def releasePlot(self):
         self.__exit  = True
         self.tData.join()


    def generateData(self):
        print('Plot线程运行中 %s' % (ctime()))
        while True:
            if self.__exit:
                break
            self.canvas.ax.set_ylim(-3000, 3000)
            if self.flag_Zero:
                for k in range(0, MAXCOUNTER):
                    self.dataY_online.append(0)
                    self.dataX_online.append(k)
                    self.dataY_offline.append(0)
                    self.dataX_offline.append(k)
                self.flag_Zero = False
            else:
                pass
##########################################################################
            if self.flag_online:
                if self.onlinedata == []:
                    self.DataY_online = 0
                    self.count_online += 1
                    self.DataX_online = self.count_online + k
                else:
                    if self.flag_onlinedata:
                        if self.count_onlinedata <= (len(self.onlinedata)-1):
                            self.DataY_online = self.onlinedata[self.count_onlinedata]
                            self.count_online += 1
                            self.count_onlinedata += 1
                            self.DataX_online = self.count_online + k
                        else:
                            self.flag_onlinedata = False
                            self.count_onlinedata = self.count_onlinedata - 1
                    else:
                        self.DataY_online = 0
                        self.count_online += 1
                        self.DataX_online = self.count_online + k

            if self.flag_offline:
                if self.__generating:
                    if self.count_offline <= len(self.offlinedata):
                        self.DataY_offline = self.offlinedata[self.count_offline]
                        self.count_offline += 1
                        self.DataX_offline = self.count_offline + k
                    else:
                        self.count_offline = 0
                else:
                    pass
            else:
                pass
##########################################################################
            if self.flag_online:
                self.dataX_online.pop(0)
                self.dataY_online.pop(0)
                self.dataX_online.append(self.DataX_online)
                self.dataY_online.append(self.DataY_online)
                time.sleep(INTERVAL_online)
                if self.__generating:
                    self.canvas.plot(self.dataX_online, self.dataY_online)
                else:
                    pass
            if self.flag_offline:
                if self.__generating:
                    self.dataX_offline.pop(0)
                    self.dataY_offline.pop(0)
                    self.dataX_offline.append(self.DataX_offline)
                    self.dataY_offline.append(self.DataY_offline)
                    time.sleep(INTERVAL_offline)
                    self.canvas.plot(self.dataX_offline, self.dataY_offline)
                else:
                    pass

            else:
                pass
