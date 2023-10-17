import paho.mqtt.client as mqtt
import json
import serial

arduino = serial.Serial('COM4', 9600)

user = 'aluno'
password = '123456'
endereco = 'mqtt.eclipseprojects.io'
port = 1883
topico = 'senaialuno'

publish = mqtt.Client()
publish.username_pw_set(user, password)
publish.connect(endereco, port)

while(True):
    if arduino.isOpen():
        temp_byte = arduino.readline()
        temp_sting = temp_byte.decode('utf-8')
        publish.publish(topico, temp_sting)