#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

BZRPin = 11

GPIO.setmode(GPIO.BOARD) # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT) # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)
p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ
p.start(50) # Duty cycle: 50%
try:
    while True:
        for f in range(220, 880, 10):
            p.ChangeFrequency(f)
            time.sleep(0.01)

        for f in range(0, 4):
            p.ChangeFrequency(923.32)
            time.sleep(0.2)
            p.ChangeFrequency(880)
            time.sleep(0.2)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    print('-- cleanup GPIO/PWM! --')