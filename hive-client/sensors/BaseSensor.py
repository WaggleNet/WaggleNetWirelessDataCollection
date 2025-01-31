from abc import ABC, abstractmethod

class BaseSensor():
    def __init__(self, rfm9x):
        print("new sensor")
        self.rfm9x = rfm9x

    # wrapper function for poll
    def wrap_poll(self):
        self.poll()

    @abstractmethod
    def poll(self):
        pass
    
    def getI2C(self, pin):
        pass