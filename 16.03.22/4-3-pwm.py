import RPi.GPIO as GPIO

#GPIO.cleanup()
#dac = [26, 19, 13, 6, 5,11, 9, 10]
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(dac, GPIO.OUT)
#GPIO.output(dac, 0)

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 500)
duty = 0
try:
    while True:
        p.start(duty)
        duty = input("Put new number")
        duty = int(duty)
        p.stop()
except ValueError:
    print("Uncorrect")
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()