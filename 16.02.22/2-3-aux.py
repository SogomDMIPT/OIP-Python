import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds, 0)

while True:
    i = 0
    while i < 8:
        GPIO.output(leds[i], GPIO.input(aux[i]))
        i = i + 1

GPIO.output(leds, 0)
GPIO.cleanup()        