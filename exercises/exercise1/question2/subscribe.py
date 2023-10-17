import paho.mqtt.client as mqtt
import json
import os

user = "aluno"
password = "123456"
address = "mqtt.eclipseprojects.io"
port = 1883
topic = "tomas"


def on_message(client, userdata, msg):
  dados = json.loads(msg.payload)
  print(f"Message: {dados['message']}")


subscribe = mqtt.Client()
subscribe.username_pw_set(user, password)
subscribe.connect(address, port)
subscribe.subscribe(topic)
subscribe.on_message = on_message
subscribe.loop_forever()
