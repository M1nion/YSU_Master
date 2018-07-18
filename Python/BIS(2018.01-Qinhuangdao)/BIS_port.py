import serial
import threading
import binascii
import struct
import time
from time import ctime
from PyQt4 import QtGui

class PortBis(QtGui.QWidget):

	def __init__(self, parent=None):

		super(PortBis, self).__init__(parent)

		self.initport()      ##################初始化串口线程###############

############SendBIS#########################################
	def SendBIS(self):
		self.flag_VARS = True
		self.flag_Version = False
		self.flag_EEG = False
		self.eegVARS = 'BAAB06000D000100040000007300000004000100009000'
		self.EEGVARS = bytes.fromhex(self.eegVARS)
		self.ser.write(self.EEGVARS)

############StopBIS#########################################
	def StopBIS(self):
		self.eegSTOPVARS = 'BAAB07000C0001000400000074000000050000009100'
		self.EEGSTOPVARS = bytes.fromhex(self.eegSTOPVARS)
		self.ser.write(self.EEGSTOPVARS)
		self.flag_Version = False
		self.flag_VARS = False
		self.flag_EEG = False

############SendEEG#########################################
	def SendEEG(self):
		self.flag_EEG = True
		self.flag_VARS = False
		self.flag_Version = False
		self.eeg = 'BAAB08000E000100040000006F0000000600020080001201'
		self.EEG = bytes.fromhex(self.eeg)
		self.ser.write(self.EEG)

############StopEEG#########################################
	def StopEEG(self):
		self.eegSTOP = 'BAAB09000C0001000400000070000000070000009100'
		self.EEGS = bytes.fromhex(self.eegSTOP)
		self.ser.write(self.EEGS)
		self.flag_Version = False
		self.flag_VARS = False
		self.flag_EEG = False

############SaveEEG#########################################
	def SaveEEG(self):
		localTime_EEG = time.strftime('%Y%m%d%H%M%S', time.localtime())
		file_eeg = open('F:\\BISYSU\\EEG\\EEG' + localTime_EEG + '.txt', 'w+')
		file_eeg.write('EEGch1\tEEGch2\tEEG_MARK\n')
		if self.EEGCH1 != [] and self.EEGCH2 != []:
			for i in range(0, len(self.EEGCH1)):
				file_eeg.write(str(self.EEGCH1[i])  + '\t' + str(self.EEGCH2[i]) + '\t' +self.EEGCH_MARK[i] + '\n')
		else:
			pass
		file_eeg.close()

############SavePatient#########################################
	def SavePatient(self):
		localTime_Patient = time.strftime('%Y%m%d%H%M%S', time.localtime())
		file_patient = open('F:\\BISYSU\\Patient\\Patient' + localTime_Patient + '.txt', 'w+')
		file_patient.write('姓名：' + str(self.nametext) + '\t' + '性别：' + str(self.gendertext) + '\t' + '\t' + '记录日期：' + str(self.datatext) + '\n' \
			+ '身高：' + str(self.heighttext) + '\t' + '体重：' + str(self.weighttext) + '\t' + '\t' + '年龄：' + str(self.agetext))
		file_patient.close()

############SaveBIS#########################################
	def SaveBIS(self):
		file_BIS = open('F:\\BISYSU\\BIS\\BIS'+ self.localTime_BIS +'.txt','w+')
		file_BIS.write("Time\tBIS \n")
		for i in range(0, len(self.BISCH)):
			file_BIS.write(str(self.BISTime[i]) + ':' + '\t' + str(self.BISCH[i])  + '\n')
		file_BIS.close()

############BISPID#########################################
	def BISPID(self):
		self.cefinal = ((self.E0 - self.bisvalue) / self.Emax * (self.EC50 **self.r) / (1 - (self.E0 - self.bisvalue) / self.Emax)) ** (1.00 / self.r)
		self.cefinal = float('%.2f' % self.cefinal)

############接收EEG##########################################
	def GetEEG(self):
		self.eegdata = self.ser.read(2)
		self.eegch, = struct.unpack('h', self.eegdata)
		self.b = binascii.b2a_hex(self.eegdata).decode('ascii').upper()
		if self.flag_savedata:
			if not self.count_i % 2:
				self.eegch = (self.eegch + 3100)*0.05
				self.eegch = float('%.2f' % self.eegch)
				if self.flag_MARK11:
					self.EEGCH_MARK.append('诱导丙')
					self.flag_MARK11 = False
				if self.flag_MARK12:
					self.EEGCH_MARK.append('诱导瑞')
					self.flag_MARK12 = False
				if self.flag_MARK2:
					self.EEGCH_MARK.append('插管')
					self.flag_MARK2 = False
				if self.flag_MARK31:
					self.EEGCH_MARK.append('维持气体')
					self.flag_MARK31 = False
				if self.flag_MARK32:
					self.EEGCH_MARK.append('维持静脉')
					self.flag_MARK32 = False
				if self.flag_MARK4:
					self.EEGCH_MARK.append('手术开始')
					self.flag_MARK4 = False
				if self.flag_MARK5:
					self.EEGCH_MARK.append('电刀')
					self.flag_MARK5 = False
				if self.flag_MARK6:
					self.EEGCH_MARK.append('手术结束')
					self.flag_MARK6 = False
				if self.flag_MARK7:
					self.EEGCH_MARK.append('停药')
					self.flag_MARK7 = False
				if self.flag_MARK8:
					self.EEGCH_MARK.append('浓度识别')
					self.flag_MARK8 = False
				if self.flag_MARK9:
					self.EEGCH_MARK.append('苏醒')
					self.flag_MARK9 = False
				else:
					self.EEGCH_MARK.append(' ')
				self.EEGCH1.append(str(self.eegch))

				if self.flag_online:
					self.EEGCH1_online = str(self.eegch)
					self.flag_onlineTimer = True
					time.sleep(0.01)
				else:
					pass

			else:
				self.eegch = (self.eegch + 3100)*0.05
				self.eegch = float('%.2f' % self.eegch)
				self.EEGCH2.append(str(self.eegch))
		else:
			pass
		if self.b == 'BAAB':
			self.count_i = 0
			self.flag_BAAB = True
		else:
			if self.flag_BAAB:
				self.count_i += 1
				if self.count_i == 6:
					if self.b == '3200':
						self.flag_3200 = True
					else:
						pass
				else:
					pass
				if self.flag_3200:
					if (self.count_i >= 11) and (self.count_i < 43):
						self.flag_savedata = True
					else:
						self.flag_savedata = False
						if self.count_i > 42:
							self.flag_BAAB = False
							self.flag_3200 = False
						else:
							pass
				else:
					pass
			else:
				pass

############接收VARS#########################################
	def GetBIS(self):
		self.localTime_BIS = time.strftime('%Y%m%d%H%M%S',time.localtime())
		self.varsdata = self.ser.read(2)
		self.bisch, = struct.unpack('h', self.varsdata)
		self.c = binascii.b2a_hex(self.varsdata).decode('ascii').upper()
		if self.flag_savedata:
			if len(str(self.bisch)) == 3:
				self.bisvalue = float(str(self.bisch)[0:2] + '.' + str(self.bisch)[-1])

				if self.flag_online:
					self.BISonline = str(self.bisvalue)
					self.flag_onlineTimer = True
				else:
					pass

				if self.flag_warning:
					self.count_warning += 1
					if self.count_warning >= 60:
						self.count_warning = 0
						self.flag_warning = False
					else:
						pass
				else:
					self.bisvalue_warning = self.bisvalue

				self.BISCH.append(str(self.bisch)[0:2] + '.' + str(self.bisch)[-1])
				self.BISTime.append(str(self.localTime_BIS))
				time.sleep(0.01)
			else:
				pass
		else:
			pass
		if self.c == 'BAAB':
			self.count_j = 0
			self.flag_BAAB = True
		else:
			if self.flag_BAAB:
				self.count_j += 1
				if self.count_j == 6:
					if self.c == '3400':
						self.flag_3400 = True
					else:
						pass
				else:
					pass
				if self.flag_3400:
					if self.count_j == 36:
						self.flag_savedata = True
					else:
						self.flag_savedata = False
				else:
					pass
			else:
				pass

############打开串口#########################################
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

		self.port_thread_exit = False
		self.flag_port = False
		self.flag_port_ok = True
############################################################
		self.flag_EEG = False
		self.flag_VARS = False
		self.flag_savedata = False
		self.flag_BAAB = False
		self.flag_3200 = False
		self.flag_3400 = False
		self.flag_online = False
		self.flag_onlineTimer = False
		self.flag_warning = False
############################################################
		self.flag_MARK11 = False
		self.flag_MARK12 = False
		self.flag_MARK2 = False
		self.flag_MARK31 = False
		self.flag_MARK32 = False
		self.flag_MARK4 = False
		self.flag_MARK5 = False
		self.flag_MARK6 = False
		self.flag_MARK7 = False
		self.flag_MARK8 = False
		self.flag_MARK9 = False
############################################################
		self.EEGCH1 = []
		self.EEGCH2 = []
		self.EEGCH1_online = []
		self.BISonline = []
		self.BISCH = []
		self.BISTime = []
		self.EEGCH_MARK = []
		self.nametext = 'xxx'
		self.gendertext = 'x'
		self.datatext = 'xxxx'
		self.weighttext = 'xxx'
		self.heighttext = 'xxx'
		self.agetext = 'xx'
		self.eegdata = ''
		self.count_i = 0
		self.count_j = 0
		self.count_warning = 0
		self.bisvalue_warning = 0
		self.bisvalue = 0
############################################################
		self.bisvalue_expect = 0
		self.E0 = 100
		self.Emax = 100
		self.EC50 = 4.700
		self.r = 3
		self.cefinal = 0
############################################################
		self.t1 = threading.Thread(target=self.port_thread)
		self.t1.start()

###########BIS串口线程############################################
	def port_thread(self):
		print('BIS Port线程运行中 %s' % (ctime()))
		while True:
			if self.port_thread_exit:
				break
			if self.flag_port:
				if self.ser.inWaiting() > 0:
############################SendEEG数据命令#############################################
					if self.flag_EEG:
						self.GetEEG()
############################SendVARS数据命令#############################################
					if self.flag_VARS:
						self.GetBIS()
########################################################################################
					else:
						pass
			else:
				pass
