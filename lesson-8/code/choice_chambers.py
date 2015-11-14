#Investigating Choice chambers
#Spencer Organ - KESH Academy


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
