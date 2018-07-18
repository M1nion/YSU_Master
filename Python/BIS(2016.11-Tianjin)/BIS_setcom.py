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
    def setupUi_COM(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWinSdow"))
        MainWindow.resize(313, 289)
#############################################################################
        MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
#############################################################################
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 19, 265, 183))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.COM_label = QtGui.QLabel(self.widget)
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
        self.COM_comboBox = QtGui.QComboBox(self.widget)
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
        self.channel_label = QtGui.QLabel(self.widget)
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
        self.channel_comboBox = QtGui.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_comboBox.setFont(font)
        self.channel_comboBox.setObjectName(_fromUtf8("channel_comboBox"))
        self.channel_comboBox.addItem(_fromUtf8(""))
        self.channel_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.channel_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.channel_label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_label_2.setFont(font)
        self.channel_label_2.setObjectName(_fromUtf8("channel_label_2"))
        self.horizontalLayout_4.addWidget(self.channel_label_2)
        spacerItem4 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.baudrate_comboBox = QtGui.QComboBox(self.widget)
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
        self.sampling_label = QtGui.QLabel(self.widget)
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
        self.sample_comboBox = QtGui.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sample_comboBox.setFont(font)
        self.sample_comboBox.setObjectName(_fromUtf8("sample_comboBox"))
        self.sample_comboBox.addItem(_fromUtf8(""))
        self.sample_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.sample_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi_COM(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#################################################################################
        self.COM_comboBox.addItems(self.Port_List())

#################################################################################
    def retranslateUi_COM(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Set COM port", None))
        self.COM_label.setText(_translate("MainWindow", "Set COM Port No.", None))
        self.channel_label.setText(_translate("MainWindow", "Set EEG channel No.", None))
        self.channel_comboBox.setItemText(0, _translate("MainWindow", "ch.0", None))
        self.channel_comboBox.setItemText(1, _translate("MainWindow", "ch.1", None))
        self.channel_label_2.setText(_translate("MainWindow", "Set BaudRate No.", None))
        self.baudrate_comboBox.setItemText(0, _translate("MainWindow", "2400", None))
        self.baudrate_comboBox.setItemText(1, _translate("MainWindow", "4800", None))
        self.baudrate_comboBox.setItemText(2, _translate("MainWindow", "9600", None))
        self.sampling_label.setText(_translate("MainWindow", "Set Sampling Rate", None))
        self.sample_comboBox.setItemText(0, _translate("MainWindow", "128Hz", None))
        self.sample_comboBox.setItemText(1, _translate("MainWindow", "256Hz", None))

######################################################################
    def Port_List(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            Com_List.append(port[0])
        return Com_List