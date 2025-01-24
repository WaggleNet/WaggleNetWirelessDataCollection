
class BaseSensor():
    def __init__(self):
        print("new sensor")

    def poll(self):
        raise NotImplementedError()

    def getI2C(self, pin):
        pass