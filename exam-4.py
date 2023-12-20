#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import sys
import time

# Read URL from the command line, ej.: python3 ./demo-get.py http://127.0.0.1:5000/medida
api_url = "http://worldtimeapi.org/api/timezone/Europe/Madrid"

# Create a URL request
req = urllib.request.Request(api_url)

# Normally you have to specify the method you are going to use: GET, POST, DELETE, etc. 
# Not necessary for GET
#req.get_method = lambda: "GET"

# Make the request
f = urllib.request.urlopen(req)

# Print the message received
data=json.loads(f.read().decode('utf-8'))
print("Date is: " + str(data['utc_datetime']))