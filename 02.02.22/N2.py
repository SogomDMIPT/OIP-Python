import RPi.GPIO as GPIO
import time

leds[8] = {21, 20, 16, 12, 7, 8, 25, 24}

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while True:
    GPIO.output(leds[0], 1)
    time.sleep(1)
    GPIO.output(leds[6], 0)
    time.sleep(1)

