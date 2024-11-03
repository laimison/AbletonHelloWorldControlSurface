import threading
import time

from _Framework.ControlSurface import ControlSurface 

class AbletonHelloWorldControlSurface(ControlSurface):
    __module__ = __name__
    __doc__ = "Hello World Script"

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)

        self.log_message('This is a message from AbletonHelloWorldControlSurface in Log.txt')

    def disconnect(self):
        ControlSurface.disconnect(self)