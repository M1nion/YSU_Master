from PyQt4 import QtGui, QtCore
from BIS_mainwindow import Ui_MainWindow


class BIS_MainWindow(Ui_MainWindow):

    def __init__(self, parent=None):

        super(BIS_MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.timerEEG = QtCore.QTimer(self)
        self.timerEEG.timeout.connect(self.OnlineEEGTimer)
        self.timerEEG.start(0.1)

        self.timerBIS =QtCore.QTimer(self)
        self.timerBIS.timeout.connect(self.OnlineBISTimer)
        self.timerBIS.start(0.1)

        self.timerBISdata =QtCore.QTimer(self)
        self.timerBISdata.timeout.connect(self.OnlineBISdataTimer)
        self.timerBISdata.start(0.1)

        self.Mark11_Button.clicked.connect(self.Mark11)
        self.Mark12_Button.clicked.connect(self.Mark12)
        self.Mark2_Button.clicked.connect(self.Mark2)
        self.Mark31_Button.clicked.connect(self.Mark31)
        self.Mark32_Button.clicked.connect(self.Mark32)
        self.Mark4_Button.clicked.connect(self.Mark4)
        self.Mark5_Button.clicked.connect(self.Mark5)
        self.Mark6_Button.clicked.connect(self.Mark6)
        self.Mark7_Button.clicked.connect(self.Mark7)
        self.Mark8_Button.clicked.connect(self.Mark8)
        self.Mark9_Button.clicked.connect(self.Mark9)

        self.btnStart.clicked.connect(self.startPlot)
        self.btnPause.clicked.connect(self.pausePlot)

        self.exit.triggered.connect(self.Exit)

        self.saveeeg.triggered.connect(self.SaveEEG)
        self.savebis.triggered.connect(self.SaveBIS)
        self.savepatient.triggered.connect(self.SavePatient)

        self.setcom_bis.triggered.connect(self.SetBISCOM)
        self.setcom_injection.triggered.connect(self.SetInjectionCOM)
        self.showversion.triggered.connect(self.Version)

        self.offline.triggered.connect(self.Offline)
        self.online.triggered.connect(self.Online)

        self.port_button.clicked.connect(self.begin)      #####串口开关触发事件#####
        self.injection_Button.clicked.connect(self.ICOMbegin)
        self.induction_Button.clicked.connect(self.Induction)
        self.remistart_Button.clicked.connect(self.Remistart)
        self.prostart_Button.clicked.connect(self.Prostart)
        self.bis_Button.clicked.connect(self.BIS)
        self.eeg_Button.clicked.connect(self.EEG)
        self.Injectctionstop_Button.clicked.connect(self.ICOMStop)
        self.stopbis_Button.clicked.connect(self.StopBIS)
        self.stopeeg_Button.clicked.connect(self.StopEEG)
        self.clear_button.clicked.connect(self.clear)
        self.exit_button.clicked.connect(self.Exit)


        self.BISset_Button.clicked.connect(self.BIS_SET)

############BIS_20###################################
    def BIS_SET(self):
        if(self.BIS20.isChecked()):
            self.portBis.bisvalue_expect = 20
        if (self.BIS40.isChecked()):
            self.portBis.bisvalue_expect = 40
        if (self.BIS60.isChecked()):
            self.portBis.bisvalue_expect = 60
        if(self.BIS80.isChecked()):
            self.portBis.bisvalue_expect = 80
        else:
            pass

############BISPlot###################################
    def BIS(self):
        self.GUI_SendBIS()
        self.portBis.SendBIS()
        self.setplot.flag_BISPlot = True
        self.setplot.flag_EEGPlot = False

############EEGPlot###################################
    def EEG(self):
        self.GUI_SendEEG()
        self.portBis.SendEEG()
        self.setplot.flag_BISPlot = False
        self.setplot.flag_EEGPlot = True

###########瑞芬太尼开始#####################################
    def Remistart(self):
        self.portInjection.command1()

###########丙泊酚开始#####################################
    def Prostart(self):
        self.portInjection.command2()

###########注射泵停止#####################################
    def ICOMStop(self):
        self.portInjection.command3()

############StopProcessedVARS###################################
    def StopBIS(self):
        #self.setplot.flag_BISPlot = False
        self.GUI_StopBIS()
        self.portBis.StopBIS()

############StopEEG###################################
    def StopEEG(self):
        self.GUI_StopEEG()
        self.portBis.StopEEG()

############SaveBIS###################################
    def SaveBIS(self):
        self.GUI_SaveBIS()
        self.portBis.SaveBIS()

############SaveEEG###################################
    def SaveEEG(self):
        self.GUI_SaveEEG()
        self.portBis.SaveEEG()

############SavePatient###################################
    def SavePatient(self):
        self.GUI_SavePatient()
        self.PatientData()
        self.portBis.SavePatient()

############Offline####################################
    def Offline(self):
        self.transportdata.Offline()
        self.setplot.offlinedata = self.transportdata.CH1
        self.portBis.flag_online = False
        self.setplot.flag_online = False
        self.setplot.flag_offline = True

############Online####################################
    def Online(self):
        self.portBis.flag_online = True
        self.setplot.flag_online = True
        self.setplot.flag_offline = False

############OnlineEEG####################################
    def OnlineEEGTimer(self):
        if self.portBis.flag_onlineTimer and self.portBis.EEGCH1_online != []:
            self.setplot.onlinedata.append(self.portBis.EEGCH1_online)
            self.portBis.flag_onlineTimer = False
            self.setplot.flag_onlinedata = True
            self.portBis.EEGCH1_online = []
        else:
            pass

############OnlineBIS####################################
    def OnlineBISTimer(self):
        if self.portBis.bisvalue_warning >= 60 and self.portInjection.flag_induction:
            self.biswarning.show()
            self.portBis.bisvalue_warning = 0
            self.portBis.flag_warning = True
        else:
            pass
############OnlineBISdata####################################
    def OnlineBISdataTimer(self):
        if self.portBis.flag_onlineTimer and self.portBis.BISonline != []:
            self.setplot.bisonlinedata.append(self.portBis.bisvalue)
            self.portBis.flag_onlineTimer = False
            self.setplot.flag_onlinebisdata = True
            self.portBis.BISonline = []
        else:
            pass

############弹出新窗口SetBISCOM###################################
    def SetBISCOM(self):
        self.setcomport.show()

############弹出新窗口SetInjectionCOM###################################
    def SetInjectionCOM(self):
        self.setingectioncomport.show()

############弹出新窗口Version##################################
    def Version(self):
        self.bisversion.show()

############开始绘图#########################################
    def startPlot(self):
        self.setplot.startPlot()
        pass

############暂停绘图#########################################
    def pausePlot(self):
        self.setplot.pausePlot()
        pass

##########Mark11############################################
    def Mark11(self):
        self.portBis.flag_MARK11 = True
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark12############################################
    def Mark12(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = True
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark2############################################
    def Mark2(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = True
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark31############################################
    def Mark31(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = True
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark32############################################
    def Mark32(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = True
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark4############################################
    def Mark4(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = True
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark5############################################
    def Mark5(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = True
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark6############################################
    def Mark6(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = True
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark7############################################
    def Mark7(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = True
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = False

##########Mark8############################################
    def Mark8(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = True
        self.portBis.flag_MARK9 = False

##########Mark9############################################
    def Mark9(self):
        self.portBis.flag_MARK11 = False
        self.portBis.flag_MARK12 = False
        self.portBis.flag_MARK2 = False
        self.portBis.flag_MARK31 = False
        self.portBis.flag_MARK32 = False
        self.portBis.flag_MARK4 = False
        self.portBis.flag_MARK5 = False
        self.portBis.flag_MARK6 = False
        self.portBis.flag_MARK7 = False
        self.portBis.flag_MARK8 = False
        self.portBis.flag_MARK9 = True

###########释放线程#######################################
    def release(self):
        self.portBis.releasePort()
        self.setplot.releasePlot()

##########串口开关############################################
    def begin(self):
        self.GUI_setport()
        self.portBis.begin()
        if self.portBis.ser.isOpen() == True:
            self.GUI_port_open()
        else:
            self.GUI_port_close()

##########Injection串口开关############################################
    def ICOMbegin(self):
        self.GUI_setICOMport()
        self.portInjection.begin()
        if self.portInjection.ser.isOpen() == True:
            self.GUI_ICOM_open()
        else:
            self.GUI_ICOM_close()


###########Induction结束#####################################
    def Induction(self):
        self.GUI_Induction()
        self.portInjection.flag_induction = True


##########清除按钮############################################
    def clear(self):
        self.GUI_clear()
        self.portBis.flag_MARK = True

###########退出按钮###########################################
    def Exit(self):
        self.release()
        quit()

###########关闭按钮###########################################
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            self.release()
            event.accept()

#####################主函数#####################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = BIS_MainWindow()
    ui.show()
    sys.exit(app.exec_())