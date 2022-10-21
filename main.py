import sys
import sqlite3
import nfc
from sqlite3 import Error

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def clickbutton():
	b.setText("scanning...")
	#b.adjustSize()
	cursor = c.execute("SELECT ID, NAME from BITCH")
	object = QLabel()
	object.setText("holy shit")
	object.setStyleSheet("color: black;")
	vbox.addWidget(object)
	

def create_connection(path):
	co = None
	try:
		co = sqlite3.connect(path)
		print("successful connection to DB")
	except Error as e:
		print("calamity!: '{e}'")
	return co

def launchWindow():
	clf = nfc.ContactlessFrontend()
	res = clf.open('usb')
	if res == True:
		print("a nfc reader was found")
	else:
		print("did not find a reader")
	app = QApplication(sys.argv)
	global c
	c = create_connection('test.db')
	c.execute('''CREATE TABLE IF NOT EXISTS BITCH(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);''')

	c.execute('''INSERT OR IGNORE INTO BITCH (ID,NAME) VALUES(1, 'Jimmy')''')
	print("added stuff to db")
	c.commit()


	w = QWidget()
	x = QWidget()
	y = QWidget()
	outerL = QHBoxLayout()
	listpanel = QScrollArea()
	actionpanel = QVBoxLayout()
	global vbox
	vbox = QVBoxLayout()
	

	
	#a.move(50,20)
	
	x.setLayout(vbox)
	word = QLabel("HELLO MF")
	word.setStyleSheet("color:black")
	vbox.addWidget(word)
	#x.adjustSize()


	w.setStyleSheet("background-color: white;")
	global b 
	b = QLabel()
	b.setStyleSheet("color: black;")
	f = QFont()
	f.setFamily("Times")
	f.setPointSize(40)

	b.setFont(f)
	b.setText("PROJECT ION")
	b.move(50,20)

	w.setGeometry(500,500,800,800)
	
	b1 = QPushButton(w)
	b1.setText("SCAN")
	b1.setFont(f)
	b1.setStyleSheet("border-width: 5px; border-style: outset; color: black; border-color: white; border-radius: 20px; padding:20px;")
	b1.move(20,200)
	b1.clicked.connect(clickbutton)
	#vbox.addWidget(b)
	

	listpanel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	listpanel.setWidgetResizable(True)

	listpanel.setWidget(x)
	#listpanel.adjustSize()

	actionpanel.addWidget(b)
	actionpanel.addWidget(b1)
	outerL.addWidget(listpanel, 8)
	#outerL.addLayout(vbox)
	outerL.addLayout(actionpanel, 2)
	w.setLayout(outerL)

	
	w.setWindowTitle("ION v1.0")
	w.show()
	
	sys.exit(app.exec_())




if __name__ == '__main__':
	launchWindow()



