import digitalio
import board
import busio
import adafruit_rfm9x
import time
import os

import os
from sensors.ExampleSensor import ExampleSensor
from sensors.humidity import humidity

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

# list of sensor objects
sensors = []

# instantiate and append your sensor objects here
sensors.append(ExampleSensor())
sensors.append(humidity()) # will crash when running on your machine

for sensor in sensors:
    try:
        sensor.wrap_setup(rfm9x)
    except Exception as e:
        print(f"failed to setup {sensor.module_name} with exception {e}")

while True:
    for sensor in sensors:
        try:
            sensor.poll()
        except Exception as e:
            print(f"failed to poll sensor {sensor.module_name} with exception {e}")