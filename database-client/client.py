from mqtt import MQTT
import callbacks

HOST = "localhost"
PORT = 6789

client = MQTT(HOST, PORT)

client.subscribe("/test-sensor", callbacks.sensor_data_callback)