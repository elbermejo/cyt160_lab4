#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

broker = "localhost"  # or your MQTT broker IP
port = 1883
topic = "test/topic"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    message = "MQTT test message"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(2)
