# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InjectionSetCOM.ui'
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

class InjectionSetCOMPort(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(InjectionSetCOMPort, self).__init__(parent)
        self.setupUi_InjectionCOM(self)
    def setupUi_InjectionCOM(self, InjectionCOM_MainWindow):
        InjectionCOM_MainWindow.setObjectName(_fromUtf8("InjectionCOM_MainWindow"))
        InjectionCOM_MainWindow.resize(313, 289)
#############################################################################
        InjectionCOM_MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
#############################################################################
        self.centralwidget = QtGui.QWidget(InjectionCOM_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(22, 21, 262, 197))
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
        spacerItem1 = QtGui.QSpacerItem(260, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.parity_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parity_label.setFont(font)
        self.parity_label.setObjectName(_fromUtf8("parity_label"))
        self.horizontalLayout.addWidget(self.parity_label)
        spacerItem2 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.parity_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parity_comboBox.setFont(font)
        self.parity_comboBox.setObjectName(_fromUtf8("parity_comboBox"))
        self.parity_comboBox.addItem(_fromUtf8("N"))
        self.parity_comboBox.addItem(_fromUtf8("O"))
        self.parity_comboBox.addItem(_fromUtf8("E"))
        self.parity_comboBox.addItem(_fromUtf8("M"))
        self.parity_comboBox.addItem(_fromUtf8("S"))
        self.horizontalLayout.addWidget(self.parity_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(260, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
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
        spacerItem5 = QtGui.QSpacerItem(260, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.stopbits_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stopbits_label.setFont(font)
        self.stopbits_label.setObjectName(_fromUtf8("stopbits_label"))
        self.horizontalLayout_5.addWidget(self.stopbits_label)
        spacerItem6 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.stopbits_comboBox = QtGui.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stopbits_comboBox.setFont(font)
        self.stopbits_comboBox.setObjectName(_fromUtf8("stopbits_comboBox"))
        self.stopbits_comboBox.addItem(_fromUtf8("1"))
        self.stopbits_comboBox.addItem(_fromUtf8("1.5"))
        self.stopbits_comboBox.addItem(_fromUtf8("2"))
        self.horizontalLayout_5.addWidget(self.stopbits_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        InjectionCOM_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(InjectionCOM_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        InjectionCOM_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(InjectionCOM_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        InjectionCOM_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InjectionCOM_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(InjectionCOM_MainWindow)
#################################################################################
        self.COM_comboBox.addItems(self.Port_List())

#################################################################################

    def retranslateUi(self, InjectionCOM_MainWindow):
        InjectionCOM_MainWindow.setWindowTitle(_translate("InjectionCOM_MainWindow", "Set Injection COM", None))
        self.COM_label.setText(_translate("InjectionCOM_MainWindow", "Set COM Port No.", None))
        self.parity_label.setText(_translate("InjectionCOM_MainWindow", "Set Parity No.", None))
        self.baudrate_label.setText(_translate("InjectionCOM_MainWindow", "Set BaudRate No.", None))
        self.stopbits_label.setText(_translate("InjectionCOM_MainWindow", "Set Stop Bits NO.", None))

######################################################################
    def Port_List(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            Com_List.append(port[0])
        return Com_List