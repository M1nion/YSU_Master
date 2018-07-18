# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetCOM.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import serial.tools.list_ports
from PyQt4 import QtCore, QtGui

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

class SetCOMPort(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(SetCOMPort, self).__init__(parent)
        self.setupUi_COM(self)
    def setupUi_COM(self, BISCOM_MainWindow):
        BISCOM_MainWindow.setObjectName(_fromUtf8("BISCOM_MainWindow"))
        BISCOM_MainWindow.resize(313, 289)
#############################################################################
        BISCOM_MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
#############################################################################
        self.centralwidget = QtGui.QWidget(BISCOM_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 19, 265, 183))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.COM_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.COM_label.setFont(font)
        self.COM_label.setObjectName(_fromUtf8("COM_label"))
        self.horizontalLayout_2.addWidget(self.COM_label)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.COM_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.COM_comboBox.setFont(font)
        self.COM_comboBox.setObjectName(_fromUtf8("COM_comboBox"))
        self.horizontalLayout_2.addWidget(self.COM_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.channel_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_label.setFont(font)
        self.channel_label.setObjectName(_fromUtf8("channel_label"))
        self.horizontalLayout_3.addWidget(self.channel_label)
        spacerItem2 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.channel_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_comboBox.setFont(font)
        self.channel_comboBox.setObjectName(_fromUtf8("channel_comboBox"))
        self.channel_comboBox.addItem(_fromUtf8("ch.0"))
        self.channel_comboBox.addItem(_fromUtf8("ch.1"))
        self.horizontalLayout_3.addWidget(self.channel_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.baudrate_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.baudrate_label.setFont(font)
        self.baudrate_label.setObjectName(_fromUtf8("baudrate_label"))
        self.horizontalLayout_4.addWidget(self.baudrate_label)
        spacerItem4 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.baudrate_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.baudrate_comboBox.setFont(font)
        self.baudrate_comboBox.setObjectName(_fromUtf8("baudrate_comboBox"))
        self.baudrate_comboBox.addItem(_fromUtf8("2400"))
        self.baudrate_comboBox.addItem(_fromUtf8("4800"))
        self.baudrate_comboBox.addItem(_fromUtf8("9600"))
        self.baudrate_comboBox.addItem(_fromUtf8("14400"))
        self.baudrate_comboBox.addItem(_fromUtf8("19200"))
        self.baudrate_comboBox.addItem(_fromUtf8("38400"))
        self.baudrate_comboBox.addItem(_fromUtf8("56000"))
        self.baudrate_comboBox.addItem(_fromUtf8("57600"))
        self.baudrate_comboBox.addItem(_fromUtf8("115200"))
        self.baudrate_comboBox.addItem(_fromUtf8("128000"))
        self.horizontalLayout_4.addWidget(self.baudrate_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.sampling_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sampling_label.setFont(font)
        self.sampling_label.setObjectName(_fromUtf8("sampling_label"))
        self.horizontalLayout_5.addWidget(self.sampling_label)
        spacerItem6 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.sample_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sample_comboBox.setFont(font)
        self.sample_comboBox.setObjectName(_fromUtf8("sample_comboBox"))
        self.sample_comboBox.addItem(_fromUtf8("128Hz"))
        self.sample_comboBox.addItem(_fromUtf8("256Hz"))
        self.horizontalLayout_5.addWidget(self.sample_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        BISCOM_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BISCOM_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BISCOM_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BISCOM_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BISCOM_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BISCOM_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(BISCOM_MainWindow)

#################################################################################
        self.COM_comboBox.addItems(self.Port_List())


    def retranslateUi(self, BISCOM_MainWindow):
        BISCOM_MainWindow.setWindowTitle(_translate("BISCOM_MainWindow", "Set BIS COM", None))
        self.COM_label.setText(_translate("BISCOM_MainWindow", "Set COM Port No.", None))
        self.channel_label.setText(_translate("BISCOM_MainWindow", "Set EEG channel No.", None))
        self.baudrate_label.setText(_translate("BISCOM_MainWindow", "Set BaudRate No.", None))
        self.sampling_label.setText(_translate("BISCOM_MainWindow", "Set Sampling Rate", None))

##################################################################################
    def Port_List(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            Com_List.append(port[0])
        return Com_List

