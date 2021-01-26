#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

Trigger = 16
Echo = 18

def checkdist():
    GPIO.output(Trigger, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trigger, GPIO.LOW)
    while not GPIO.input(Echo):
        pass
    t1 = time.time()
    while GPIO.input(Echo):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trigger,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo,GPIO.IN)

try:
    while True:
        d = checkdist()
        df = "%0.2f" %d
        print ('Distance: %s m' %df)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print ('GPIO cleeanup and end!')