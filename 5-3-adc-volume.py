import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def dec2bin(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

def adc():
    exp = 128
    n = 0
    while(exp > 0):
        n += exp
        GPIO.output(dac, dec2bin(n))
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            n -= exp
        exp //= 2
    return n

def volume(val):
    val = int(val/256*10)
    arr = [0]*8
    for i in range(val - 1):
        arr[i] = 1
    return arr

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256.0
        if i:
            volume_val = volume(i)
            GPIO.output(led, volume_val)
            print(int(i/256*10))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()