from time import sleep
from sense_hat import SenseHat
import paho.mqtt.client as mqtt

sense = SenseHat()

letter = '@'

def create():
    global letter
    letter = chr(ord(letter)+ 1)
    return """{"ID": "%c", "city": "Madrid", "humidity": %f}"""%(letter, sense.get_humidity())

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()

while True:
    #print(sense.get_humidity())
    if sense.get_humidity() > 65 :client.publish("/ETSIDI/Hum", create())
    sleep(3)

client.disconnect()
client.loop_stop()