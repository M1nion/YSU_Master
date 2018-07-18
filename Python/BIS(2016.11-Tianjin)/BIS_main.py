from PyQt4 import QtGui
from BIS_mainwindow import Ui_MainWindow

class BIS_MainWindow(Ui_MainWindow):

    def __init__(self, parent=None):

        super(BIS_MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.btnStart.clicked.connect(self.startPlot)     #####开始绘图触发事件#####
        self.btnPause.clicked.connect(self.pausePlot)     #####暂停绘图触发事件#####

        self.exit.triggered.connect(self.Exit)            #####窗口退出触发事件#####
        self.sendeeg.triggered.connect(self.SendEEG)  #####窗口OpenEEG触发事件#####
        self.printeeg.triggered.connect(self.PrintEEG)
        self.openversion.triggered.connect(self.OpenVersion)
        self.stopeeg.triggered.connect(self.StopEEG)
        self.saveeeg.triggered.connect(self.SaveEEG)
        self.plotshow.triggered.connect(self.PlotShow)
        self.messageshow.triggered.connect(self.MessageShow)
        self.setcom.triggered.connect(self.SetCOM)
        self.offline.triggered.connect(self.OpenFile)

        self.port_button.clicked.connect(self.begin)      #####串口开关触发事件#####
        self.clear_button.clicked.connect(self.clear)
        self.exit_button.clicked.connect(self.Exit)       #####退出触发事件#####

############PlotShow###################################
    def PlotShow(self):
        self.GUI_PlotShow()

############PlotShow###################################
    def MessageShow(self):
        self.GUI_MessageShow()

############OpenVersion###################################
    def OpenVersion(self):
        self.portBis.OpenVersion()
        # self.GUI_OpenVersion()

############OpenVersion###################################
    def StopEEG(self):
        self.portBis.StopEEG()
        self.GUI_StopEEG()

############PrintEEG###################################
    def PrintEEG(self):
        print(self.portBis.EEGCH1)
        print(self.portBis.EEGCH2)

############PrintEEG###################################
    def SaveEEG(self):
        self.portBis.SaveEEG()
        self.GUI_SaveEEG()

############打开文件####################################
    def OpenFile(self):
        self.transportdata.openFile()
        self.mplCanvas.data1 = self.transportdata.CH1
        self.mplCanvas.data2 = self.transportdata.CH2
        self.mplCanvas.openflag_set()
        pass

############OpenEEG#######################################
    def SendEEG(self):
        self.portBis.SendEEG()
        self.GUI_SendEEG()
        self.mplCanvas.openflag_set()

############弹出新窗口SetCOM###################################
    def SetCOM(self):
        self.setcomport.show()

############弹出新窗口Version##################################
    #def Version(self):
        #self.

############开始绘图#########################################
    def startPlot(self):
        self.mplCanvas.startPlot()
        pass

############暂停绘图#########################################
    def pausePlot(self):
        self.mplCanvas.pausePlot()
        pass

##########释放绘图线程########################################
    def releasePlot(self):
        self.mplCanvas.releasePlot()
        pass

###########释放串口线程#######################################
    def releasePort(self):
        self.portBis.releasePort()

##########串口开关############################################
    def begin(self):
        self.GUI_abc()
        self.portBis.begin()
        if self.portBis.ser.isOpen() == True:
            self.GUI_port_open()
        else:
            self.GUI_port_close()
        pass

##########清除按钮############################################
    def clear(self):
        self.GUI_clear()

###########退出按钮###########################################
    def Exit(self):
        self.releasePlot()  ######释放绘图线程######
        self.releasePort()  ######释放串口线程######
        quit()

###########关闭按钮###########################################
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit ?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            self.releasePlot()  ######释放绘图线程######
            self.releasePort()  ######释放串口线程######
            event.accept()

#####################主函数#####################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = BIS_MainWindow()
    ui.show()

sys.exit(app.exec_())