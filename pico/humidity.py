#"module" is not the final name for this interface
#every data generating device (camera, microphone, thermometer) 
#should have its own module class which implements setup and
#poll functions

import random
import time

# We're going to replace this with board.i2c
from machine import i2c, Pin


#dummy class representing a generic sensor, not required


class humiditySensor():
    module_name = "humidity-sensor" #put the name of your sensor/project here
    polling_interval = .5 #time between polls in seconds
    last_poll = time.monotonic()

    # Module specific stuff
    Si7021_ADDR = 0x40
    i2c

    def __init__(self):
        print(f"instance of {self.module_name} created")

    def setup(self, p_i2c):
        # This might be necessary if you remove this line from radioManager
        # self.i2c = I2C(0,sda=Pin(8), scl=Pin(9),freq=400000)
        self.i2c = p_i2c

#don't need to modify this
    def wrap_poll(self):
        if ((time.monotonic() - self.last_poll) > self.polling_interval):
            self.last_poll = time.monotonic()
            return self.poll()
        return None


    def poll(self):
        RH_code = self.i2c.readfrom_mem(self.Si7021_ADDR, 0xE5, 2)
        Temp_code = self.i2c.readfrom_mem(self.Si7021_ADDR, 0xE3, 2)

        #convert to useful number
        humidity = round((((RH_code[0] * 256 + RH_code[1]) * 125 / 65536.0) - 6),1)
        cTemp = round((((Temp_code[0] * 256 + Temp_code[1]) * 175.72 / 65536.0) - 46.85)*1.8+32,1)
        return humidity, cTemp