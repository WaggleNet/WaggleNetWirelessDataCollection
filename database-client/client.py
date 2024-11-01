from mqtt import MQTT
import callbacks
import time, json

HOST = "localhost"
PORT = 1883

client = MQTT(HOST, PORT)

data = {
        'hive_id': "12345test", # identifying string for which hive
        'sensor_id': "s1", # identifying string for which sensor within a hive
        'timestamp': 149129421, # unix timestamp in ms of when the data was retrieved
        'value': 12543.0, # sensor value
    }

data_json = json.dumps(data)

def start_client():
    client.subscribe("/test-sensor", callbacks.sensor_data_callback)
    client.publish("/test-sensor", data_json)
   
    print("Listening to MQTT broker for new data, CTRL-C to exit")
    while True:
        time.sleep(1)
