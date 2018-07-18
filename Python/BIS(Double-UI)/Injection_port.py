import serial
from time import ctime
from PyQt4 import QtGui


class PortInjection(QtGui.QWidget):

	def __init__(self, parent=None):

		super(PortInjection, self).__init__(parent)

		self.initport()      ##################初始化串口线程###############


###########打开Injection串口##########################################
	def begin(self):
		if self.flag_port_ok:
			self.ser = serial.Serial()
			self.ser.port = self.InjectionCOMport
			self.ser.baudrate = self.InjectionCOMbaudrate
			self.ser.close()
		else:
			pass
		if self.ser.isOpen() == True:
			self.flag_port = False
			self.ser.close()
			self.flag_port_ok = True
		else:
			self.ser.open()
			self.flag_port = True
			self.flag_port_ok = False

###########初始化Injection串口线程#####################################
	def initport(self):
		self.flag_injectionport = False
		self.flag_induction = False
		self.flag_port = False
		self.flag_port_ok = True


###########命令1#####################################
	def command1(self):
		if self.flag_injectionport:
			self.icom1 = 'FF02010101230155'
			self.ICOM1 = bytes.fromhex(self.icom1)
			self.ser.write(self.ICOM1)
		else:
			pass

###########命令2#####################################
	def command2(self):
		if self.flag_injectionport:
			self.icom2 = 'FF02010107890155'
			self.ICOM2 = bytes.fromhex(self.icom2)
			self.ser.write(self.ICOM2)
		else:
			pass






