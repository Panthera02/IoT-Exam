import paho.mqtt.client as mqtt
import json

client = mqtt.Client()

def on_message(client1, userdata, message):
    data = json.loads(str(message.payload.decode("utf-8")))
    for key in data.keys():
        if key == "humidity": 
            print(f"Humidity is: {data[key]}")

client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)
client.subscribe("/ETSIDI/Hum")

client.loop_forever()