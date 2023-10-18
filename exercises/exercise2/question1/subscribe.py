import paho.mqtt.client as mqtt
import mysql.connector
import json
from datetime import datetime
import time

user = 'tomas'
password = '12345'
address = 'mqtt.eclipseprojects.io' 
port = 1883
topic = 'wokwi'

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)

    print(f'Temp: {data["temp"]}°C | Humidity: {data["humidity"]}')

    actual_time = datetime.now()
    actual_date = actual_time.strftime('%Y-%m-%d %H:%M')

    print(actual_date)

    add_data = "INSERT INTO datas (temp, humidity, date) VALUES (%s, %s, %s)"

    try:
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database="arduino")

        cursor = connection.cursor()

        cursor.execute(add_data, (data['temp'], data['humidity'], actual_date))

        connection.commit()

        cursor.close()
    except mysql.connector.Error as err:
        print(err)
    else:
        connection.close()

subscribe = mqtt.Client()
subscribe.username_pw_set(user, password)
subscribe.connect(address, port)
subscribe.subscribe(topic)
subscribe.on_message = on_message
subscribe.loop_forever()
