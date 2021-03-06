# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pinLevelDiagram.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Resources import imageResource_rc


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(670, 540)
        Frame.setStyleSheet("color: rgb(204, 0, 0);")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ddrRegisterFrame = QtWidgets.QFrame(Frame)
        self.ddrRegisterFrame.setGeometry(QtCore.QRect(410, 100, 81, 80))
        self.ddrRegisterFrame.setAutoFillBackground(False)
        self.ddrRegisterFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.ddrRegisterFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.ddrRegisterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ddrRegisterFrame.setLineWidth(3)
        self.ddrRegisterFrame.setObjectName("ddrRegisterFrame")
        self.ddrValueLabel = QtWidgets.QLabel(self.ddrRegisterFrame)
        self.ddrValueLabel.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.ddrValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ddrValueLabel.setObjectName("ddrValueLabel")
        self.portRegisterFrame = QtWidgets.QFrame(Frame)
        self.portRegisterFrame.setGeometry(QtCore.QRect(410, 320, 81, 80))
        self.portRegisterFrame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.portRegisterFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.portRegisterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.portRegisterFrame.setLineWidth(3)
        self.portRegisterFrame.setObjectName("portRegisterFrame")
        self.portValueLabel = QtWidgets.QLabel(self.portRegisterFrame)
        self.portValueLabel.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.portValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portValueLabel.setObjectName("portValueLabel")
        self.portLine = QtWidgets.QFrame(Frame)
        self.portLine.setGeometry(QtCore.QRect(290, 360, 118, 3))
        self.portLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.portLine.setLineWidth(3)
        self.portLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.portLine.setObjectName("portLine")
        self.ddrLine1 = QtWidgets.QFrame(Frame)
        self.ddrLine1.setGeometry(QtCore.QRect(270, 130, 141, 20))
        self.ddrLine1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ddrLine1.setLineWidth(3)
        self.ddrLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.ddrLine1.setObjectName("ddrLine1")
        self.ddrLine2 = QtWidgets.QFrame(Frame)
        self.ddrLine2.setGeometry(QtCore.QRect(260, 140, 20, 201))
        self.ddrLine2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ddrLine2.setLineWidth(3)
        self.ddrLine2.setFrameShape(QtWidgets.QFrame.VLine)
        self.ddrLine2.setObjectName("ddrLine2")
        self.pinLine = QtWidgets.QFrame(Frame)
        self.pinLine.setGeometry(QtCore.QRect(120, 350, 131, 21))
        self.pinLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pinLine.setLineWidth(3)
        self.pinLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.pinLine.setObjectName("pinLine")
        self.pinOutputFrame = QtWidgets.QFrame(Frame)
        self.pinOutputFrame.setGeometry(QtCore.QRect(80, 340, 41, 41))
        self.pinOutputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.pinOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pinOutputFrame.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.pinOutputFrame.setLineWidth(3)
        self.pinOutputFrame.setObjectName("pinOutputFrame")
        self.pullupLine = QtWidgets.QFrame(Frame)
        self.pullupLine.setGeometry(QtCore.QRect(180, 170, 20, 191))
        self.pullupLine.setStyleSheet("")
        self.pullupLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pullupLine.setLineWidth(3)
        self.pullupLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.pullupLine.setObjectName("pullupLine")
        self.ddrLabel = QtWidgets.QLabel(Frame)
        self.ddrLabel.setGeometry(QtCore.QRect(420, 80, 67, 17))
        self.ddrLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.ddrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ddrLabel.setObjectName("ddrLabel")
        self.portLabel = QtWidgets.QLabel(Frame)
        self.portLabel.setGeometry(QtCore.QRect(420, 300, 67, 17))
        self.portLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.portLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portLabel.setObjectName("portLabel")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 110, 81, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(250, 340, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(180, 350, 16, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.ddrValueLabel.setText(_translate("Frame", "0"))
        self.portValueLabel.setText(_translate("Frame", "0"))
        self.ddrLabel.setText(_translate("Frame", "DDR"))
        self.portLabel.setText(_translate("Frame", "PORT"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><img src=\":/image/Images/pullupResistor.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><img src=\":/image/Images/multiplexer.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><img src=\":/image/Images/connection.png\"/></p></body></html>"))



