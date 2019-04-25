# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMega_Block_Diagram.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Resources import imageResource_rc

class Ui_microcontrollerBlock(object):
    def setupUi(self, microcontrollerBlock):
        microcontrollerBlock.setObjectName("microcontrollerBlock")
        microcontrollerBlock.resize(793, 607)
        microcontrollerBlock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        microcontrollerBlock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tc0Frame = QtWidgets.QFrame(microcontrollerBlock)
        self.tc0Frame.setGeometry(QtCore.QRect(570, 240, 120, 80))
        self.tc0Frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.tc0Frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.tc0Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tc0Frame.setLineWidth(2)
        self.tc0Frame.setObjectName("tc0Frame")
        self.tc0Label = QtWidgets.QLabel(self.tc0Frame)
        self.tc0Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
        self.tc0Label.setScaledContents(False)
        self.tc0Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tc0Label.setWordWrap(True)
        self.tc0Label.setObjectName("tc0Label")
        self.watchdogFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.watchdogFrame.setGeometry(QtCore.QRect(60, 140, 120, 80))
        self.watchdogFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.watchdogFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.watchdogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.watchdogFrame.setLineWidth(2)
        self.watchdogFrame.setObjectName("watchdogFrame")
        self.watchdogLabel = QtWidgets.QLabel(self.watchdogFrame)
        self.watchdogLabel.setGeometry(QtCore.QRect(16, 20, 91, 41))
        self.watchdogLabel.setScaledContents(False)
        self.watchdogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.watchdogLabel.setWordWrap(True)
        self.watchdogLabel.setObjectName("watchdogLabel")
        self.tc2Frame = QtWidgets.QFrame(microcontrollerBlock)
        self.tc2Frame.setGeometry(QtCore.QRect(60, 390, 120, 80))
        self.tc2Frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.tc2Frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.tc2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tc2Frame.setLineWidth(2)
        self.tc2Frame.setObjectName("tc2Frame")
        self.tc2Label = QtWidgets.QLabel(self.tc2Frame)
        self.tc2Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
        self.tc2Label.setScaledContents(False)
        self.tc2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tc2Label.setWordWrap(True)
        self.tc2Label.setObjectName("tc2Label")
        self.usartFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.usartFrame.setGeometry(QtCore.QRect(340, 350, 120, 80))
        self.usartFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.usartFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.usartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usartFrame.setLineWidth(2)
        self.usartFrame.setObjectName("usartFrame")
        self.usartLabel = QtWidgets.QLabel(self.usartFrame)
        self.usartLabel.setGeometry(QtCore.QRect(30, 30, 67, 16))
        self.usartLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usartLabel.setObjectName("usartLabel")
        self.flashFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.flashFrame.setGeometry(QtCore.QRect(340, 80, 120, 80))
        self.flashFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.flashFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.flashFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.flashFrame.setLineWidth(2)
        self.flashFrame.setObjectName("flashFrame")
        self.flashLabel = QtWidgets.QLabel(self.flashFrame)
        self.flashLabel.setGeometry(QtCore.QRect(20, 30, 67, 17))
        self.flashLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.flashLabel.setObjectName("flashLabel")
        self.gpiorFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.gpiorFrame.setGeometry(QtCore.QRect(570, 130, 120, 80))
        self.gpiorFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.gpiorFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.gpiorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gpiorFrame.setLineWidth(2)
        self.gpiorFrame.setObjectName("gpiorFrame")
        self.gpiorLabel = QtWidgets.QLabel(self.gpiorFrame)
        self.gpiorLabel.setGeometry(QtCore.QRect(20, 20, 67, 41))
        self.gpiorLabel.setScaledContents(False)
        self.gpiorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gpiorLabel.setWordWrap(True)
        self.gpiorLabel.setObjectName("gpiorLabel")
        self.spiFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.spiFrame.setGeometry(QtCore.QRect(570, 350, 120, 80))
        self.spiFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.spiFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.spiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spiFrame.setLineWidth(2)
        self.spiFrame.setObjectName("spiFrame")
        self.spiLabel = QtWidgets.QLabel(self.spiFrame)
        self.spiLabel.setGeometry(QtCore.QRect(30, 20, 67, 41))
        self.spiLabel.setScaledContents(False)
        self.spiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.spiLabel.setWordWrap(True)
        self.spiLabel.setObjectName("spiLabel")
        self.tc1Frame = QtWidgets.QFrame(microcontrollerBlock)
        self.tc1Frame.setGeometry(QtCore.QRect(60, 270, 120, 80))
        self.tc1Frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.tc1Frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.tc1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tc1Frame.setLineWidth(2)
        self.tc1Frame.setObjectName("tc1Frame")
        self.tc1Label = QtWidgets.QLabel(self.tc1Frame)
        self.tc1Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
        self.tc1Label.setScaledContents(False)
        self.tc1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tc1Label.setWordWrap(True)
        self.tc1Label.setObjectName("tc1Label")
        self.eepromFrame = QtWidgets.QFrame(microcontrollerBlock)
        self.eepromFrame.setGeometry(QtCore.QRect(340, 200, 120, 80))
        self.eepromFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.eepromFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.eepromFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eepromFrame.setLineWidth(2)
        self.eepromFrame.setObjectName("eepromFrame")
        self.eepromLabel = QtWidgets.QLabel(self.eepromFrame)
        self.eepromLabel.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.eepromLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eepromLabel.setObjectName("eepromLabel")
        self.label = QtWidgets.QLabel(microcontrollerBlock)
        self.label.setGeometry(QtCore.QRect(220, 100, 66, 381))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_2.setGeometry(QtCore.QRect(180, 160, 61, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_3.setGeometry(QtCore.QRect(180, 290, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_4.setGeometry(QtCore.QRect(180, 410, 61, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_5.setGeometry(QtCore.QRect(280, 130, 61, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_6.setGeometry(QtCore.QRect(270, 240, 71, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_7.setGeometry(QtCore.QRect(280, 370, 61, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_8.setGeometry(QtCore.QRect(460, 90, 66, 381))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_9.setGeometry(QtCore.QRect(510, 160, 61, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_10.setGeometry(QtCore.QRect(510, 260, 61, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(microcontrollerBlock)
        self.label_11.setGeometry(QtCore.QRect(510, 370, 61, 41))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(microcontrollerBlock)
        QtCore.QMetaObject.connectSlotsByName(microcontrollerBlock)

    def retranslateUi(self, microcontrollerBlock):
        _translate = QtCore.QCoreApplication.translate
        microcontrollerBlock.setWindowTitle(_translate("microcontrollerBlock", "Frame"))
        self.tc0Label.setText(_translate("microcontrollerBlock", "TC 0            (8-bit)"))
        self.watchdogLabel.setText(_translate("microcontrollerBlock", "Watchdog timer"))
        self.tc2Label.setText(_translate("microcontrollerBlock", "TC 2            (8-bit)"))
        self.usartLabel.setText(_translate("microcontrollerBlock", "USART 0"))
        self.flashLabel.setText(_translate("microcontrollerBlock", "Flash"))
        self.gpiorLabel.setText(_translate("microcontrollerBlock", "GPIOR [2:0]"))
        self.spiLabel.setText(_translate("microcontrollerBlock", "SPI 0            (8-bit)"))
        self.tc1Label.setText(_translate("microcontrollerBlock", "TC 1            (16-bit)"))
        self.eepromLabel.setText(_translate("microcontrollerBlock", "EEPROM"))
        self.label.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow2.png\"/></p></body></html>"))
        self.label_2.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_3.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_4.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_5.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow6.png\"/></p></body></html>"))
        self.label_6.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow6.png\"/></p></body></html>"))
        self.label_7.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_8.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow2.png\"/></p></body></html>"))
        self.label_9.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_10.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))
        self.label_11.setText(_translate("microcontrollerBlock", "<html><head/><body><p><img src=\":/blockImages/Images/arrow4.png\"/></p></body></html>"))

