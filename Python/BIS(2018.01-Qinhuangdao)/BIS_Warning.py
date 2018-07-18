# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BISWarning.ui'
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

class BISWarning(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(BISWarning, self).__init__(parent)
        self.setupUi_Warning(self)
    def setupUi_Warning(self, Waring_MainWindow):
        Waring_MainWindow.setObjectName(_fromUtf8("Waring_MainWindow"))
        Waring_MainWindow.resize(313, 115)
#############################################################################
        Waring_MainWindow.setWindowIcon(QtGui.QIcon('燕山大学.jpg'))  # 设置窗体图标
#############################################################################
        self.centralwidget = QtGui.QWidget(Waring_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Version_label_2 = QtGui.QLabel(self.centralwidget)
        self.Version_label_2.setGeometry(QtCore.QRect(0, 40, 301, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Version_label_2.setFont(font)
        self.Version_label_2.setObjectName(_fromUtf8("Version_label_2"))
        self.Version_label = QtGui.QLabel(self.centralwidget)
        self.Version_label.setGeometry(QtCore.QRect(0, 10, 311, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Version_label.setFont(font)
        self.Version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Version_label.setObjectName(_fromUtf8("Version_label"))
        Waring_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Waring_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Waring_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Waring_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Waring_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Waring_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Waring_MainWindow)

    def retranslateUi(self, Waring_MainWindow):
        Waring_MainWindow.setWindowTitle(_translate("Waring_MainWindow", "Warning", None))
        self.Version_label_2.setText(_translate("Waring_MainWindow", "          BIS Value is higher than 60 !", None))
        self.Version_label.setText(_translate("Waring_MainWindow", "Waring ! ! !", None))

