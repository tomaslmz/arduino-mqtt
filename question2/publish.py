from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import os
import json
import serial

load_dotenv()

arduino = serial.Serial(os.getenv("INPUT"), 9600)

user = os.getenv("PUB_USER")
password = os.getenv("PUB_PASSWORD")
address = os.getenv("PUB_ADDRESS")
port = 1883
topic = os.getenv("PUB_TOPIC")

publish = mqtt.Client()
publish.username_pw_set(user, password)
publish.connect(address, port)

while(True):
    if arduino.isOpen():
        button_byte = arduino.readline()
        message = button_byte.decode('utf-8')
        print(message)
        publish.publish(topic, message)
