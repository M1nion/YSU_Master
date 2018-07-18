# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '702.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import threading
import serial
import binascii
import struct
import serial.tools.list_ports

from time import ctime,sleep
from PyQt4 import QtCore, QtGui


global data
global hexdata
global asciidata
data = ''
hexdata = ''
asciidata = ''
global flag_hexsend
flag_hexsend = 1
global flag_hexshow
flag_hexshow = 1
global flag_port
flag_port = 0
global ser
ser = serial.Serial('COM3', 9600, timeout=1)
ser.close()


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
########################################################################################################
        MainWindow.setGeometry(150,50,1000, 650)            ###########将窗体放在桌面中心位置###########
        MainWindow.setWindowIcon(QtGui.QIcon('C:\\Desktop\\BIS\\李健楠python\\燕山大学.jpg')) #设置窗体图标
########################################################################################################
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
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
        self.horizontalLayout_6.addWidget(self.datareceive_groupBox)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_6.addWidget(self.line_4)
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
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
        self.verticalLayout_5.addWidget(self.datadebug_groupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.operation_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.operation_groupBox.setFont(font)
        self.operation_groupBox.setObjectName(_fromUtf8("operation_groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.operation_groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.port_button = QtGui.QPushButton(self.operation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.port_button.setFont(font)
        self.port_button.setObjectName(_fromUtf8("port_button"))
        self.horizontalLayout_3.addWidget(self.port_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.savefile_button = QtGui.QPushButton(self.operation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.savefile_button.setFont(font)
        self.savefile_button.setObjectName(_fromUtf8("savefile_button"))
        self.horizontalLayout_3.addWidget(self.savefile_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.clear_button = QtGui.QPushButton(self.operation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_4.addWidget(self.clear_button)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.openfile_button = QtGui.QPushButton(self.operation_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.openfile_button.setFont(font)
        self.openfile_button.setObjectName(_fromUtf8("openfile_button"))
        self.horizontalLayout_4.addWidget(self.openfile_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.comboBox = QtGui.QComboBox(self.operation_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_4.addWidget(self.comboBox)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.comboBox_2 = QtGui.QComboBox(self.operation_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.operation_groupBox)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem8)
        self.senddata_groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文新魏"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.senddata_groupBox.setFont(font)
        self.senddata_groupBox.setObjectName(_fromUtf8("senddata_groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.senddata_groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.datasend_lineEdit = QtGui.QLineEdit(self.senddata_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("隶书"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.datasend_lineEdit.setFont(font)
        self.datasend_lineEdit.setText(_fromUtf8(""))
        self.datasend_lineEdit.setObjectName(_fromUtf8("datasend_lineEdit"))
        self.horizontalLayout.addWidget(self.datasend_lineEdit)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.senddata_button = QtGui.QPushButton(self.senddata_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.senddata_button.setFont(font)
        self.senddata_button.setObjectName(_fromUtf8("senddata_button"))
        self.horizontalLayout.addWidget(self.senddata_button)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkbox_hexsend = QtGui.QCheckBox(self.senddata_groupBox)
###########################################################
        self.checkbox_hexsend.toggle()
###########################################################
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("黑体"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkbox_hexsend.setFont(font)
        self.checkbox_hexsend.setObjectName(_fromUtf8("checkbox_hexsend"))
        self.verticalLayout.addWidget(self.checkbox_hexsend)
        self.checkBox_hexshow = QtGui.QCheckBox(self.senddata_groupBox)
###########################################################
        self.checkBox_hexshow.toggle()
###########################################################
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("黑体"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_hexshow.setFont(font)
        self.checkBox_hexshow.setObjectName(_fromUtf8("checkBox_hexshow"))
        self.verticalLayout.addWidget(self.checkBox_hexshow)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem11)
        self.exit_button = QtGui.QPushButton(self.senddata_groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("楷体"))
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.verticalLayout_2.addWidget(self.exit_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.senddata_groupBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
#####################################################################################################
        self.testTimer = QtCore.QTimer(MainWindow)           ##############设置定时器##############

        File = self.menubar.addMenu("&文件")
        File.addMenu("&打开文件")
        File.addMenu("&保存文件")
        File.addMenu("&退出")
        Edit = self.menubar.addMenu("&编辑")
        Edit.addMenu("撤销")
        Edit.addMenu("复制")
        Edit.addMenu("粘贴")
        Option = self.menubar.addMenu("&选项")
        Option.addMenu("操作界面")
        Option.addMenu("输入命令界面")
        Help = self.menubar.addMenu("&帮助")
        Help.addMenu("说明")
#######################################################################################################
        self.retranslateUi(MainWindow)
#################################################################################################################################################
        QtCore.QObject.connect(self.port_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Begin)    #创建开关按钮，触发时对应事件Begin
        QtCore.QObject.connect(self.senddata_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Senddata)      #创建发送数据按钮，触发时对应事件Senddata
        QtCore.QObject.connect(self.testTimer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.TimeOut)     #创建定时器事件，触发对应事件TimeOut
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Exit)      #创建退出按钮，触发时对应事件Exit
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Clear)    #创建清除按钮，触发时对应事件Clear
        QtCore.QObject.connect(self.savefile_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SaveFile)   #创建保存文件按钮，触发时对应事件SaveFile
        QtCore.QObject.connect(self.openfile_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenFile)   #创建打开文件按钮，触发时对应事件OpenFile
        QtCore.QObject.connect(self.checkbox_hexsend, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), self.HexSend)  #创建十六进制发送复选框，触发事件HexSend
        QtCore.QObject.connect(self.checkBox_hexshow, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), self.HexShow)  #创建十六进制显示复选框，触发事件HexShow
#################################################################################################################################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.addItems(self.Port_List())

    def retranslateUi(self, MainWindow):
###########################################################################################
        MainWindow.setWindowTitle(_translate("MainWindow", "BIS系统", None))
###########################################################################################
        self.datareceive_groupBox.setTitle(_translate("MainWindow", "信息接收区", None))
        self.datadebug_groupBox.setTitle(_translate("MainWindow", "信息调试区", None))
        self.textBrowser_datadebug.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文新魏\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'隶书\'; font-weight:400;\"><br /></p></body></html>", None))
        self.operation_groupBox.setTitle(_translate("MainWindow", "操作界面", None))
        self.port_button.setText(_translate("MainWindow", "打开串口", None))
        self.savefile_button.setText(_translate("MainWindow", "保存文件", None))
        self.clear_button.setText(_translate("MainWindow", "清除窗口", None))
        self.openfile_button.setText(_translate("MainWindow", "打开文件", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "2400", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "4800", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "9600", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "14400", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "19200", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "38400", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "56000", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "57600", None))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "115200", None))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "128000", None))
        self.senddata_groupBox.setTitle(_translate("MainWindow", "信息发送区", None))
        self.senddata_button.setText(_translate("MainWindow", "发送信息", None))
        self.checkbox_hexsend.setText(_translate("MainWindow", "  HEX发送", None))
        self.checkBox_hexshow.setText(_translate("MainWindow", "  HEX显示", None))
        self.exit_button.setText(_translate("MainWindow", "退出", None))

#####串口开关#####
    def Begin(self):
        global ser
        global data
        global flag_port
        if ser.isOpen() == True :
            flag_port = 1
            self.textBrowser_datadebug.append("串口已经关闭")
            self.statusbar.showMessage("数据接收停止",5000)
            self.port_button.setText(_translate("Form", "打开串口", None))

        else:
            ser.open()
            flag_port = 0
            if ser.isOpen() == True:
                self.textBrowser_datadebug.append("串口通讯已经建立")
                self.statusbar.showMessage("正在读取串口数据",5000)
                #self.textBrowser_datadebug.append("正在读取串口数据")
                self.port_button.setText(_translate("Form", "关闭串口", None))
                self.testTimer.start(50)
            else:
                self.textBrowser_datadebug.append("串口通讯未建立")

####发送数据####
    def Senddata(self):
        global ser
        global text
        text = self.datasend_lineEdit.text()
        self.statusbar.showMessage("数据发送中",5000)
        if flag_hexsend == 1:            
            text1 = bytes.fromhex(text)
            ser.write(text1)
        if flag_hexsend == 0:
            text2 = text.encode('ascii') 
            ser.write(text2)
              
####定时器接收数据####
    def TimeOut(self):
        global data
        global ser
        global hexdata
        global asciidata
        global flag_hexshow
        self.statusbar.showMessage("正在读取串口数据",5000)
        if flag_hexshow == 1:
            if hexdata != '':
                self.textBrowser_datareceive.insertPlainText(hexdata)
                data = ''
                hexdata = ''
        if flag_hexshow == 0:
            if asciidata != '':
                asciidata = asciidata.decode("ascii")
                self.textBrowser_datareceive.insertPlainText(asciidata)
                asciidata = ''
                data = ''
######退出######
    def Exit(self):
        global ser
        global flag_port
        if ser.isOpen() == True:
            flag_port = 1
            #sleep(1)        
            quit()
        else:
            quit()

######清空窗口######
    def Clear(self):
        self.textBrowser_datareceive.clear()
        self.textBrowser_datadebug.append("数据已清空")
        self.statusbar.showMessage("窗口清除中",5000)

######保存文件######
    def SaveFile(self):
        self.textBrowser_datadebug.append("文件已保存")
        self.statusbar.showMessage("文件保存中",5000)

######打开文件######
    def OpenFile(self):
        self.textBrowser_datadebug.append("文件打开中")
        self.statusbar.showMessage("文件打开中",5000)

    def HexSend(self):
        global flag_hexsend
        if self.checkbox_hexsend.isChecked():
            flag_hexsend = 1
        else:
            flag_hexsend = 0

    def HexShow(self):
        global flag_hexshow
        if self.checkBox_hexshow.isChecked():
            flag_hexshow = 1
        else:
            flag_hexshow =0

    def Port_List(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            Com_List.append(port[0])
        return Com_List

###########################################################################################
######串口函数#####
###########################################################################################
def port(self):
    global data
    global ser
    global flag_port
    global flag_hexshow
    global hexdata
    global asciidata
    print ('串口正在接受 %s' %(ctime()))
    while True:
        if ser.isOpen() == True:
            if flag_port == 0:
                if ser.inWaiting() > 0:
                    data = ser.read(ser.inWaiting())
                    if flag_hexshow == 0:
                        asciidata = data
                    if flag_hexshow == 1:
                        if not len(data)%2 :
                            data = binascii.b2a_hex(data)
                            data = data.decode('ascii')
                            m = len(data)
                            data_i = 1
                            while data_i <= m:
                                hexdata = hexdata + data[data_i-1:data_i+1]+' '
                                hexdata = hexdata.upper()
                                data_i = data_i + 2
                        else:
                            print("字符串位数不正确!")


            if flag_port == 1:
                ser.close()
                flag_port = 0            

###########################################################################################
######界面函数#####
###########################################################################################
def gui(self):
    print ('界面正在运行 %s' %(ctime()))

    app = QtGui.QApplication(sys.argv)
    Mainwindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())

#####################################################################
##两个线程##
#####################################################################
threads = []
t1 = threading.Thread(target=port, args=(u'串口正在接受',))
threads.append(t1)
t2 = threading.Thread(target=gui, args=(u'界面正在运行',))
threads.append(t2)

#####################################################################
####主函数####
#####################################################################
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()  

    t.join()

    print ("all over %s" %ctime())
