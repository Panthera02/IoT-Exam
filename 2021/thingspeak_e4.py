from datetime import datetime
#from sense_hat import SenseHat
from time import sleep
import http.client
import urllib

#sense = SenseHat()

key = "6KB2X4XEAXMZMVK3"
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")

while True:
    params = urllib.parse.urlencode({"time": f"{datetime.now().strftime('%H:%M:%S')}", "city": "Madrid", "temperature": 23, "key": key})
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    conn.close()
    sleep(5)

