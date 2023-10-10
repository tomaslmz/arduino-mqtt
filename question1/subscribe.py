import paho.mqtt.client as mqtt
import json

user = os.getenv("PUB_USER")
password = os.getenv("PUB_PASSWORD")
address = os.getenv("PUB_ADDRESS")
port = 1883
topic = os.getenv("PUB_TOPIC")

def on_message(client, userdata, msg):
    dados = json.loads(msg.payload)
    print(f"Message: {dados['message']}")

subscribe = mqtt.Client()
subscribe.username_pw_set(user, password)
subscribe.connect(endereco, port)
subscribe.subscribe(topico)
subscribe.on_message = on_message
subscribe.loop_forever()