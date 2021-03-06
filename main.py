# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplitter, QApplication, QHBoxLayout, QVBoxLayout

import Components.ATMega_PIN_Diagram
import Components.Globalmap
import Components.List_of_Registers
import Components.Register_Values
import Components.stackedWidget
from pysimulavrExample.examples import SimulavrAdaptor


class Landing(QtWidgets.QWidget):


	def __init__(self):
		super(Landing, self).__init__()
		self.Register_Values = None
		self.List_of_Registers = None
		self.PIN_Diagram = None
		self.stackWidget = None
		self.initUI()


	def initUI(self):
		self.title = "ATMega Simulator"
		self.top = 100
		self.left = 100
		self.width = 1000
		self.height = 800
		self.setWindowTitle(self.title)
		self.setStyleSheet("background-color: white")
		self.window()
		self.setGeometry(self.top, self.left, self.width, self.height)

		self.show()

	def window(self):

		self.Register_Values = Components.Register_Values.Register_Values().getInstance()  # Object of Class Register Values
		self.List_of_Registers = Components.List_of_Registers.List_of_Registers().getInstance() # Object of Class List of Registers

		self.PIN_Diagram = Components.ATMega_PIN_Diagram.PIN_Diagram() # Object of Class PIN Diagram

		self.stackWidget = Components.stackedWidget.stackWidget().getInstance()

		self.splitter = QSplitter(Qt.Vertical)

		self.splitter.addWidget(self.List_of_Registers)
		self.splitter.addWidget(self.Register_Values)
		self.splitter.setSizes([300,150])

		self.horizontalLayout = QHBoxLayout()

		self.rightFrame = self.PIN_Diagram.getPIN_Digram()

		self.stackWidget.addWidget(self.rightFrame)
		print(self.stackWidget.currentWidget())

		self.horizontalSplitter = QSplitter(Qt.Horizontal)
		self.horizontalLayout.addWidget(self.splitter)
		self.horizontalSplitter.addWidget(self.stackWidget)
		self.horizontalSplitter.setSizes([80,320])
		self.horizontalSplitter.adjustSize()

		self.titleFont =  QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
		self.Title = QtWidgets.QLabel(self)
		self.Title.setText("ATMega328p Simulator")
		self.Title.setFont(self.titleFont)
		self.Title.setAlignment(Qt.AlignCenter)

		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(lambda : self.backClicked())

		self.horizontalLayout.addWidget(self.horizontalSplitter)

		self.StatusFont =  QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
		self.Status = QtWidgets.QLabel(self)
		self.Status.setText(self.getConnectionStatus())
		self.Status.setFont(self.StatusFont)
		self.Status.setStyleSheet('color : green')
		self.Status.setAlignment(Qt.AlignCenter)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.Title)
		self.verticalLayout.addWidget(self.Status)
		self.verticalLayout.addWidget(self.backButton, 0, Qt.AlignRight)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.setLayout(self.verticalLayout)

	def getConnectionStatus(self):  # Function returns status (Connected / Disconnected)
		return "Connected to Simulavr"

	def backClicked(self):
		topWidget = Components.stackedWidget.stackWidget.top
		if topWidget != 0:
			print("TOP")
			widgetToRemove = Components.stackedWidget.stackWidget.StackWidget.widget(topWidget)
			Components.stackedWidget.stackWidget.decrementTopCount()
			Components.stackedWidget.stackWidget.removeWidget(widgetToRemove)

	def updateUI(self):
		for key, value in Components.Globalmap.Map.map.items():
			port = key.split('.')[0]
			if key in ['PORTB.PORT', 'PORTC.PORT', 'PORTD.PORT']:
				self.setPortValues(port, value)
			if key in ['PORTB.DDR', 'PORTC.DDR', 'PORTD.DDR']:
				self.setDdrValues(port, value)
			if key in ['PORTB.PIN', 'PORTC.PIN', 'PORTD.PIN']:
				self.setPinValues(port, value)

	def setPortValues(self, key, value):
		binVal = self.convertValueToBin(value)
		for i in range(len(binVal) - 1, -1, -1):
			update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
			value = int(binVal[i])
			Components.Globalmap.Map.pin_portRegisterValue_map[update] = value

	def setDdrValues(self, key, value):
		binVal = self.convertValueToBin(value)
		for i in range(len(binVal) - 1, -1, -1):
			update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
			value = int(binVal[i])
			Components.Globalmap.Map.pin_ddrRegisterValue_map[update] = value

	def setPinValues(self, key, value):
		binVal = self.convertValueToBin(value)
		for i in range(len(binVal) - 1, -1, -1):
			update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
			value = int(binVal[i])
			Components.Globalmap.Map.pin_pinRegisterValue_map[update] = value
			self.PIN_Diagram.setPinStatus(update, value)

	def convertValueToBin(self, value):
		binVal = bin(value)[2:]
		if len(binVal) < 8:
			binVal = '0' * (8 - len(binVal)) + binVal
		return binVal

class threadExample(QThread):
	def __init__(self, ui, sim):
		QThread.__init__(self)
		self.sim = sim
		self.ui = ui
		self.start()

	def run(self):
		self.sim.runProgram(self.ui, self)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	obj = Landing()
	sim = SimulavrAdaptor.SimulavrAdapter()
	thread = threadExample(obj, sim)
	app.exec_()
