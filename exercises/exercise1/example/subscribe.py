import paho.mqtt.client as mqtt
import json

user = 'aluno'
password = '123456'
endereco = 'mqtt.eclipseprojects.io'
port = 1883
topico = 'senaialuno'

def on_message(client, userdata, msg):
    dados = json.loads(msg.payload)
    print(f"Temperatura: {dados['Temperatura']}°C | Umidade: {dados['Umidade']}")

subscribe = mqtt.Client()
subscribe.username_pw_set(user, password)
subscribe.connect(endereco, port)
subscribe.subscribe(topico)
subscribe.on_message = on_message
subscribe.loop_forever()