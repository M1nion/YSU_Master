from PyQt4 import QtGui, QtCore
from BIS_mainwindow import Ui_MainWindow
import time


class BIS_MainWindow(Ui_MainWindow):

    def __init__(self, parent=None):

        super(BIS_MainWindow, self).__init__(parent)

        self.setupUi(self)

#####################BIS计时器####################################
        self.timerBISdata =QtCore.QTimer(self)
        self.timerBISdata.timeout.connect(self.OnlineBISdataTimer)
        self.timerBISdata.start(0.1)

#####################注射泵定时器####################################
        self.timerICOM = QtCore.QTimer(self)
        self.timerICOM.timeout.connect(self.ICOMTimer)
        self.timerICOM.start(10000)

#####################按键触发事件####################################
        self.btnStart.clicked.connect(self.startPlot)               ###绘制开始###
        self.btnPause.clicked.connect(self.pausePlot)               ###绘制暂停###
        self.port_button.clicked.connect(self.begin)                #####BIS串口开关#####
        self.ICOM_button.clicked.connect(self.ICOMbegin)
        self.InjectionStart_Button.clicked.connect(self.InjectStart)       #####注射泵串口开始####
        self.InjectctionStop_Button.clicked.connect(self.InjectStop)       #####注射泵串口停止####
        self.ManStart_Button.clicked.connect(self.StartMC)
        self.ManStop_Button.clicked.connect(self.StopMC)
        self.BISset_Button.clicked.connect(self.BIS_SET)                 #####期望BIS值设定#####

        self.clear.triggered.connect(self.Clear)              #####清除界面#####
        self.exit.triggered.connect(self.Exit)                      ###标题栏退出###

        self.Export_data.triggered.connect(self.portBis.SendBIS)            ###BIS数据存储(待修订)###
        self.Export_finish.triggered.connect(self.SaveBIS)
        self.savepatient.triggered.connect(self.SavePatient)        ###病人信息存储###

        self.setcom_bis.triggered.connect(self.SetBISCOM)               ###标题栏BIS设备串口设置###
        self.setcom_injection.triggered.connect(self.SetInjectionCOM)   ###标题栏注射泵设备串口设置###

        self.showversion.triggered.connect(self.Version)            ###标题栏版本信息###

#####################Mark标记####################################
        self.propofol.triggered.connect(self.Mark11)
        self.reminfentanil.triggered.connect(self.Mark12)
        self.cannula.triggered.connect(self.Mark2)
        self.maintain_gas.triggered.connect(self.Mark31)
        self.maintain_liquid.triggered.connect(self.Mark32)
        self.operation_start.triggered.connect(self.Mark4)
        self.operation_end.triggered.connect(self.Mark5)
        self.electrotome.triggered.connect(self.Mark6)
        self.drug_stop.triggered.connect(self.Mark7)
        self.awake.triggered.connect(self.Mark8)
        self.change.triggered.connect(self.Mark9)

##########开始Man-Control############################################
    def StartMC(self):
        self.GUI_StartMC()
        self.paras.Speed = float('%.1f' % self.portInjection.ManSpeed)
        self.portInjection.ICOM_SET = self.paras.SpeedCommand(self.paras.Speed)
        self.portInjection.Injectport_stop()
        time.sleep(0.1)
        self.portInjection.ParaSet()
        time.sleep(0.1)
        self.portInjection.Injectport_start()
        self.paras.autoControl = False
        self.paras.injecting = True
        self.paras.manControl = True

##########停止Man-Control############################################
    def StopMC(self):
        self.GUI_StopMC()
        self.portInjection.Injectport_stop()
        self.paras.injecting = False
        self.paras.manControl = False

##########注射泵串口开关############################################
    def ICOMbegin(self):
        self.GUI_setICOMport()
        self.portInjection.begin()
        if self.portInjection.ser.isOpen() == True:
            self.GUI_ICOM_open()
        else:
            self.GUI_ICOM_close()

###########注射开始#####################################
    def InjectStart(self):
        self.GUI_InjectStart()
        self.paras.injecting = True
        self.paras.autoControl = True
        self.paras.manControl = False

###########注射停止#####################################
    def InjectStop(self):
        self.GUI_InjectStop()
        self.portInjection.Injectport_stop()
        self.paras.injecting = False
        self.paras.autoControl = False



############BIS_Set###################################
    def BIS_SET(self):
        if (self.BIS40.isChecked()):
            self.portBis.bisvalue_expect = 40
        if (self.BIS45.isChecked()):
            self.portBis.bisvalue_expect = 45
        if (self.BIS50.isChecked()):
            self.portBis.bisvalue_expect = 50
        if (self.BIS55.isChecked()):
            self.portBis.bisvalue_expect = 55
        if (self.BIS60.isChecked()):
            self.portBis.bisvalue_expect = 60
        if (self.BIS65.isChecked()):
            self.portBis.bisvalue_expect = 65
        if (self.BIS70.isChecked()):
            self.portBis.bisvalue_expect = 70
        else:
            pass
        self.GUI_BISSET()

############SaveBIS###################################
    def SaveBIS(self):
        self.GUI_SaveBIS()
        self.portBis.SaveBIS()

############Export_finish###################################
    def Export_finish(self):
        pass

############SavePatient###################################
    def SavePatient(self):
        self.GUI_SavePatient()
        self.PatientData()
        self.portBis.SavePatient()
        self.ceff.age = float(self.portBis.agetext)
        self.ceff.weight = float(self.portBis.weighttext)
        self.ceff.height = float(self.portBis.heighttext)
        self.ceff.gender = self.portBis.gendertext
        self.ceff.Ceff_Para()

############OnlineBISdata定时器####################################
    def OnlineBISdataTimer(self):
        if self.portBis.flag_onlineTimer and self.portBis.BISonline != []:
            if self.paras.autoControl:
                self.pidControl.ActualBIS = self.portBis.bisvalue
                self.portInjection.PIDSpeed = self.pidControl.control_pid(25, 0.2, 8, self.portBis.bisvalue_expect)
                if self.portInjection.PIDSpeed > (40*float(self.portBis.weighttext)/60):
                    if (40*float(self.portBis.weighttext)/60) <= 45:
                        self.portInjection.PIDSpeed = 40*float(self.portBis.weighttext)/60
                    else:
                        self.portInjection.PIDSpeed = 45
                elif self.portInjection.PIDSpeed < 0:
                    self.portInjection.PIDSpeed = 0
                else:
                    pass
                self.paras.ceffinal = float('%.2f' % self.ceff.Ceffinal(self.portInjection.PIDSpeed))
                self.paras.Speed = float('%.1f' % self.portInjection.PIDSpeed)
                self.portInjection.ICOM_SET = self.paras.SpeedCommand(self.paras.Speed)
            elif self.paras.manControl:
                self.paras.ceffinal = float('%.2f' % self.ceff.Ceffinal(self.portInjection.ManSpeed))
            else:
                self.paras.ceffinal = float('%.2f' % self.ceff.Ceffinal(0))
                pass
            self.setplot.bisonlinedata.append(self.portBis.bisvalue)
            self.portBis.flag_onlineTimer = False
            self.setplot.flag_onlinebisdata = True
            self.portBis.BISonline = []
        else:
            pass

############注射泵定时器####################################
    def ICOMTimer(self):
        self.paras.localtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
        if self.portInjection.flag_ICOM:
            if self.paras.injecting:
                self.portInjection.Injectport_stop()
                time.sleep(0.1)
                self.portInjection.ParaSet()
                time.sleep(0.1)
                self.portInjection.Injectport_start()
            else:
                pass
            self.GUI_Para()
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
        self.GUI_SendBIS()
        self.portBis.SendBIS()
        self.setplot.flag_BISPlot = True
        self.setplot.startPlot()
        pass

############暂停绘图#########################################
    def pausePlot(self):
        self.GUI_StopBIS()
        self.portBis.StopBIS()
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

##########清除按钮############################################
    def Clear(self):
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