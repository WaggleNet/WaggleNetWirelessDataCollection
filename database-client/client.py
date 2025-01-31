from mqtt import MQTT
import callbacks
import time

HOST = "localhost"
PORT = 1883

client = MQTT(HOST, PORT)

def start_client() -> None:
    client.subscribe("/test-sensor", callbacks.sensor_data_callback)
   
    print("Listening to MQTT broker for new data, CTRL-C to exit")
    while True:
        time.sleep(0.01)

if __name__ == "__main__":
    start_client()