import paho.mqtt.client as mqtt
import json

# Part B
from sense_hat import SenseHat
from time import sleep

client = mqtt.Client()

# Part B
sense = SenseHat()

def on_message(client1, userdata, message):
    data = json.loads(str(message.payload.decode("utf-8")))
    for key in data.keys():
        print(f"{key}: {data[key]}")

    # Part B
    sense.clear(255,0,0)
    sleep(2)
    sense.clear()

client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)
client.subscribe("/ETSIDI/666")

client.loop_forever()