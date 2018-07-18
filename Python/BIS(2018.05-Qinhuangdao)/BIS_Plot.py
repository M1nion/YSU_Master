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
INTERVAL_bisonline = 0.8
MAXCOUNTER = 2000

class SetPlot(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.ax.set_ylim(0, 100)

        xmajorLocator = MultipleLocator(100)
        xminorLocator = MultipleLocator(50)
        xmajorFormatter = FormatStrFormatter('%1d')

        ymajorLocator = MultipleLocator(20)  # 将y轴主刻度标签设置为20的倍数
        yminorLocator = MultipleLocator(10)  # 将此y轴次刻度标签设置为10的倍数
        ymajorFormatter = FormatStrFormatter('%1d')  # 设置y轴标签文本的格式

        self.ax.xaxis.set_major_locator(xmajorLocator)
        self.ax.xaxis.set_minor_locator(xminorLocator)
        self.ax.xaxis.set_major_formatter(xmajorFormatter)
        self.ax.xaxis.grid(True, which='major')  # x坐标轴的网格使主刻度用

        self.ax.yaxis.set_major_locator(ymajorLocator)
        self.ax.yaxis.set_minor_locator(yminorLocator)
        self.ax.yaxis.set_major_formatter(ymajorFormatter)
        self.ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
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
        self.flag_Zero = True
        self.flag_onlinebisdata = False

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

##################绘制实时BIS曲线###################
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
##################plot线程###################
    def plot_thread(self):
        print('Plot线程运行中 %s' % (ctime()))
        while True:
            if self.__exit:
                break
            if self.flag_Zero:
                for self.k in range(0, MAXCOUNTER):
                    self.bisdataY_online.append(0)
                    self.bisdataX_online.append(self.k)
                self.flag_Zero = False
            else:
                pass
            if self.flag_BISPlot:
                self.canvas.ax.set_ylim(0, 100)
                self.onlinePlot_BIS()
            else:
                pass
