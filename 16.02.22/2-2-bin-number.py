import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5,11, 9, 10]
number255 = [1, 1, 1, 1, 1, 1, 1, 1]
number127 = [0, 1, 1, 1, 1, 1, 1, 1]
number64 = [0, 0, 1, 0, 0, 0, 0, 0]
number32 = [0, 0, 0, 1, 0, 0, 0, 0]
number5 = [0, 0, 0, 0, 0, 1, 0, 1]
number0 = [0, 0, 0, 0, 0, 0, 0, 0]

numbers = [number255, number127, number64, number32, number5, number0] 

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for num in numbers:
    GPIO.output(dac, num)
    time.sleep(15 )
    GPIO.output(dac, 0)
GPIO.cleanup()    
