from time import sleep
from sense_hat import SenseHat
from datetime import datetime
import paho.mqtt.client as mqtt

sense = SenseHat()

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()

while True:
    temp = sense.get_temperature()
    data = '''{"time": "%s", "city": "Madrid", "temperature": %f}'''%(datetime.now().strftime("%H:%M:%S"), temp)
    if temp < 12:
        client.publish("/ETSIDI/666", data)

client.disconnect()
client.loop_stop()