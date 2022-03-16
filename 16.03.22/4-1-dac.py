import RPi.GPIO as GPIO
import time

def main():
    dac = [26, 19, 13, 6, 5,11, 9, 10]

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)

    while True:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(dac, GPIO.OUT)
            value = input("Put number: ")
      
            if value == "q":
                print("finish")
                break

            value = float(value)
            if 0 != (float(value) - int(value)):
                print("Число не целое")
                exit(0)
        
            value = int(value)

            if value < 0:
                print("Отрицательное")
                exit(0)

            if value > 255:
                print("Превышает")
                exit(0)

            print("Напряжение будет", (value / 255* 3.3))
            binary = to_binary(value)
            for el in binary:
                print(el)
            GPIO.output(dac, binary)
            time.sleep(4)    
        except ValueError:
            print("Это не число")    
        finally:
            GPIO.output(dac, 0)
            GPIO.cleanup()

def to_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

main()