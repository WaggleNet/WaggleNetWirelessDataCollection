import paho.mqtt.client as paho

class MQTT():
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.connect(host=self.broker, port=self.port)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"connected to broker at {self.broker}:{self.port}")

    def subscribe(self, topic, callback):
        self.client.subscribe(topic, qos=1)
        self.client.message_callback_add(topic, callback)

    def publish(self, topic, data):
        self.client.publish(topic, data, qos=1)


