import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5,11, 9, 10]
comp = 4
troyka = 17
MaxVolt = 3.3
bits = len(dac)
levels = 2**bits

def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
    GPIO.setup(comp, GPIO.IN)

    try:
        while True:
                #InputS = input("Put Value:")
                #if InputS.isdigit():
                #    value = int(InputS)

                #    if value > levels -1
            #print(1)
            value = adc()  
            signal = num2dac(value)
            voltage = value / levels *MaxVolt 
            print("Entered value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))
            time.sleep(0.001)
    except ValueError:
        print("Uncorrect")
    finally:
        GPIO.output(dac, 0)
        GPIO.cleanup()

def num2dac(value):
    signal = to_binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    max = levels
    min = 0
    value = int(max / 2)
    #voltage = value / levels *MaxVolt 
    while max - min > 1:
                num2dac(value) 
                time.sleep(0.001)
                CompVal = GPIO.input(comp)   
                if CompVal == 0:
                    max = value
                if CompVal == 1:
                    min = value
                value = int((min + max)/2)    

    return int(value)

def to_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]    

main()