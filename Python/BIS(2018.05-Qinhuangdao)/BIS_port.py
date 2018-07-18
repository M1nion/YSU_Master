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
		self.flag_VARS = False
		self.flag_onlineTimer = False
		self.flag_saveBIS = False
		self.flag_saveEMG = False
		self.flag_saveSQI = False
		self.flag_BAAB = False
		self.flag_3400 = False
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
		self.BISonline = []
		self.BISCH = []
		self.BISTime = []
		self.bisvalue = 0
		self.nametext = 'xxx'
		self.gendertext = 'x'
		self.datatext = 'xxxx'
		self.weighttext = 'xxx'
		self.heighttext = 'xxx'
		self.agetext = 'xx'
		self.MCtext= 'xxx'
###################Control#########################################
		self.bisvalue_expect = 0
############################################################
		self.t1 = threading.Thread(target=self.port_thread)
		self.t1.start()

############接收VARS#########################################
	def GetBIS(self):
		self.localTime_BIS = time.strftime('%Y%m%d%H%M%S', time.localtime())
		self.varsdata = self.ser.read(2)
		self.c = binascii.b2a_hex(self.varsdata).decode('ascii').upper()

		if self.flag_saveBIS:
			self.bisch, = struct.unpack('h', self.varsdata)
			self.bisvalue = float(str(self.bisch)[0:2] + '.' + str(self.bisch)[-1])  #######计算控制时使用#######
			if len(str(self.bisch)) == 3 and self.bisvalue >= 30:
				self.flag_onlineTimer = True
				self.BISonline = str(self.bisvalue)
				self.BISCH.append(str(self.bisch)[0:2] + '.' + str(self.bisch)[-1])
				self.BISTime.append(str(self.localTime_BIS))
				time.sleep(0.01)  #############这种方式肯定是有很大的问题的，希望有一天能找到更好的解决方案#############
			else:
				pass
		elif self.flag_saveEMG:
			self.emgch, = struct.unpack('h', self.varsdata)
			if len(str(self.emgch)) == 4:
				self.emgvalue = float(str(self.emgch)[0:2] + '.' + str(self.emgch)[-2] + str(self.emgch)[-1])
			elif len(str(self.emgch)) == 3:
				self.emgvalue = float(str(self.emgch)[0] + '.' + str(self.emgch)[-2] + str(self.emgch)[-1])
			else:
				pass
		elif self.flag_saveSQI:
			self.sqich, = struct.unpack('h', self.varsdata)
			if len(str(self.sqich)) == 2:
				self.sqivalue = float(str(self.sqich)[0] + '.' + str(self.sqich)[-1])
			elif len(str(self.sqich)) == 3:
				self.sqivalue = float(str(self.sqich)[0:2] + '.' + str(self.sqich)[-1])
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
						self.flag_saveBIS = True
						self.flag_saveEMG = False
						self.flag_saveSQI = False
					elif self.count_j == 40:
						self.flag_saveEMG = True
						self.flag_saveBIS = False
						self.flag_saveSQI = False
					elif self.count_j == 41:
						self.flag_saveSQI = True
						self.flag_saveBIS = False
						self.flag_saveEMG = False
					else:
						self.flag_saveBIS = False
						self.flag_saveEMG = False
						self.flag_saveSQI = False
				else:
					pass
			else:
				pass


###########BIS串口线程############################################
	def port_thread(self):
		print('BIS Port线程运行中 %s' % (ctime()))
		while True:
			if self.port_thread_exit:
				break
			if self.flag_port:
				if self.ser.inWaiting() > 0:
############################SendBIS数据命令#############################################
					if self.flag_VARS:
						self.GetBIS()
########################################################################################
					else:
						pass
				else:
					pass
			else:
				pass
