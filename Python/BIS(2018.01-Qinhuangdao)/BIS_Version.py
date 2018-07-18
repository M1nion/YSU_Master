# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Version.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class BISVersion(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(BISVersion, self).__init__(parent)
        self.setupUi_Version(self)
    def setupUi_Version(self, Version_MainWindow):
        Version_MainWindow.setObjectName(_fromUtf8("Version_MainWindow"))
        Version_MainWindow.resize(313, 289)
#############################################################################
        Version_MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
#############################################################################
        self.centralwidget = QtGui.QWidget(Version_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Version_label_2 = QtGui.QLabel(self.centralwidget)
        self.Version_label_2.setGeometry(QtCore.QRect(0, 100, 301, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Version_label_2.setFont(font)
        self.Version_label_2.setObjectName(_fromUtf8("Version_label_2"))
        self.Version_label = QtGui.QLabel(self.centralwidget)
        self.Version_label.setGeometry(QtCore.QRect(0, 60, 311, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Version_label.setFont(font)
        self.Version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Version_label.setObjectName(_fromUtf8("Version_label"))
        Version_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Version_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Version_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Version_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Version_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Version_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Version_MainWindow)

    def retranslateUi(self, Version_MainWindow):
        Version_MainWindow.setWindowTitle(_translate("Version_MainWindow", "BIS Version", None))
        self.Version_label_2.setText(_translate("Version_MainWindow", "               by YSU.Automation", None))
        self.Version_label.setText(_translate("Version_MainWindow", "  Version 1.0(for VISTA)programmed", None))

