from sense_hat import SenseHat
from time import sleep
import os

clear =  lambda: os.system('cls')

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    dew = temp - (100-hum)/5
    if temp == dew:
        newTemp = sense.get_temperature()
        while temp == newTemp:
            newTemp = sense.get_temperature()
            print(dew)
            sleep(0.5)
            clear()
            sleep(0.5)
    clear()
    print(dew)
    sleep(1)