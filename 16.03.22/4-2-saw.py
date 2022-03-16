import RPi.GPIO as GPIO
import time

def main():
    dac = [26, 19, 13, 6, 5,11, 9, 10]

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)
    value = 0
    k = 1

    k = input("Период: ")
    while True:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(dac, GPIO.OUT)
            
            k = int(k)
            k = int(0.3*510/k) 

            value = value + k
            if value > 255 or value < 0:
                k = -1 * k
                value = value + k
            
            binary = to_binary(value)
            for el in binary:
                print(el)
            GPIO.output(dac, binary)
            time.sleep(0.3)    
        except ValueError:
            print("Это не число")    
        finally:
            GPIO.output(dac, 0)
            GPIO.cleanup()

def to_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

main()