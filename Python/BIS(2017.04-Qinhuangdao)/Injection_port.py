import serial
import threading
from time import ctime
from PyQt4 import QtGui


class PortInjection(QtGui.QWidget):

	def __init__(self, parent=None):

		super(PortInjection, self).__init__(parent)

		self.initport()      ##################初始化串口线程###############

###########释放Injection串口线程#######################################
	def releasePort(self):
		self.port_thread_exit = True
		self.t1.join()

###########打开Injection串口##########################################
	def begin(self):
		self.ser = serial.Serial()
		self.ser.port = self.InjectionCOMport
		self.ser.baudrate = self.InjectionCOMbaudrate
		self.ser.parity = self.InjectionCOMpartiy
		self.ser.open()
		self.flag_injectionport = True

###########关闭Injection串口##########################################
	def close(self):
		self.ser.close()
		self.flag_injectionport = False

###########初始化Injection串口线程#####################################
	def initport(self):
		self.injectiongdata = ''
		self.flag_injectionport = False
		self.port_thread_exit = False
		self.t1 = threading.Thread(name = "port_thread",target=self.port_thread)
		self.t1.start()

###########Injection串口线程############################################
	def port_thread(self):
		print('Injection Port线程运行中 %s' % (ctime()))
		while True:
			if self.port_thread_exit:
				break
			else:
				pass



