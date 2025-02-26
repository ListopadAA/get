import RPi.GPIO as GPIO
import time

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

x = 0

try:
    period = float(input("Type a period: "))

    while True:
        print(x)
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            flag = 1
        elif x == 255:
            flag = 0
        
        if flag:
            x = x + 1
        else:
            x = x - 1
        
        time.sleep(period/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()