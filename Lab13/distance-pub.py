#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

###### Edit variables to your environment #######
broker_address = "test.mosquitto.org"     #MQTT broker_address :192.168.0.31
Topic = "piper-jp"

Trigger = 16
Echo = 18

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trigger, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo ,GPIO.IN)

print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

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

def loop():
    while True:
        d = checkdist()
        df = "%0.2f" %d
        print ('Distance: %s m' % df)
        client.publish(Topic, df)
        time.sleep(2)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print ('The end !!')
