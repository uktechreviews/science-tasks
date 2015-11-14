import time
import random

print "Reaction time game" print "Python Project 8"
print "" 
  

print "The green light will stay on for a random amount of time between 1 and 10 seconds" 
print "It will then swap to the red light"
print "As soon as it changes hit the switch"
print "We start in 5 seconds"
time.sleep(5)

try:
	while True:
		if (GPIO.input(12) ==1): 
			end = time.time()
			print "you pressed the button" elapsed = end - start
			print "and it took "
			print round(elapsed,2)
			print "Try to beat that next time" 
			GPIO.cleanup() 
			
			break
		else:
			
except KeyboardInterrupt: print "game over"