from mqtt import MQTT
import time

m = MQTT('localhost', 1883)

def mqtt_callback(client, userdata, msg):
    print(msg.payload)

m.subscribe("/test-sensor", mqtt_callback)
time.sleep(1)

for i in range(100):
    m.publish("/test-sensor", "testmessage")

time.sleep(1)