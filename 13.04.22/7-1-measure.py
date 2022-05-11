import matplotlib.pyplot as plot
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

    volt_list = list()
    time_list = list()

    try:
        start = time.time()
        GPIO.output(troyka, GPIO.LOW)
        voltage = 0


        GPIO.output(17, 1)
        while voltage / 3.3 <= 0.92:
            bit = adc()
            voltage = bit * 3.3 / 255

            print(voltage)
            end = time.time()
            ex_time = end - start
            time_list.append(ex_time)
            volt_list.append(voltage) 

        GPIO.output(17, 0)
        while voltage / 3.3 >= 0.07:
            bit = adc()
            voltage = bit * 3.3 / 255

            end = time.time()
            ex_time = end - start
            time_list.append(ex_time)
            print(voltage)
            volt_list.append(voltage) 

        
        plot.plot(time_list, volt_list)
        plot.show()

    except ValueError:
        print("Uncorrect")
    finally:
        GPIO.output(dac, 0)
        GPIO.cleanup()
    
    volt_str = [str(item) for item in volt_list]
    with open("7-1-dats.txt",'w') as file:
        file.write("\n".join(volt_str))

    with open("7-1-param.txt", 'w') as file:
        file.write("period {:.5f} sec\n".format(ex_time/len(volt_list)))
        file.write("quant step: {:.5f} V\n".format(3.3/256))
    return 
def num2dac(value):
    signal = to_binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    list = [0] * 8
    for i in range(0,8):
        list[i] = 1
        GPIO.output(dac, list)
        time.sleep(0.001)

        if(GPIO.input(comp) == 0):
            list[i] = 0
    return to_dec(list)

def to_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]    

def to_dec(list):
    weight = 128
    val = 0
    for i in range(0, 8):
        val += weight * list[i]
        weight = weight / 2
    return val

main()