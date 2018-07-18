# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mplCanvasWrapper import MplCanvasWrapper
from BIS_port import PortBis
from BIS_setcom import SetCOMPort
from BIS_offline import bis_offline

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):

###################################################################
        self.portBis = PortBis()
        self.setcomport = SetCOMPort()
        #self.setversion =
        self.testTimer = QtCore.QTimer(MainWindow)  ##############设置定时器##############
        self.transportdata = bis_offline()
###################################################################

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
##########################################################################################################
        MainWindow.setGeometry(150, 50, 1000, 650)  ###########将窗体放在桌面中心位置###########
        MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
##########################################################################################################
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.datareceive_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.datareceive_groupBox.setFont(font)
        self.datareceive_groupBox.setObjectName(_fromUtf8("datareceive_groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.datareceive_groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textBrowser_datareceive = QtGui.QTextBrowser(self.datareceive_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_datareceive.setFont(font)
        self.textBrowser_datareceive.setObjectName(_fromUtf8("textBrowser_datareceive"))
        self.gridLayout_4.addWidget(self.textBrowser_datareceive, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.datareceive_groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.plot_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plot_groupBox.setFont(font)
        self.plot_groupBox.setObjectName(_fromUtf8("plot_groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.plot_groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.mplCanvas = MplCanvasWrapper(self.plot_groupBox)
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.gridLayout_5.addWidget(self.mplCanvas, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.plot_groupBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_6.addWidget(self.line_4)
        spacerItem2 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.datadebug_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.datadebug_groupBox.setFont(font)
        self.datadebug_groupBox.setObjectName(_fromUtf8("datadebug_groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.datadebug_groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.textBrowser_datadebug = QtGui.QTextBrowser(self.datadebug_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_datadebug.setFont(font)
        self.textBrowser_datadebug.setObjectName(_fromUtf8("textBrowser_datadebug"))
        self.gridLayout_3.addWidget(self.textBrowser_datadebug, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.datadebug_groupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.dataoperation_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dataoperation_groupBox.setFont(font)
        self.dataoperation_groupBox.setObjectName(_fromUtf8("dataoperation_groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dataoperation_groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.port_button = QtGui.QPushButton(self.dataoperation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.port_button.setFont(font)
        self.port_button.setObjectName(_fromUtf8("port_button"))
        self.horizontalLayout_4.addWidget(self.port_button)
        spacerItem4 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.clear_button = QtGui.QPushButton(self.dataoperation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_4.addWidget(self.clear_button)
        spacerItem5 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.exit_button = QtGui.QPushButton(self.dataoperation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.horizontalLayout_4.addWidget(self.exit_button)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.clear_button.raise_()
        self.exit_button.raise_()
        self.verticalLayout.addWidget(self.dataoperation_groupBox)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.plotoperation_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plotoperation_groupBox.setFont(font)
        self.plotoperation_groupBox.setObjectName(_fromUtf8("plotoperation_groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.plotoperation_groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnStart = QtGui.QPushButton(self.plotoperation_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout.addWidget(self.btnStart)
        spacerItem8 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.btnPause = QtGui.QPushButton(self.plotoperation_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.horizontalLayout.addWidget(self.btnPause)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.plotoperation_groupBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
###############################################
        self.statusBar()
        menubar = self.menuBar()

###############File菜单########################
        file = menubar.addMenu('&File(F)')
        save = file.addMenu('&Save')
        self.exit = QtGui.QAction('Exit', self)
        file.addAction(self.exit)

###############Mode菜单########################
        mode = menubar.addMenu('&Mode(M)')
        online = mode.addMenu('&Online')
        self.offline = QtGui.QAction('Offline', self)
        mode.addAction(self.offline)
###############Option菜单########################
        option = menubar.addMenu('&Option(O)')
        self.setcom = QtGui.QAction('Set COM', self)
        option.addAction(self.setcom)

###############Version菜单########################
        veison = menubar.addMenu('&Version(V)')

###############Operation菜单#####################
        operation = menubar.addMenu('&Operation(O)')

        EEG = operation.addMenu('&EEG')
        self.sendeeg = QtGui.QAction('SendEEG', self)
        EEG.addAction(self.sendeeg)
        self.printeeg = QtGui.QAction('PrintEEG', self)
        EEG.addAction(self.printeeg)
        self.stopeeg = QtGui.QAction('StopEEG', self)
        EEG.addAction(self.stopeeg)
        self.saveeeg = QtGui.QAction('SaveEEG', self)
        EEG.addAction(self.saveeeg)

        Display = operation.addMenu('&Display')
        self.plotshow = QtGui.QAction('PlotShow', self)
        Display.addAction(self.plotshow)
        self.messageshow = QtGui.QAction('MessageShow', self)
        Display.addAction(self.messageshow)

        self.openversion = QtGui.QAction('OpenVersion', self)
        operation.addAction(self.openversion)


###########################################################
        self.plot_groupBox.hide()
        self.plotoperation_groupBox.hide()


        self.retranslateUi(MainWindow)
############################################################################################################################################################
        QtCore.QObject.connect(self.testTimer, QtCore.SIGNAL(_fromUtf8("timeout()")),self.TimeOut)  # 创建定时器事件，触发对应事件TimeOut
#############################################################################################################################################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BIS系统", None))
        self.datareceive_groupBox.setTitle(_translate("MainWindow", "Message Receive Region", None))
        self.plot_groupBox.setTitle(_translate("MainWindow", "Plot Showing Region", None))
        self.datadebug_groupBox.setTitle(_translate("MainWindow", "Message Record Region", None))
        self.textBrowser_datadebug.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文新魏\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'隶书\'; font-weight:400;\"><br /></p></body></html>", None))
        self.dataoperation_groupBox.setTitle(_translate("MainWindow", "Message Operation Region", None))
        self.port_button.setText(_translate("MainWindow", "Open", None))
        self.clear_button.setText(_translate("MainWindow", "Clear", None))
        self.exit_button.setText(_translate("MainWindow", "Exit", None))
        self.plotoperation_groupBox.setTitle(_translate("MainWindow", "Plot Operation Region", None))
        self.btnStart.setText(_translate("MainWindow", "Start", None))
        self.btnPause.setText(_translate("MainWindow", "Pause", None))

#################PlotShow##########################################
    def GUI_PlotShow(self):
        self.plot_groupBox.show()
        self.plotoperation_groupBox.show()
        self.datareceive_groupBox.hide()
        self.datadebug_groupBox.hide()
        self.dataoperation_groupBox.hide()

#################PlotShow##########################################
    def GUI_MessageShow(self):
        self.plot_groupBox.hide()
        self.plotoperation_groupBox.hide()
        self.datareceive_groupBox.show()
        self.datadebug_groupBox.show()
        self.dataoperation_groupBox.show()
#################串口打开GUI##########################################
    def GUI_port_open(self):
        self.textBrowser_datadebug.append("Serial communication has been established")
        self.statusbar.showMessage("Reading serial data", 5000)
        self.port_button.setText(_translate("Form", "Close", None))
        self.testTimer.start(50)

#################串口关闭GUI##########################################
    def GUI_port_close(self):
        self.textBrowser_datadebug.append("Serial communication has been closed")
        self.statusbar.showMessage("Closing serial port", 5000)
        self.port_button.setText(_translate("Form", "Open", None))

######################################################################
    def GUI_abc(self):
        self.portBis.COMport = self.setcomport.COM_comboBox.currentText()
        self.portBis.COMbaudrate = self.setcomport.baudrate_comboBox.currentText()

#################清除按钮GUI##########################################
    def GUI_clear(self):
        self.textBrowser_datadebug.clear()
        self.textBrowser_datareceive.clear()

#################发送EEG命令GUI##########################################
    def GUI_SendEEG(self):
        self.textBrowser_datadebug.append("Send EEG Command has been sended")

#################停止EEG命令GUI##########################################
    def GUI_StopEEG(self):
        self.textBrowser_datadebug.append("STOP EEG Command has been sended")

#################发送EEG命令GUI##########################################
    def GUI_SaveEEG(self):
        self.textBrowser_datadebug.append("EEG data has been saved")

#################定时器################################################
    def TimeOut(self):
        if self.portBis.hexdata != '':
            self.textBrowser_datareceive.insertPlainText(self.portBis.hexdata)
            self.portBis.data = ''
            self.portBis.hexdata = ''
        else:
            if self.portBis.eegch1 != '':
                self.textBrowser_datareceive.insertPlainText(self.portBis.eegch1)
                self.portBis.eegch1 = ''
