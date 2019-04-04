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
        self.ddrValueLabel_2 = QtWidgets.QLabel(self.portRegisterFrame)
        self.ddrValueLabel_2.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.ddrValueLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ddrValueLabel_2.setObjectName("ddrValueLabel_2")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(290, 360, 118, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(270, 130, 141, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.muxFrame = QtWidgets.QFrame(Frame)
        self.muxFrame.setGeometry(QtCore.QRect(240, 340, 51, 41))
        self.muxFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.muxFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.muxFrame.setLineWidth(0)
        self.muxFrame.setObjectName("muxFrame")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(260, 140, 20, 201))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setGeometry(QtCore.QRect(120, 360, 118, 3))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.pinOutputFrame = QtWidgets.QFrame(Frame)
        self.pinOutputFrame.setGeometry(QtCore.QRect(80, 340, 41, 41))
        self.pinOutputFrame.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.pinOutputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.pinOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pinOutputFrame.setLineWidth(3)
        self.pinOutputFrame.setObjectName("pinOutputFrame")
        self.line_5 = QtWidgets.QFrame(Frame)
        self.line_5.setGeometry(QtCore.QRect(170, 170, 20, 191))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.pullUpFrame = QtWidgets.QFrame(Frame)
        self.pullUpFrame.setGeometry(QtCore.QRect(160, 100, 61, 71))
        self.pullUpFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pullUpFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pullUpFrame.setLineWidth(0)
        self.pullUpFrame.setObjectName("pullUpFrame")
        self.label = QtWidgets.QLabel(self.pullUpFrame)
        self.label.setGeometry(QtCore.QRect(0, -20, 66, 141))
        self.label.setObjectName("label")
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

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.ddrValueLabel.setText(_translate("Frame", "0"))
        self.ddrValueLabel_2.setText(_translate("Frame", "0"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><img src=\":/image/Images/rheostat.png\"/></p></body></html>"))
        self.ddrLabel.setText(_translate("Frame", "DDR"))
        self.portLabel.setText(_translate("Frame", "PORT"))


