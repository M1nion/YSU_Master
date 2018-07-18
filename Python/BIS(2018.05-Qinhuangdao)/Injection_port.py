import serial
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
		self.PIDSpeed = 0
		self.ManSpeed = 0
		self.ICOM_SET = "00000000"
		self.flag_ICOM = False
		self.flag_port = False
		self.flag_port_ok = True

###########注射泵参数预设#####################################
	def ParaSet(self):
		if self.flag_ICOM:
			self.icom_paras = self.ICOM_SET
			self.ICOM_Paras = bytes.fromhex(self.icom_paras)
			self.ser.write(self.ICOM_Paras)
		else:
			pass

###########注射泵启动#####################################
	def Injectport_start(self):
		if self.flag_ICOM:
			self.icom_start = '55AA0504012100D5'
			self.ICOM_Start = bytes.fromhex(self.icom_start)
			self.ser.write(self.ICOM_Start)
		else:
			pass

###########注射泵停止#####################################
	def Injectport_stop(self):
		if self.flag_ICOM:
			self.icom_stop = '55AA0504012200D4'
			self.ICOM_Stop = bytes.fromhex(self.icom_stop)
			self.ser.write(self.ICOM_Stop)
		else:
			pass






