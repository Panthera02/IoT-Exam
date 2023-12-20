from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def get_idx(matrix):
    for i,c in enumerate(matrix):
        if c == X: return i

X = [0, 255, 0]
O = [0, 0, 0]

pix = [
O, O, O, O, O, O, O, O,
O, O, X, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(pix)

while True:
    for event in sense.stick.get_events():
        if event.direction == "up" and event.action == "pressed" :
            idx = get_idx(pix)
            pix[idx] = O
            pix[idx-8] = X
        if event.direction == "down" and event.action == "pressed" :
            idx = get_idx(pix)
            pix[idx] = O
            if  not idx+8 >= len(pix)-1: pix[idx+8] = X
            else: pix[(idx+8)%64] = X
        if event.direction == "left" and event.action == "pressed" :
            idx = get_idx(pix)
            pix[idx] = O
            pix[idx-1] = X
        if event.direction == "right" and event.action == "pressed" :
            idx = get_idx(pix)
            pix[idx] = O
            if  not idx == len(pix)-1: pix[idx+1] = X
            else: pix[0] = X
        sense.set_pixels(pix)
            
            