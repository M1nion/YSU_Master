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

        self.btnStart.clicked.connect(self.startPlot)     #####开始绘图触发事件#####
        self.btnPause.clicked.connect(self.pausePlot)     #####暂停绘图触发事件#####

        self.exit.triggered.connect(self.Exit)            #####窗口退出触发事件#####
        self.save.triggered.connect(self.Save)

        self.sendeeg.triggered.connect(self.SendEEG)  #####窗口OpenEEG触发事件#####
        self.stopeeg.triggered.connect(self.StopEEG)
        self.saveeeg.triggered.connect(self.SaveEEG)
        self.openversion.triggered.connect(self.OpenVersion)
        self.savevars.triggered.connect(self.SaveVARS)
        self.sendprocessedvars.triggered.connect(self.SendProcessedVARS)
        self.stopprocessedvars.triggered.connect(self.StopProcessedVARS)

        self.setcom_bis.triggered.connect(self.SetBISCOM)
        self.setcom_injection.triggered.connect(self.SetInjectionCOM)
        self.showversion.triggered.connect(self.Version)
        self.maingui.triggered.connect(self.MainGUI)
        self.minorgui.triggered.connect(self.MinorGUI)

        self.offline.triggered.connect(self.Offline)
        self.online.triggered.connect(self.Online)

        self.port_button.clicked.connect(self.begin)      #####串口开关触发事件#####
        self.injection_Button.clicked.connect(self.ICOMbegin)
        self.induction_Button.clicked.connect(self.Induction)
        self.remistart_Button.clicked.connect(self.Remistart)
        self.prostart_Button.clicked.connect(self.Prostart)
        self.clear_button.clicked.connect(self.clear)
        self.exit_button.clicked.connect(self.Exit)       #####退出触发事件#####

############MainGUI###################################
    def MainGUI(self):
        self.induction_groupBox.hide()
        self.maintain_groupBox.hide()
        self.add_groupBox.hide()
        self.icom_groupBox.hide()
        self.patient_groupBox.show()
        self.mark_groupBox.show()
        self.datadebug_groupBox.show()
        self.dataoperation_groupBox.show()
        self.plot_groupBox.show()
        self.plotoperation_groupBox.show()

############MinorGUI###################################
    def MinorGUI(self):
        self.induction_groupBox.show()
        self.maintain_groupBox.show()
        self.add_groupBox.show()
        self.icom_groupBox.show()
        self.patient_groupBox.hide()
        self.mark_groupBox.hide()
        self.datadebug_groupBox.hide()
        self.dataoperation_groupBox.hide()
        self.plot_groupBox.hide()
        self.plotoperation_groupBox.hide()

############OpenVersion###################################
    def OpenVersion(self):
        self.GUI_OpenVersion()
        self.portBis.OpenVersion()

############SendProcessedVARS###################################
    def SendProcessedVARS(self):
        self.GUI_SendProcessedVARS()
        self.portBis.SendProcessedVARS()

############StopProcessedVARS###################################
    def StopProcessedVARS(self):
        self.GUI_StopProcessedVARS()
        self.portBis.StopProcessedVARS()

############StopEEG###################################
    def StopEEG(self):
        self.GUI_StopEEG()
        self.portBis.StopEEG()

############SaveVARS###################################
    def SaveVARS(self):
        self.GUI_SaveVARS()
        self.portBis.SaveVARS()

############SaveEEG###################################
    def SaveEEG(self):
        self.GUI_SaveEEG()
        self.portBis.SaveEEG()

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

############SendEEG#######################################
    def SendEEG(self):
        self.GUI_SendEEG()
        self.portBis.SendEEG()

############弹出新窗口SetBISCOM###################################
    def SetBISCOM(self):
        self.setcomport.show()

############弹出新窗口SetInjectionCOM###################################
    def SetInjectionCOM(self):
        self.setingectioncomport.show()

############弹出新窗口Version##################################
    def Version(self):
        self.bisversion.show()
        self.biswarning.show()

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

##########Save病人###信息########################################
    def Save(self):
        self.portBis.flag_record = True
        self.SavePaient()

###########Induction结束#####################################
    def Induction(self):
        self.portInjection.flag_induction = True

###########瑞芬太尼开始#####################################
    def Remistart(self):
        self.portInjection.command1()

###########丙泊酚开始#####################################
    def Prostart(self):
        self.portInjection.command2()

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