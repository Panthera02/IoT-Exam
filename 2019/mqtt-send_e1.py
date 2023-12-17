import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()

json =  """
        {
            "name": 12.7
        }
        """

client.publish("/ETSIDI/666", json)

client.disconnect()
client.loop_stop()