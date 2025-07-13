#!/usr/bin/env python3
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "test/topic"

def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()}")

client = mqtt.Client()
client.connect(broker, port, 60)
client.subscribe(topic)
client.on_message = on_message

print(f"Subscribed to {topic}. Waiting for messages...")
client.loop_forever()
