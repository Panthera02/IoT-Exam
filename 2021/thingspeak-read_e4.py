import http.client
import urllib
import json

key = "6KB2X4XEAXMZMVK3"
channel = "2383210"
url = "api.thingspeak.com:80"

path = "/channels/"+channel+"/feeds"
params = urllib.parse.urlencode({'key':key}) 
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection(url)

conn.request("GET", path, params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()

data2 = json.loads(data)
print(json.dumps(data2["feeds"][-1],indent=4,sort_keys=True))

conn.close()