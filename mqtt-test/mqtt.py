import paho.mqtt.client as paho

class MQTT():
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.connect(host=self.broker, port=self.port)
        self.client.on_message = self.on_message
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"connected to broker at {self.broker}:{self.port}")

    def on_message(self, client, userdata, msg):
        print(f"got {msg.payload}")

    def subscribe(self, topic):
        self.client.subscribe(topic, qos=1)

    def publish(self, topic, data):
        self.client.publish(topic, data, qos=1)


