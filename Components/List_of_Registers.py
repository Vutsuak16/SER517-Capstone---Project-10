# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import  QMessageBox , QListWidget
from PyQt5 import  QtCore

import Components.Register_Values
import Components.Globalmap

class List_of_Registers(QListWidget):

    pins = ['SPMCR', 'CORE.SREG', 'CORE.PC', 'CORE.PCb', 'CORE.PRESCALER2', 'CORE.GTCCR', 'CORE.ASSR', 'CORE.PRESCALER01',
            'CORE.CLKPR', 'CORE.OSCCAL', 'CORE.EICRA', 'CORE.EIMSK', 'CORE.EIFR', 'CORE.PCICR', 'CORE.PCIFR', 'CORE.PCMSK0',
            'CORE.PCMSK1', 'CORE.PCMSK2', 'CORE.GPIOR0', 'CORE.GPIOR1', 'CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR',
            'PORTB.B0-Out', 'PORTB.B1-Out', 'PORTB.B2-Out', 'PORTB.B3-Out', 'PORTB.B4-Out', 'PORTB.B5-Out', 'PORTB.B6-Out',
            'PORTB.B7-Out', 'PORTC.PORT', 'PORTC.PIN', 'PORTC.DDR', 'PORTC.C0-Out', 'PORTC.C1-Out', 'PORTC.C2-Out', 'PORTC.C3-Out',
            'PORTC.C4-Out', 'PORTC.C5-Out', 'PORTC.C6-Out', 'PORTD.PORT', 'PORTD.PIN', 'PORTD.DDR', 'PORTD.D0-Out', 'PORTD.D1-Out',
            'PORTD.D2-Out', 'PORTD.D3-Out', 'PORTD.D4-Out', 'PORTD.D5-Out', 'PORTD.D6-Out', 'PORTD.D7-Out', 'ACOMP.ACSR',
            'IRQ.VECTOR0', 'IRQ.VECTOR1', 'IRQ.VECTOR2', 'IRQ.VECTOR3', 'IRQ.VECTOR4', 'IRQ.VECTOR5', 'IRQ.VECTOR6', 'IRQ.VECTOR7',
            'IRQ.VECTOR8', 'IRQ.VECTOR9', 'IRQ.VECTOR10', 'IRQ.VECTOR11', 'IRQ.VECTOR12', 'IRQ.VECTOR13', 'IRQ.VECTOR14',
            'IRQ.VECTOR15', 'IRQ.VECTOR16', 'IRQ.VECTOR17', 'IRQ.VECTOR18', 'IRQ.VECTOR19', 'IRQ.VECTOR20', 'IRQ.VECTOR21',
            'IRQ.VECTOR22', 'IRQ.VECTOR23', 'IRQ.VECTOR24', 'IRQ.VECTOR25', 'EEPROM.EEARH', 'EEPROM.EEARL', 'EEPROM.EEDR',
            'EEPROM.EECR', 'STACK.SPH', 'STACK.SPL', 'TMRIRQ0.TIMSK0', 'TMRIRQ0.TIFR0', 'TIMER0.Counter', 'TIMER0.TCNT',
            'TIMER0.OCRA', 'TIMER0.OCRB', 'TIMER0.TCCRA', 'TIMER0.TCCRB' , 'TMRIRQ1.TIMSK1', 'TMRIRQ1.TIFR1', 'TIMER1.Counter',
            'TIMER1.TCNTH', 'TIMER1.TCNTL', 'TIMER1.OCRAH', 'TIMER1.OCRAL', 'TIMER1.OCRBH', 'TIMER1.OCRBL', 'TIMER1.ICRH',
            'TIMER1.ICRL', 'TIMER1.TCCRA', 'TIMER1.TCCRB', 'TIMER1.TCCRC', 'TMRIRQ2.TIMSK2', 'TMRIRQ2.TIFR2', 'TIMER2.Counter',
            'TIMER2.TCNT', 'TIMER2.OCRA', 'TIMER2.OCRB', 'TIMER2.TCCRA', 'TIMER2.TCCRB', 'AD.ADCH', 'AD.ADCL', 'AD.ADCSRA',
            'AD.ADCSRB', 'AD.ADMUX', 'SPI.SPDR', 'SPI.SPSR', 'SPI.SPCR', 'SPI.shift_in', 'SPI.data_read', 'SPI.data_write',
            'SPI.sSPSR', 'SPI.sSPCR', 'WADO.WDTCR', 'UART0.UDR', 'UART0.USR', 'UART0.UCR', 'UART0.UCSRA', 'UART0.UCSRB',
            'UART0.UBRR', 'UART0.UBRRHI', 'UART0.UDR_write', 'UART0.UDR_read', 'UART0.sUSR', 'UART0.sUCR', 'UART0.sUBR',
            'UART0.UCSRC_UBRRH']

    listWidget = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if List_of_Registers.listWidget != None:
            raise Exception("This class is a singleton!")
        else:
            # Add the correct register values from tracelist and update this comment

            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            List_of_Registers.listWidget.move(90, 195)

            for i in self.pins:
                List_of_Registers.listWidget.addItem(i)

            List_of_Registers.listWidget.itemClicked.connect(List_of_Registers.Clicked)



    @staticmethod
    def getInstance():
        """ Static access method. """
        if List_of_Registers.listWidget == None:
            List_of_Registers()
        return List_of_Registers.listWidget


    def Clicked(self):  # On Click Register name calls this function
        print('there', self.text())
        value = Components.Globalmap.Map.getValue(self.text())
        address = Components.Globalmap.Map.getRegisterAddress(self.text())
        print('there2', value)
        print('map', Components.Globalmap.Map.map)
        Components.Register_Values.Register_Values.clearList()

        if value !=None and address!= None:
            Components.Register_Values.Register_Values.addRegister(self.text(), hex(address), hex(value))
        else:
            Components.Register_Values.Register_Values.addRegister(self.text(), "NA", "NA")



