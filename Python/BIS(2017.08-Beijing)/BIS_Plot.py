from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import time
from time import ctime
import threading
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


INTERVAL_online = 0.0015
INTERVAL_offline = 0.03
INTERVAL_bisonline = 0.8
MAXCOUNTER = 1000

class SetPlot(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.ax.set_ylim(-3000, 3000)

        xmajorLocator = MultipleLocator(1000)
        xmajorFormatter = FormatStrFormatter('%1.1f')
        xminorLocator = MultipleLocator(500)

        self.ax.xaxis.set_major_locator(xmajorLocator)
        self.ax.xaxis.set_minor_locator(xminorLocator)
        self.ax.xaxis.set_major_formatter(xmajorFormatter)
        self.curveObj = None

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


        self.initDataGenerator()

    def startPlot(self):
        self.__generating = True

    def pausePlot(self):
        self.__generating = False

    def initDataGenerator(self):

        self.__generating = False
        self.__exit = False
        self.flag_BISPlot = False
        self.flag_EEGPlot = False
        self.flag_Zero = True
        self.flag_onlinedata = False
        self.flag_onlinebisdata = False
        self.flag_online = False
        self.flag_offline = False

        self.dataX_online = []
        self.dataY_online = []
        self.onlinedata = []
        self.count_online = 0
        self.count_onlinedata = 0

        self.dataX_offline = []
        self.dataY_offline = []
        self.offlinedata = []
        self.count_offline = 0

        self.bisdataX_online = []
        self.bisdataY_online = []
        self.bisonlinedata = []
        self.count_bisonline = 0
        self.count_bisonlinedata = 0

        self.t2 = threading.Thread(target=self.plot_thread)
        self.t2.start()

    def releasePlot(self):
         self.__exit  = True
         self.t2.join()

########################实时plot#####################################################
    def onlinePlot(self):
        if self.onlinedata == []:
            self.DataY_online = 0
            self.count_online += 1
            self.DataX_online = self.count_online + self.k
        else:
            if self.flag_onlinedata:
                if self.count_onlinedata <= (len(self.onlinedata) - 1):
                    self.DataY_online = self.onlinedata[self.count_onlinedata]
                    self.count_online += 1
                    self.count_onlinedata += 1
                    self.DataX_online = self.count_online + self.k
                else:
                    self.flag_onlinedata = False
                    self.count_onlinedata = self.count_onlinedata - 1
            else:
                self.DataY_online = 0
                self.count_online += 1
                self.DataX_online = self.count_online + self.k
        self.dataX_online.pop(0)
        self.dataY_online.pop(0)
        self.dataX_online.append(self.DataX_online)
        self.dataY_online.append(self.DataY_online)
        time.sleep(INTERVAL_online)
        if self.__generating:
            self.canvas.plot(self.dataX_online, self.dataY_online)
        else:
            pass

########################离线plot#####################################################
    def offlinePlot(self):
        if self.__generating:
            if self.count_offline <= len(self.offlinedata):
                self.DataY_offline = self.offlinedata[self.count_offline]
                self.count_offline += 1
                self.DataX_offline = self.count_offline + self.k
            else:
                self.count_offline = 0
            self.dataX_offline.pop(0)
            self.dataY_offline.pop(0)
            self.dataX_offline.append(self.DataX_offline)
            self.dataY_offline.append(self.DataY_offline)
            time.sleep(INTERVAL_offline)
            self.canvas.plot(self.dataX_offline, self.dataY_offline)
        else:
            pass

########################plot线程#####################################################
    def onlinePlot_BIS(self):
        if self.bisonlinedata == []:
            self.bisDataY_online = 0
            self.count_bisonline += 1
            self.bisDataX_online = self.count_bisonline + self.k
        else:
            if self.flag_onlinebisdata:
                if self.count_bisonlinedata <= (len(self.bisonlinedata) - 1):
                    self.bisDataY_online = self.bisonlinedata[self.count_bisonlinedata]
                    self.count_bisonline += 1
                    self.count_bisonlinedata += 1
                    self.bisDataX_online = self.count_bisonline + self.k
                else:
                    self.flag_onlinebisdata = False
                    self.count_bisonlinedata = self.count_bisonlinedata - 1
            else:
                self.bisDataY_online = 0
                self.count_bisonline += 1
                self.bisDataX_online = self.count_bisonline + self.k
        self.bisdataX_online.pop(0)
        self.bisdataY_online.pop(0)
        self.bisdataX_online.append(self.bisDataX_online)
        self.bisdataY_online.append(self.bisDataY_online)
        time.sleep(INTERVAL_bisonline)
        if self.__generating:
            self.canvas.plot(self.bisdataX_online, self.bisdataY_online)
        else:
            pass
    def plot_thread(self):
        print('Plot线程运行中 %s' % (ctime()))
        while True:
            if self.__exit:
                break
            if self.flag_Zero:
                for self.k in range(0, MAXCOUNTER):
                    self.dataY_online.append(0)
                    self.dataX_online.append(self.k)
                    self.bisdataY_online.append(0)
                    self.bisdataX_online.append(self.k)
                    self.dataY_offline.append(0)
                    self.dataX_offline.append(self.k)
                self.flag_Zero = False
            else:
                pass
            if self.flag_online:
                if self.flag_BISPlot:
                    self.canvas.ax.set_ylim(0, 100)
                    self.onlinePlot_BIS()
                if self.flag_EEGPlot:
                    self.canvas.ax.set_ylim(-100, 100)
                    self.onlinePlot()
                else:
                    pass
            if self.flag_offline:
                self.canvas.ax.set_ylim(-100, 100)
                self.offlinePlot()
            else:
                pass
