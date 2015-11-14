#Investigating Reaction times on the motorway
#Spencer Organ - KESH Academy
#You will need to plug in a pair of earphones for the audio test

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys
import random

sense.clear(255,255,255)

b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
w = (255,255,255)

red_on = [
b,b,w,w,w,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b
]

green_on = [
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,w,w,w,b,b
]

sense.set_pixels(red_on)
time.sleep(5)
sense.clear(0,0,0)
sense.set_pixels(green_on)
sense.clear(0,0,0)

