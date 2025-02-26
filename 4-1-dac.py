import RPi.GPIO as GPIO

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        inp = input("Enter a numder from 0 to 255: ")

        try:
            num = int(inp)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                volt = float(num) / 256.0 * 3.3
                print(f"Output voltage is {volt:.4} V")
            else:
                if num < 0:
                    print("Num have to be >= 0!")
                elif num > 255:
                    print("Num is out of range [0; 255]!")
        except Exception:
            if inp == "q":
                break
            if not inp.isdigit() and not inp.isalpha():
                print("You have to enter an integer number, not float!")
            else:
                print("You have to enter a number, not string!")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()