import sys
import time
#import your module
import exampleModule
import digitalio
import dataCollection
import board
import busio
import adafruit_rfm9x
import time

import os

RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.GP5)
RESET = digitalio.DigitalInOut(board.GP6)
spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP4)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)

rfm9x.coding_rate = 5
rfm9x.spreading_factor = 8
rfm9x.tx_power = 23
rfm9x.enable_crc = False
rfm9x.node = 200
rfm9x.destination = 201

# RTC Initalization

#list will contain all data collection modules
modules = []
i2c = busio.I2C(board.GP13, board.GP12)

#append it to the list of modules
modules.append(exampleModule.exampleModule())
modules.append(dataCollection.TMG_data())
for module in modules:
    #always use try except when calling module functions to prevent one module
    # from crashing the whole program
    try:
        module.setup()
    except:
        print(f"an exception occurred while setting up {module.module_name}")

running = True
message_length = 64

while(running):
    transmit = ""
    for module in modules:
        try:
            poll_result = module.wrap_poll()
            if (poll_result is not None):
                transmit += f"[\"{module.module_name}\",  \"{poll_result}\"]"
        except:
            e = sys.exception()
            transmit += f"an exception occurred when polling module \"{module.module_name}\" \n{e}"

    
    for i in range(len(transmit) // message_length + 1):
        message = transmit[i : min( (i + 1) * message_length, len(transmit) )]

        if message != "":
            rfm9x.send_with_ack(bytearray(message))
            print(f"sending: {message}")
