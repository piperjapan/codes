#!/usr/bin/env python

import RPi.GPIO as GPIO
import l20_ds18b20
import l20_i2c_lcd1602
import time

screen = l20_i2c_lcd1602.Screen(bus=1, addr=0x27, cols=16, rows=2)

def destory():
   GPIO.cleanup()

def loop():
    while True:
       screen.cursorTo(0, 0)
       screen.println(line)
       t = l20_ds18b20.l20_dsb20Read()
       t = round(t, 2)
       m = '%f' %t
       m = m[:5]
       screen.cursorTo(1, 0)
       screen.println(' Temp: ' + m + ' C  ')
       screen.clear()
       time.sleep(1)      

if __name__ == '__main__':
   line = " Piper4Partner  "
   screen.enable_backlight()
   screen.clear()
   try:
      loop()
   except KeyboardInterrupt:
      destory()
