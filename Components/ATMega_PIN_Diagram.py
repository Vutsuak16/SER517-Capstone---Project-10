# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen

from PyQt5.QtWidgets import QWidget, QLabel, QSplitter, QApplication, QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt

import Components.Register_Values
import Components.List_of_Registers
import Components.stackedWidget
import Components.ViewFactory
import Components.ATMega_Block_Diagram
import Components.Globalmap
import Components.ObjectFactory
import Components.Standard

from Components import ATMega_Block_Diagram



class PIN_Diagram(QtWidgets.QWidget):

    rightFrame = None
    stackedLayout = None
    pinr_dict = {}
    pinl_dict = {}
    standard = None

    def __init__(self):
        super(PIN_Diagram, self).__init__()

        if self.rightFrame == None:

            PIN_Diagram.standard = Components.Standard.value

            self.rightFrame = QFrame()

            simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            simulatorTitle = QtWidgets.QLabel(self)
            simulatorTitle.setText("ATMega328p")
            simulatorTitle.setStyleSheet('color : white')
            simulatorTitle.setAlignment(Qt.AlignCenter)
            simulatorTitle.setFont(simulatorFont)

            simulatorFrame = QFrame()
            simulatorFrame.setStyleSheet("QWidget { background-color: black }")
            simulatorFrame.setLineWidth(3)
            simulatorFrame.setMidLineWidth(3)
            simulatorFrame.mousePressEvent = PIN_Diagram.microcontrollerClicked
            simulatorFrame.setFrameShape(QFrame.Panel)
            simulatorFrame.setFixedSize(270, 490)
            simulatorFrame.layout = QHBoxLayout()
            simulatorFrame.layout.addWidget(simulatorTitle)

            simulatorFrame.setFrameShadow(simulatorFrame.Raised)
            simulatorFrame.setLayout(simulatorFrame.layout)

            pinFont = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)

            pinsl = ['PD0', 'PD1', 'PD2', 'PD3', 'PD4', 'PD5', 'PD6', 'PD7','PB4', 'PB5', 'PB6', 'PB7']

            leftPinFrame = QFrame()
            leftPinFrame.layout = QVBoxLayout()
            leftPinFrame.layout.setAlignment(Qt.AlignRight)
            leftPinFrame.layout.addStretch()

            # .itemClicked.connect(self.Clicked)

            for i in pinsl:
                self.pinl_dict[i] = QtWidgets.QPushButton(self)

                self.pinl_dict[i].setText(i)
                self.pinl_dict[i].setStyleSheet(PIN_Diagram.standard.deactivated)
                self.pinl_dict[i].setEnabled(False)
                # pinl_dict[i].setAlignment(Qt.AlignRight)
                self.pinl_dict[i].setFixedSize(30, 30)
                self.pinl_dict[i].setFont(pinFont)
                self.pinl_dict[i].clicked.connect(lambda state, x=i: self.portClicked(x))
                leftPinFrame.layout.setSpacing(10)
                leftPinFrame.layout.addWidget(self.pinl_dict[i])

            leftPinFrame.setLayout(leftPinFrame.layout)
            leftPinFrame.layout.addStretch()

            rightPinFrame = QFrame()
            rightPinFrame.layout = QVBoxLayout()
            rightPinFrame.layout.setAlignment(Qt.AlignLeft)
            rightPinFrame.layout.addStretch()

            pinsr = ['PC7','PC6', 'PC5', 'PC4', 'PC3', 'PC2', 'PC1', 'PC0','PB0', 'PB1', 'PB2','PB3']

            for i in pinsr:
                self.pinr_dict[i] = QtWidgets.QPushButton(self)

                self.pinr_dict[i].setText(i)
                self.pinr_dict[i].setStyleSheet(PIN_Diagram.standard.deactivated)
                self.pinr_dict[i].setEnabled(False)
                self.pinr_dict[i].setFixedSize(30, 30)
                self.pinr_dict[i].setFont(pinFont)
                self.pinr_dict[i].clicked.connect(lambda state, x=i: self.portClicked(x))
                rightPinFrame.layout.setSpacing(10)
                rightPinFrame.layout.addWidget(self.pinr_dict[i])

            rightPinFrame.layout.addStretch()
            rightPinFrame.setLayout(rightPinFrame.layout)
            #enable pin clicks for left
            for val in pinsl:
                self.pinl_dict[val].setEnabled(True)
                self.pinl_dict[val].setStyleSheet(self.standard.low)

            # enable pin clicks for left
            for val in pinsl:
                self.pinl_dict[val].setEnabled(True)
                self.pinl_dict[val].setStyleSheet(self.standard.low)

            # enable pin clicks for right
            for val in pinsr:
                self.pinr_dict[val].setEnabled(True)
                self.pinr_dict[val].setStyleSheet(self.standard.low)


            self.verticalSlider = QtWidgets.QSlider()
            self.verticalSlider.setGeometry(QtCore.QRect(10, 10, 10, 10))
            self.verticalSlider.setMinimum(0)
            self.verticalSlider.setMaximum(100)
            self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
            self.verticalSlider.setObjectName("verticalSlider")
            self.verticalSlider.setFocusPolicy(Qt.StrongFocus)
            self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksRight)
            self.verticalSlider.setTickInterval(10)
            self.verticalSlider.setSingleStep(1)

            temperature = ["120","110","100" , "90" , "80", "70", "60", "50", "40","30","20","10","0"]
            self.temperatureFrame = QFrame()
            self.temperatureFrame.layout = QVBoxLayout()
            self.temperatureFrame.layout.setAlignment(Qt.AlignLeft)
            self.temperatureFrame.layout.addStretch()


            for val in temperature:
                temp = QLabel()
                temp.setText(val)
                self.temperatureFrame.layout.setSpacing(37)
                self.temperatureFrame.layout.addWidget(temp)

            self.temperatureFrame.layout.addStretch()
            self.temperatureFrame.setLayout(self.temperatureFrame.layout)

            self.rightFrame.setFrameShape(QFrame.StyledPanel)
            self.rightFrame.layout = QHBoxLayout()
            self.rightFrame.layout.addWidget(leftPinFrame)
            self.rightFrame.layout.addWidget(simulatorFrame)
            self.rightFrame.layout.addWidget(rightPinFrame)
            self.rightFrame.layout.addWidget(self.verticalSlider)
            self.rightFrame.layout.addWidget(self.temperatureFrame)
            self.rightFrame.setLayout(self.rightFrame.layout)

    def getPIN_Digram(self):
        return self.rightFrame

    @staticmethod
    def setPinStatus(port, value):
        if value != 0:
            if port in PIN_Diagram.pinl_dict:
                PIN_Diagram.pinl_dict[port].setStyleSheet(PIN_Diagram.standard.high)
                # PIN_Diagram.pinl_dict[port].setFont(QtGui.QFont("Arial", 9, QtGui.QFont.ExtraBold))
            elif port in PIN_Diagram.pinr_dict:
                PIN_Diagram.pinr_dict[port].setStyleSheet(PIN_Diagram.standard.high)
                # PIN_Diagram.pinr_dict[port].setEnabled(True)

        else:
            if port in PIN_Diagram.pinl_dict:
                PIN_Diagram.pinl_dict[port].setStyleSheet(PIN_Diagram.standard.low)
                # PIN_Diagram.pinl_dict[port].setFont(QtGui.QFont("Arial", 5, QtGui.QFont.ExtraBold))
            elif port in PIN_Diagram.pinr_dict:
                PIN_Diagram.pinr_dict[port].setStyleSheet(PIN_Diagram.standard.low)
                # PIN_Diagram.pinr_dict[port].setEnabled(True)

    def microcontrollerClicked(self):
        microcontrollerBlock = QFrame()
        blockDiagramFrame = ATMega_Block_Diagram.Ui_microcontrollerBlock()
        blockDiagramFrame.setupUi(microcontrollerBlock)
        blockDiagramFrame.eepromFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram, "EEPROM", ['EEPROM.EEARL', 'EEPROM.EEARH', 'EEPROM.EEDR', 'EEPROM.EECR'])
        blockDiagramFrame.gpiorFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "GPIOR", ['CORE.GPIOR0', 'CORE.GPIOR1', 'CORE.GPIOR2'])
        blockDiagramFrame.flashFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "FLASH", [])
        blockDiagramFrame.tc0Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "TIMER0", ['TMRIRQ0.TIMSK0',
                                                                                                               'TMRIRQ0.TIFR0', 'TIMER0.Counter',
                                                                                                               'TIMER0.TCNT', 'TIMER0.OCRA',
                                                                                                               'TIMER0.OCRB', 'TIMER0.TCCRA','TIMER0.TCCRB'])
        blockDiagramFrame.tc1Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram, "TIMER1", ['TMRIRQ1.TIMSK1', 'TMRIRQ1.TIFR1', 'TIMER1.TCNTH',
                                                                                                 'TIMER1.TCNTL', 'TIMER1.OCRAH', 'TIMER1.OCRAL', 'TIMER1.OCRBH',
                                                                                                 'TIMER1.OCRBL', 'TIMER1.ICRH', 'TIMER1.ICRL', 'TIMER1.TCCRA',
                                                                                                 'TIMER1.TCCRB', 'TIMER1.TCCRC'])
        blockDiagramFrame.tc2Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "TIMER2", ['TMRIRQ2.TIMSK2', 'TMRIRQ2.TIFR2', 'TIMER2.TCNT',
                                                                                                               'TIMER2.OCRA', 'TIMER2.OCRB', 'TIMER2.TCCRA', 'TIMER2.TCCRB'])
        blockDiagramFrame.watchdogFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "WATCHDOG", [])
        blockDiagramFrame.spiFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "SPI", ['SPI.SPDR', 'SPI.SPSR', 'SPI.SPCR'])
        blockDiagramFrame.usartFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "UART0", ['UART0.UDR', 'UART0.UCSRA', 'UART0.UCSRB'])
        Components.stackedWidget.stackWidget.addWidget(microcontrollerBlock)
        Components.stackedWidget.stackWidget.incrementTopCount()

    def portClicked(self, port):  # On Click opens up port circuit diagram

        Components.Register_Values.Register_Values.clearList()

        pinRegister = "PORT" + port[1] + ".PIN"
        pinValue = Components.Globalmap.Map.getValue(pinRegister)
        pinAddress = Components.Globalmap.Map.getRegisterAddress(pinRegister)


        ddrRegister = "PORT" + port[1] + ".DDR"
        ddrValue = Components.Globalmap.Map.getValue(ddrRegister)
        ddrAddress = Components.Globalmap.Map.getRegisterAddress(ddrRegister)

        portRegister = "PORT" + port[1] + ".PORT"
        portValue = Components.Globalmap.Map.getValue(portRegister)
        portAddress = Components.Globalmap.Map.getRegisterAddress(portRegister)

        if pinValue!=None:
            Components.Register_Values.Register_Values.addRegister(pinRegister, hex(pinAddress), pinValue)
        else:
            Components.Register_Values.Register_Values.addRegister(pinRegister, hex(pinAddress), "0")

        if ddrValue!=None:
            Components.Register_Values.Register_Values.addRegister(ddrRegister,hex(ddrAddress) , ddrValue)
        else:
            Components.Register_Values.Register_Values.addRegister(ddrRegister, hex(ddrAddress), "0")

        if portValue!=None:
            Components.Register_Values.Register_Values.addRegister(portRegister, hex(portAddress), portValue)
        else:
            Components.Register_Values.Register_Values.addRegister(portRegister, hex(portAddress), "0")


        print(port)
        pinFrame = Components.ViewFactory.ViewFactory.getView(port)

        obj = Components.ObjectFactory.ObjectFactory.getObject(port)
        if obj != None:

            obj.setDDR(Components.Globalmap.Map.pin_ddrRegisterValue_map[port])
            obj.setPort(Components.Globalmap.Map.pin_portRegisterValue_map[port])
            obj.setPin(Components.Globalmap.Map.pin_pinRegisterValue_map[port])

        if pinFrame != None:
            Components.stackedWidget.stackWidget.addWidget(pinFrame)
            Components.stackedWidget.stackWidget.incrementTopCount()

    def blockComponentClicked(self, component, registers):
        frame = Components.ViewFactory.ViewFactory.getView(component)

        if frame != None:
            if type(frame) != QFrame:
                block = QFrame()
                frame.setupUi(block)
                Components.stackedWidget.stackWidget.addWidget(block)
                Components.stackedWidget.stackWidget.incrementTopCount()
            else:
                Components.stackedWidget.stackWidget.addWidget(frame)
                Components.stackedWidget.stackWidget.incrementTopCount()

        Components.Register_Values.Register_Values.clearList()
        for key in registers:
            registerAddress = Components.Globalmap.Map.getRegisterAddress(key)
            registerValue = Components.Globalmap.Map.getValue(key)
            Components.Register_Values.Register_Values.addRegister(key.split('.')[1], hex(registerAddress), registerValue)





