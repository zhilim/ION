# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uFSimplestForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 452)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblCardType = QtWidgets.QLabel(self.centralwidget)
        self.lblCardType.setGeometry(QtCore.QRect(40, 37, 60, 13))
        self.lblCardType.setObjectName("lblCardType")
        self.txtCardType = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardType.setGeometry(QtCore.QRect(107, 34, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardType.setFont(font)
        self.txtCardType.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardType.setReadOnly(True)
        self.txtCardType.setObjectName("txtCardType")
        self.txtUIDSize = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUIDSize.setGeometry(QtCore.QRect(237, 34, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtUIDSize.setFont(font)
        self.txtUIDSize.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUIDSize.setReadOnly(True)
        self.txtUIDSize.setObjectName("txtUIDSize")
        self.lblUIDSize = QtWidgets.QLabel(self.centralwidget)
        self.lblUIDSize.setGeometry(QtCore.QRect(170, 37, 60, 13))
        self.lblUIDSize.setObjectName("lblUIDSize")
        self.txtCardUID = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardUID.setGeometry(QtCore.QRect(107, 58, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardUID.setFont(font)
        self.txtCardUID.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardUID.setReadOnly(True)
        self.txtCardUID.setObjectName("txtCardUID")
        self.lblCardSize = QtWidgets.QLabel(self.centralwidget)
        self.lblCardSize.setGeometry(QtCore.QRect(40, 61, 60, 13))
        self.lblCardSize.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCardSize.setObjectName("lblCardSize")
        self.btnFormatCard = QtWidgets.QPushButton(self.centralwidget)
        self.btnFormatCard.setGeometry(QtCore.QRect(309, 30, 241, 51))
        self.btnFormatCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFormatCard.setObjectName("btnFormatCard")
        self.lblLinearRead = QtWidgets.QLabel(self.centralwidget)
        self.lblLinearRead.setGeometry(QtCore.QRect(40, 90, 70, 13))
        self.lblLinearRead.setObjectName("lblLinearRead")
        self.txtLinearRead = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLinearRead.setGeometry(QtCore.QRect(40, 110, 241, 181))
        self.txtLinearRead.setReadOnly(True)
        self.txtLinearRead.setObjectName("txtLinearRead")
        self.lblLinearWrite = QtWidgets.QLabel(self.centralwidget)
        self.lblLinearWrite.setGeometry(QtCore.QRect(310, 90, 70, 13))
        self.lblLinearWrite.setObjectName("lblLinearWrite")
        self.txtLinearWrite = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLinearWrite.setGeometry(QtCore.QRect(310, 110, 241, 181))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 160, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.txtLinearWrite.setPalette(palette)
        self.txtLinearWrite.setObjectName("txtLinearWrite")
        self.btnLinearRead = QtWidgets.QPushButton(self.centralwidget)
        self.btnLinearRead.setGeometry(QtCore.QRect(40, 295, 241, 51))
        self.btnLinearRead.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLinearRead.setObjectName("btnLinearRead")
        self.btnLinearWrite = QtWidgets.QPushButton(self.centralwidget)
        self.btnLinearWrite.setGeometry(QtCore.QRect(310, 295, 241, 51))
        self.btnLinearWrite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLinearWrite.setObjectName("btnLinearWrite")
        self.pBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pBar.setEnabled(False)
        self.pBar.setGeometry(QtCore.QRect(41, 351, 510, 10))
        self.pBar.setProperty("value", 0)
        self.pBar.setTextVisible(False)
        self.pBar.setObjectName("pBar")
        self.txtConnected = QtWidgets.QLineEdit(self.centralwidget)
        self.txtConnected.setGeometry(QtCore.QRect(0, 410, 151, 20))
        self.txtConnected.setAlignment(QtCore.Qt.AlignCenter)
        self.txtConnected.setReadOnly(True)
        self.txtConnected.setObjectName("txtConnected")
        self.txtConnErrorValue = QtWidgets.QLineEdit(self.centralwidget)
        self.txtConnErrorValue.setGeometry(QtCore.QRect(151, 410, 50, 20))
        self.txtConnErrorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.txtConnErrorValue.setReadOnly(True)
        self.txtConnErrorValue.setObjectName("txtConnErrorValue")
        self.txtConnErrorMsg = QtWidgets.QLineEdit(self.centralwidget)
        self.txtConnErrorMsg.setGeometry(QtCore.QRect(201, 410, 390, 20))
        self.txtConnErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.txtConnErrorMsg.setReadOnly(True)
        self.txtConnErrorMsg.setObjectName("txtConnErrorMsg")
        self.txtCardErrorMsg = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardErrorMsg.setGeometry(QtCore.QRect(201, 390, 390, 20))
        self.txtCardErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardErrorMsg.setReadOnly(True)
        self.txtCardErrorMsg.setObjectName("txtCardErrorMsg")
        self.txtCardErrorValue = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardErrorValue.setGeometry(QtCore.QRect(151, 390, 50, 20))
        self.txtCardErrorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardErrorValue.setReadOnly(True)
        self.txtCardErrorValue.setObjectName("txtCardErrorValue")
        self.txtCardStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardStatus.setGeometry(QtCore.QRect(0, 390, 151, 20))
        self.txtCardStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardStatus.setObjectName("txtCardStatus")
        self.txtFunctErrorMsg = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFunctErrorMsg.setGeometry(QtCore.QRect(201, 370, 390, 20))
        self.txtFunctErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFunctErrorMsg.setReadOnly(True)
        self.txtFunctErrorMsg.setObjectName("txtFunctErrorMsg")
        self.txtFuncErrorValue = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFuncErrorValue.setGeometry(QtCore.QRect(151, 370, 50, 20))
        self.txtFuncErrorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFuncErrorValue.setReadOnly(True)
        self.txtFuncErrorValue.setObjectName("txtFuncErrorValue")
        self.txtFunctError = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFunctError.setGeometry(QtCore.QRect(0, 370, 151, 20))
        self.txtFunctError.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFunctError.setReadOnly(True)
        self.txtFunctError.setObjectName("txtFunctError")
        self.linkLabel = QtWidgets.QLabel(self.centralwidget)
        self.linkLabel.setGeometry(QtCore.QRect(40, 4, 261, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.linkLabel.setFont(font)
        self.linkLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.linkLabel.setAutoFillBackground(True)
        self.linkLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.linkLabel.setOpenExternalLinks(False)
        self.linkLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.linkLabel.setObjectName("linkLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.mnuExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.mnuExit.setFont(font)
        self.mnuExit.setObjectName("mnuExit")
        self.menuFile.addAction(self.mnuExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.mnuExit.triggered.connect(MainWindow.close)
        self.btnFormatCard.clicked.connect(self.txtLinearWrite.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtLinearWrite, self.btnLinearWrite)
        MainWindow.setTabOrder(self.btnLinearWrite, self.btnLinearRead)
        MainWindow.setTabOrder(self.btnLinearRead, self.txtLinearRead)
        MainWindow.setTabOrder(self.txtLinearRead, self.txtCardType)
        MainWindow.setTabOrder(self.txtCardType, self.txtUIDSize)
        MainWindow.setTabOrder(self.txtUIDSize, self.txtCardUID)
        MainWindow.setTabOrder(self.txtCardUID, self.txtConnected)
        MainWindow.setTabOrder(self.txtConnected, self.txtConnErrorValue)
        MainWindow.setTabOrder(self.txtConnErrorValue, self.txtConnErrorMsg)
        MainWindow.setTabOrder(self.txtConnErrorMsg, self.txtCardErrorMsg)
        MainWindow.setTabOrder(self.txtCardErrorMsg, self.txtCardErrorValue)
        MainWindow.setTabOrder(self.txtCardErrorValue, self.txtCardStatus)
        MainWindow.setTabOrder(self.txtCardStatus, self.txtFunctErrorMsg)
        MainWindow.setTabOrder(self.txtFunctErrorMsg, self.txtFuncErrorValue)
        MainWindow.setTabOrder(self.txtFuncErrorValue, self.txtFunctError)
        MainWindow.setTabOrder(self.txtFunctError, self.btnFormatCard)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "uFCoder Simplest"))
        self.lblCardType.setText(_translate("MainWindow", "Card Type"))
        self.lblUIDSize.setText(_translate("MainWindow", "UID Size"))
        self.lblCardSize.setText(_translate("MainWindow", "Card UID"))
        self.btnFormatCard.setText(_translate("MainWindow", "FORMAT CARD"))
        self.lblLinearRead.setText(_translate("MainWindow", "Linear Read"))
        self.lblLinearWrite.setText(_translate("MainWindow", "Linear Write"))
        self.btnLinearRead.setText(_translate("MainWindow", "LINEAR READ"))
        self.btnLinearWrite.setText(_translate("MainWindow", "LINEAR WRITE"))
        self.txtCardStatus.setText(_translate("MainWindow", "CARD STATUS"))
        self.txtFunctError.setText(_translate("MainWindow", "FUNCTION ERROR"))
        self.linkLabel.setText(_translate("MainWindow", "http://www.d-logic.net/nfc-rfid-reader-sdk/"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.mnuExit.setText(_translate("MainWindow", "Exit"))

