#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(15, GPIO.OUT)       # Set pin mode as output
GPIO.output(15, GPIO.HIGH)     # Set pin to high(+3.3V) to off the led

for i in range(1,10):
        
        print ('...led on')
        GPIO.output(15, GPIO.LOW)  # led on
        time.sleep(0.5)
        
        print ('led off...')
        GPIO.output(15, GPIO.HIGH) # led off
        time.sleep(0.5)

GPIO.output(15, GPIO.HIGH)     # led off
GPIO.cleanup()                 # Release resource

