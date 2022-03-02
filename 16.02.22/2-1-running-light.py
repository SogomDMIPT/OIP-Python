import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

i = 0
k = 0
while True:
    GPIO.output(leds[i], 1)
    time.sleep(0.2)
    GPIO.output(leds[i], 0)
    if i < 7:
        i = i + 1
    else: 
        i = 0
        k = k + 1
    if k == 3:
        break    

GPIO.output(leds, 0)
GPIO.cleanup()    