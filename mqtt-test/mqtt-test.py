from mqtt import MQTT
import time

m = MQTT('localhost', 1883)

m.subscribe("/test-sensor")
time.sleep(1)

for i in range(100):
    m.publish("/test-sensor", "testmessage")

time.sleep(1)