import serial
import serial.tools.list_ports
import threading
import binascii
import struct
from time import ctime,sleep
from PyQt4 import QtGui

class PortBis(QtGui.QWidget):

	def __init__(self, parent=None):

		super(PortBis, self).__init__(parent)
		self.initport()      ##################初始化串口线程###############

############OpenVersion#########################################
	def OpenVersion(self):
		self.eegVersion = 'BAAB05000C00010006000000EC030000030000000A01'
		self.EEGV = bytes.fromhex(self.Version)
		self.ser.write(self.EEGV)
		self.flag_showMessage = True

############SendEEG#########################################
	def SendEEG(self):
		self.flag_EEG = True
		self.flag_showMessage = False
		self.eeg = 'BAAB06000E000100040000006F0000000400020080000E01'
		self.EEG = bytes.fromhex(self.eeg)
		self.ser.write(self.EEG)

############StopEEG#########################################
	def StopEEG(self):
		self.eegSTOP = 'BAAB07000C000100040000007000000005000000008D'
		self.EEGS = bytes.fromhex(self.eegSTOP)
		self.ser.write(self.EEGS)
		self.flag_EEG = False

############StopEEG#########################################
	def SaveEEG(self):
		f = open("F:/EEGDATA.txt", "w+")
		f.write("EEGch1\tEEGch2\n")
		for i in range(0, len(self.EEGCH1)):
			f.write(str(self.EEGCH1[i]) + "\t" + str(self.EEGCH2[i]) + '\n')
		f.close()

############开始绘图#########################################
	def begin(self):
		if self.flag_port_ok:
			self.ser = serial.Serial()
			self.ser.port = self.COMport
			self.ser.baudrate = self.COMbaudrate
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

###########释放串口线程#######################################
	def releasePort(self):
		self.port_thread_exit = True
		self.t1.join()

###########初始化串口线程#####################################
	def initport(self):
		self.flag_port = False
		self.flag_port_ok = True
		self.flag_EEG = False
		self.port_thread_exit =False
		self.flag_savedata = False
		self.flag_BAAB = False
		self.flag_5000 = False
		self.flag_showMessage = False

		self.EEGCH1 = []
		self.EEGCH2 = []
		self.eegdata = ''
		self.data = ''
		self.eegch1 = ''
		self.eegch2 = ''
		self.hexdata = ''
		self.t1 = threading.Thread(name = "port_thread",target=self.port_thread)
		self.t1.start()

###########串口线程############################################
	def port_thread(self):
		print('串口线程运行中 %s' % (ctime()))
		while True:
			if self.port_thread_exit:
				break
			if self.flag_port:
				if self.ser.inWaiting() > 0:
############################OpenEEG#############################################
					if self.flag_EEG:
						self.eegdata = self.ser.read(2)
						self.eegch, = struct.unpack('h', self.eegdata)
						self.b = binascii.b2a_hex(self.eegdata).decode('ascii').upper()
						if self.flag_savedata:
							if not self.count_i % 2:
								#print(self.eegch)
								self.eegch = self.eegch + 3000
								self.eegch1 += str(self.eegch) + ','
								self.EEGCH1.append(self.eegch)
							else:
								self.eegch = self.eegch + 3000
								self.eegch2 = str(self.eegch)
								self.EEGCH2.append(self.eegch)
								#print(self.eegch)
						else:
							pass
						if self.b == 'BAAB':
							self.count_i = 0
							self.flag_BAAB = True
						else:
							if self.flag_BAAB:
								self.count_i += 1
								if self.count_i == 2:
									if self.b == '5000':
										self.flag_5000 = True
										#print('楠哥好nb')
									else:
										pass
								else:
									pass
								if self.flag_5000:
									if (self.count_i >= 11) and (self.count_i < 43):
										self.flag_savedata = True
									# print(self.count_i)
									else:
										self.flag_savedata = False
										if self.count_i > 42:
											self.flag_BAAB = False
											self.flag_5000 = False
										else:
											pass
								else:
									pass
							else:
								pass
############################OpenEEG#############################################
					else:
						if self.flag_showMessage:
							self.data = self.ser.read(self.ser.inWaiting())
							if not len(self.data) % 2:
								self.data = binascii.b2a_hex(self.data)
								self.data = self.data.decode('ascii')
								m = len(self.data)
								data_i = 1
								while data_i <= m:
									self.hexdata = self.hexdata + self.data[data_i - 1:data_i + 1] + ' '
									self.hexdata = self.hexdata.upper()
									data_i = data_i + 2
							else:
								print('字符串个数不正确！')
						else:
							pass
			pass