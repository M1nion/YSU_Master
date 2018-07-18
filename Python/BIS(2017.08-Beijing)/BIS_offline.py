from PyQt4 import QtGui
import struct


class bis_offline(QtGui.QMainWindow):

    def __init__(self, parent=None):

        super(bis_offline, self).__init__(parent)
        self.CH1 = []
        self.CH2 = []

    def Offline(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.fname = open(self.filename, 'rb')
        self.fdata = self.fname.read()
        if not len(self.fdata) % 2:
            for i in range(0, len(self.fdata), 4):
                self.ch1, = struct.unpack('h', self.fdata[i:i + 2])
                self.ch2, = struct.unpack('h', self.fdata[i + 2:i + 4])
                self.ch1 = (self.ch1 + 3100)*0.05
                self.ch2 = (self.ch2 + 3100)*0.05
                self.CH1.append(self.ch1)
                self.CH2.append(self.ch2)
        else:
            for i in range(0, len(self.fdata) - 1, 4):
                self.ch1, = struct.unpack('h', self.fdata[i:i + 2])
                self.ch2, = struct.unpack('h', self.fdata[i + 2:i + 4])
                self.ch1 = (self.ch1 + 3100)*0.05
                self.ch2 = (self.ch2 + 3100)*0.05
                self.CH1.append(self.ch1)
                self.CH2.append(self.ch2)