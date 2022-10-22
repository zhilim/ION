import sys
import sqlite3
from ctypes import *
import os
#from sqlite3 import Error

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Constants, ErrCodes
import threading
import time

class NFC():

	def __init__(self):
		super().__init__()
		self.init_NFC()
		

	def init_NFC(self):
	
 		self.CONN = False
 		self.readerON = False
 		self.functionOn = False
 		self.DLogicCardType = c_int()

 		self.scanning = False
 		self.writing = False
 		self.committing = False
 		self.scannedArray = []
 		a = os.getcwd()
 		b = "ufr-lib"
 		c = "windows"
 		d = "x86_64"
 		e = "uFCoder-x86_64.dll"


 		self.mySO = windll.LoadLibrary(os.path.join(a,b,c,d,e))

 		t = threading.Thread(target=self.threadstart)
 		t.daemon = True
 		t.start()
	
	def setScanningStatus(self, truth):
		self.scanning = truth

	def setWritingStatus(self, truth):
		self.writing = truth

	def setCommitStatus(self, truth):
		self.committing = truth

	def threadstart(self):
		while True:
			#print("connection daemon is running")
			self.connectReader()
			time.sleep(interval)

	def ReaderUISignal(self, lightValue, soundValue):
		uis = self.mySO.ReaderUISignal
		uis.argtypes = (c_uint8, c_uint8)
		uis.restype = c_int
		uis(lightValue, soundValue)

	def goodlight():
		self.ReaderUISignal(Constants.FUNCT_LIGHT_OK, Constants.FUNCT_SOUND_OK)
	
	def wipecard(self):
		word.setText("Wiping old data...")
		b.setText("Formatting")
		blockCount = 0
		keyIndex = 0
		pData = POINTER(c_uint8)
		blockData = (c_int8 * Constants.MAX_BLOCK)()
		maxBlock = Constants.MaxBlock(self.DLogicCardType.value)
		fResult = 0

		memset(blockData, Constants.FORMAT_SIGN, Constants.MAX_BLOCK)

		pData = byref(blockData)

		while blockCount<maxBlock:
			fResult = self.mySO.BlockWrite(pData, blockCount, Constants.MIFARE_AUTHENT1A, keyIndex)
			blockCount += 1
		return fResult



	def connectReader(self):
		#print("im here")
		#print(connected)
		if self.functionOn : return


		readerType = c_int32()
		cardType = c_uint8()
		cardUIDSize = c_uint8()
		cardUID = (c_ubyte*9)()
		c = str()

		try:
			#print("checking connected")
			self.readerON = True
			if self.CONN != True:
		
				#print("attempt opening reader")
				fResult = self.mySO.ReaderOpen()
				if fResult == Constants.DL_OK:
					print("Successful connection to UFR XL READER")
					#prompt.setText("Reader detected, pls wait")
					#print(fResult)
					self.CONN = True
				else:
					prompt.setText("Plug in the reader..")
					prompt.adjustSize()
					self.CONN = False
			if self.CONN:
				fResult = self.mySO.GetReaderType(byref(readerType))
				#print("got reader type")
				#print(hex(readerType.value))
				if fResult == Constants.DL_OK:
					fResult = self.mySO.GetDlogicCardType(byref(self.DLogicCardType))

					if fResult == Constants.DL_OK:
						prompt.setText("NFC detected, system linked")
						#print(hex(self.DLogicCardType.value))
						fResult = self.mySO.GetCardIdEx(byref(cardType), cardUID, byref(cardUIDSize))
						if fResult == Constants.DL_OK:
							#print("got some card info")
							#print(cardUIDSize.value)
							for n in range(cardUIDSize.value):
								c +=  '%0.2x' % cardUID[n]
							print(c)
							if self.scanning or self.writing:
								dataLength = (Constants.MaxBytes(self.DLogicCardType.value))
								dataValue = (c_uint8*dataLength)()
								byRet = c_uint16()

								fResult = self.mySO.LinearRead((dataValue), 0, dataLength, byref(byRet), Constants.MIFARE_AUTHENT1A, 0)
								if fResult == Constants.DL_OK:
									li = [chr(i) for i in dataValue]
									if self.writing:

										readtagforwrite(c, ''.join(li))
										if self.committing:
											sexresult = self.wipecard()
											if sexresult != Constants.DL_OK:
												word.setText("formatting failed.")
												b.setText("formatting failed")
												return
											toWrite = whatuwrite.toPlainText()
											if not toWrite.strip():
												toWrite = "empty"
											toBytes = str.encode(toWrite)
											dlength = len(toWrite)
											byRet2 = c_uint16()
											fResult = self.mySO.LinearWrite(toBytes, 0, dlength, byref(byRet2), Constants.MIFARE_AUTHENT1A,0)
											if fResult == Constants.DL_OK:
												self.ReaderUISignal(Constants.FUNCT_LIGHT_OK, Constants.FUNCT_SOUND_OK)
												word.setText("COMMIT SUCCESSFUL")
												b.setText("COMMITTED")
												self.committing = False;

									if self.scanning:
										self.ReaderUISignal(Constants.FUNCT_LIGHT_OK, Constants.FUNCT_SOUND_OK)
										multireadcard(c, ''.join(li))

					else:
						prompt.setText("Reader detected, ION ready")
						if self.writing:
							removenfcinfo()
						if self.committing:
							self.committing = False
							word.setText("NFC removed before successful commit")
							b.setText("Commit failed due NFC removed")


		finally:
			self.readerON = False


def readtagforwrite(u_id, content):
	b.setText("WRITE MODE")
	word.setText("WRITING TO NFC TAG: ")
	word.adjustSize()
	spacearray[0].setText("UID [" + u_id + "] Previous Content: \n" + content)
	spacearray[0].adjustSize()
	x.adjustSize()
	b5.show()


def multireadcard(u_id, content):
	unique = True
	if len(u_id) < 5:
		return
	for i in uidarray:
		#print(i.text())
		if i == u_id:
			unique = False

	if unique:
		print("unique id detected, adding to array")
		signoutname.show()
		b2.show()
		uidarray.append(u_id)
		contentarray.append(content)
		word.setText(str(len(uidarray))+ " classifieds scanned")
		word.adjustSize()
		
		tempi = None
		for rec in records:
			if rec[0] == u_id:
				tempi = rec[1]

		for n in spacearray:
			
			if n.text() == "":
				txt = content + " detected, uid " + u_id
				if tempi != None:
					txt += "\n drawn by " + tempi
				else:
					txt += "status: not drawn"
				n.setText(txt)
				n.adjustSize()
				break
		x.adjustSize()


def commitwrite():

	print(whatuwrite.toPlainText())
	word.setText("COMMITTING, DO NOT MOVE NFC")
	word.adjustSize()
	b.setText("COMMITTING")
	b.adjustSize()
	myNFC.setCommitStatus(True)

def signin():
	print("signing in")


def signout():
	#print(signoutname.text())
	word.setText("Signing Out")
	counter = 0
	nm = signoutname.text()
	for i in uidarray:
		print("inserting " + contentarray[counter])
		query = '''INSERT OR IGNORE INTO SIGNEDOUT(UID, NAME, CONTENT) VALUES (?, ?, ?)'''
		data = [i, nm, contentarray[counter]]
		c.execute(query, data)
		records.append([i, nm])
		counter += 1
	c.commit()	
	word.setText("Signed Out as " + nm)

	for n in spacearray:
		n.setText("")
		n.adjustSize()
	uidarray.clear()
	contentarray.clear()
	signoutname.hide()
	b2.hide()

def viewClassifieds():
	b1.hide()
	b3.hide()
	b7.hide()
	b8.show()
	b.setText("Records")
	word.setText("The following assets have been signed out")
	cursor = c.execute('''SELECT UID, NAME, CONTENT from SIGNEDOUT''')
	#print(len(cursor))
	counter = 0
	for row in cursor:
		print("extracting #" + str(counter+1))
		uid = row[0]
		name = row[1]
		content = row[2]
		txt = content + " signed out by " + name + "\nUID: " + uid
		spacearray[counter].setText(txt)
		spacearray[counter].adjustSize()
		x.adjustSize()
		counter+=1

def outofview():
	b1.show()
	b3.show()
	b7.show()
	b8.hide()
	b.setText("Project Ion")
	word.setText("0 classifieds scanned")
	for n in spacearray:
		n.setText("")
		n.adjustSize()

def writemode():
	interval = 0.1
	myNFC.setWritingStatus(True)
	b1.hide()
	b3.hide()
	b7.hide()
	#b5.show()
	b6.show()
	whatuwrite.show()

def cancelwrite():
	myNFC.setWritingStatus(False)
	b1.show()
	b3.show()
	b5.hide()
	b6.hide()
	b7.show()
	spacearray[0].setText("")
	spacearray[0].adjustSize()
	whatuwrite.hide()


def clickbutton():
	global records
	records = []
	recor = c.execute('''SELECT UID, NAME from SIGNEDOUT''')
	for row in recor:
		records.append([row[0], row[1]])
	b.setText("SCAN MODE")
	#signoutname.show()
	myNFC.setScanningStatus(True)
	interval = 0.05
	#b1.setText("Cancel")
	#b1.clicked.connect(unclickbutton)
	b1.hide()
	#b2.show()
	b3.hide()
	b4.show()
	b7.hide()
	#b.adjustSize()
	#cursor = c.execute("SELECT ID, NAME from BITCH")
	#object = QLabel()
	#object.setText("holy shit")
	#object.setStyleSheet("color: black;")
	#vbox.addWidget(object)

def unclickbutton():
	b.setText("Project ION")
	interval = 0.6
	myNFC.setScanningStatus(False)
	signoutname.hide()
	b1.show()
	word.setText("0 classifieds scanned")
	word.adjustSize()
	uidarray.clear()
	contentarray.clear()
	for n in spacearray:
		n.setText("")
		n.adjustSize()
	b2.hide()
	b3.show()
	b4.hide()
	b7.show()

def removenfcinfo():
	word.setText("No Tags to Write")
	word.adjustSize()
	b.setText("Project Ion")
	spacearray[0].setText("")
	spacearray[0].adjustSize()
	b5.hide()


def create_connection(path):
	co = None
	try:
		co = sqlite3.connect(path)
		print("successful connection to DB")
	except Error as e:
		print("calamity!: '{e}'")
	return co


def launchWindow():
	
	global interval
	interval = 0.6
	global myNFC
	global spacearray
	global uidarray
	global tagtowrite
	global contentarray
	uidarray = []
	spacearray = []
	contentarray = []
	app = QApplication(sys.argv)

	global whatuwrite
	whatuwrite = QTextEdit()
	global c
	c = create_connection('test.db')
	c.execute('''DROP TABLE IF EXISTS SIGNEDOUT''')
	c.execute('''CREATE TABLE IF NOT EXISTS SIGNEDOUT(UID TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, CONTENT TEXT NOT NULL);''')

	#c.execute('''INSERT OR IGNORE INTO BITCH (ID,NAME) VALUES(1, 'Jimmy')''')
	#print("added stuff to db")
	c.commit()


	w = QWidget()
	global x
	x = QWidget()
	y = QWidget()
	outerL = QHBoxLayout()
	listpanel = QScrollArea()
	global actionpanel
	actionpanel = QVBoxLayout()
	global vbox
	vbox = QVBoxLayout()
	

	
	#a.move(50,20)
	
	x.setLayout(vbox)
	global word
	word = QLabel("0 classifieds scanned")

	word.setStyleSheet("color:black;")
	vbox.addWidget(word)
	global signoutname
	signoutname = QLineEdit()
	signoutname.setPlaceholderText("SIGN HERE")
	for space in range(10):
		sp = QLabel("")
		sp.setStyleSheet("color:black;")
		vbox.addWidget(sp)
		spacearray.append(sp)

	#x.adjustSize()


	w.setStyleSheet("background-color: white;")
	global b 
	b = QLabel()
	b.setStyleSheet("color: black;")
	f = QFont("Times", 26)
	#f.setFamily("Serif")
	#f.setPointSize(26)

	b.setFont(f)
	b.setText("Project ION")
	b.setFont(f)
	b.move(50,20)

	w.setGeometry(500,50,1200,800)
	
	global b1
	b1 = QPushButton(w)
	b1.setText("Scan")
	#b1.setFont(f)
	#b1.setStyleSheet("border-width: 5px; border-style: outset; color: black; border-color: white; border-radius: 20px; padding:20px;")
	#b1.move(20,200)
	b1.clicked.connect(clickbutton)
	#vbox.addWidget(b)

	global b2
	b2 = QPushButton(w)
	b2.setText("Sign Out")
	b2.clicked.connect(signout)

	global b4
	#cancel scan
	b4 = QPushButton(w)
	b4.setText("Cancel")
	b4.clicked.connect(unclickbutton)

	global b6
	#cancel write
	b6 = QPushButton(w)
	b6.setText("Cancel")
	b6.clicked.connect(cancelwrite)

	global b5
	b5 = QPushButton(w)
	b5.setText("Commit")
	b5.clicked.connect(commitwrite)

	global prompt
	prompt = QLabel()
	prompt.setStyleSheet("color: black;")
	prompt.setText("No NFC Detected")
	f.setPointSize(16)
	prompt.setFont(f)
	signoutname.setFont(f)

	global b3
	b3 = QPushButton(w)
	b3.setText("Write")
	b3.clicked.connect(writemode)

	global b7
	b7 = QPushButton(w)
	b7.setText("View")
	b7.clicked.connect(viewClassifieds)

	global b8
	b8 = QPushButton(w)
	b8.setText("Back")
	b8.clicked.connect(outofview)

	global b9
	b9 = QPushButton(w)
	b9.setText("Sign In")
	b9.clicked.connect(signin)

	listpanel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	listpanel.setWidgetResizable(True)

	listpanel.setWidget(x)
	#listpanel.adjustSize()

	actionpanel.addWidget(b)
	actionpanel.addWidget(prompt)
	actionpanel.addWidget(signoutname)
	actionpanel.addWidget(whatuwrite)
	
	actionpanel.addWidget(b7)
	actionpanel.addWidget(b8)
	actionpanel.addWidget(b2)
	actionpanel.addWidget(b1)
	actionpanel.addWidget(b3)
	actionpanel.addWidget(b4)
	actionpanel.addWidget(b5)
	actionpanel.addWidget(b6)
	actionpanel.addWidget(b9)

	b9.hide()
	b8.hide()
	b6.hide()
	b4.hide()
	b5.hide()
	whatuwrite.hide()
	signoutname.hide()
	b2.hide()
	outerL.addWidget(listpanel, 8)
	#outerL.addLayout(vbox)
	outerL.addLayout(actionpanel, 2)
	w.setLayout(outerL)

	myNFC = NFC()
	w.setWindowTitle("ION v1.0")
	w.show()
	
	sys.exit(app.exec_())




if __name__ == '__main__':
	
	launchWindow()



