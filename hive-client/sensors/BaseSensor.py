
class BaseSensor():
    def __init__(self):
        print("new sensor")

    # wrapper function for poll
    def wrap_poll(self):
        self.poll()

    def wrap_setup(self, rfm9x):
        self.rfm9x = rfm9x
        self.setup()

    def poll(self):
        raise NotImplementedError()

    def getI2C(self, pin):
        pass

    def setup(self):
        pass