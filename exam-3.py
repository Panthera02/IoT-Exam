from datetime import datetime
from sense_hat import SenseHat
from time import sleep
import http.client
import urllib

sense = SenseHat()

key = "2HWZ97D30LAJBYLL"
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")

while True:
    params = urllib.parse.urlencode({"field1": sense.get_temperature(), "key": key})
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    conn.close()
    sleep(5)