import Components.Port_View.PD0_View
import Components.Port_View.PD1_View
import Components.Port_View.PD2_View
import Components.Port_View.PD3_View
import Components.Port_View.PD4_View
import Components.Port_View.PD5_View
import Components.Port_View.PD6_View
import Components.Port_View.PD7_View

import Components.Port_View.PC7_View

from Components import WatchDogTimer
from Components import  SPI
from Components import EEPROM


class ViewFactory():

    viewFactory = None
    top = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if ViewFactory.viewFactory != None:
            raise Exception("This class is a singleton!")
        else:
            ViewFactory.viewFactory = ViewFactory()


    @staticmethod
    def getInstance():
        if ViewFactory.viewFactory == None:
            ViewFactory()
        return ViewFactory.viewFactory

    @staticmethod
    def getView(viewName):
        if viewName == 'PD0':
            return Components.Port_View.PD0_View.PD0_View().getViewFrame()
        elif viewName == 'PD1':
            return Components.Port_View.PD1_View.PD1_View().getViewFrame()
        elif viewName == 'PD2':
            return Components.Port_View.PD2_View.PD2_View().getViewFrame()
        elif viewName == 'PD3':
            return Components.Port_View.PD3_View.PD3_View().getViewFrame()
        elif viewName == 'PD4':
            return Components.Port_View.PD4_View.PD4_View().getViewFrame()
        elif viewName == 'PD5':
            return Components.Port_View.PD5_View.PD5_View().getViewFrame()
        elif (viewName == 'PD6'):
            return Components.Port_View.PD6_View.PD6_View().getViewFrame()
        elif viewName == 'PD7':
            return Components.Port_View.PD7_View.PD7_View().getViewFrame()
        elif viewName == 'PC7':
            return Components.Port_View.PC7_View.PC7_View().getViewFrame()
        elif viewName == 'WATCHDOG':
            return WatchDogTimer.Ui_watchDogFrame()
        elif viewName == 'EEPROM':
            return EEPROM.memoryDump().getMemoryDump()
        elif viewName == 'SPI':
            return SPI.Ui_SPIFrame()
        else:
            return None

