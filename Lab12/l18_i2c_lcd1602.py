#!/usr/bin/env python

import smbus
from time import sleep

def delay(time):
    sleep(time/1000.0)

def delayMicroseconds(time):
    sleep(time/1000000.0)


class Screen():

    enable_mask = 1<<2
    rw_mask = 1<<1
    rs_mask = 1<<0
    backlight_mask = 1<<3

    data_mask = 0x00

    def __init__(self, cols = 16, rows = 2, addr=0x27, bus=1):
        self.cols = cols
        self.rows = rows        
        self.bus_num = bus
        self.bus = smbus.SMBus(self.bus_num)
        self.addr = addr
        self.display_init()
        
    def enable_backlight(self):
        self.data_mask = self.data_mask|self.backlight_mask
        
    def disable_backlight(self):
        self.data_mask = self.data_mask& ~self.backlight_mask
       
    def display_data(self, *args):
        self.clear()
        for line, arg in enumerate(args):
            self.cursorTo(line, 0)
            self.println(arg[:self.cols].ljust(self.cols))
           
    def cursorTo(self, row, col):
        offsets = [0x00, 0x40, 0x14, 0x54]
        self.command(0x80|(offsets[row]+col))
    
    def clear(self):
        self.command(0x10)

    def println(self, line):
        for char in line:
            self.print_char(char)     

    def print_char(self, char):
        char_code = ord(char)
        self.send(char_code, self.rs_mask)

    def display_init(self):
        delay(1.0)
        self.write4bits(0x30)
        delay(4.5)
        self.write4bits(0x30)
        delay(4.5)
        self.write4bits(0x30)
        delay(0.15)
        self.write4bits(0x20)
        self.command(0x20|0x08)
        self.command(0x04|0x08, delay=80.0)
        self.clear()
        self.command(0x04|0x02)
        delay(3)

    def command(self, value, delay = 50.0):
        self.send(value, 0)
        delayMicroseconds(delay)
        
    def send(self, data, mode):
        self.write4bits((data & 0xF0)|mode)
        self.write4bits((data << 4)|mode)

    def write4bits(self, value):
        value = value & ~self.enable_mask
        self.expanderWrite(value)
        self.expanderWrite(value | self.enable_mask)
        self.expanderWrite(value)        

    def expanderWrite(self, data):
        self.bus.write_byte_data(self.addr, 0, data|self.data_mask)
       

if __name__ == "__main__":
    screen = Screen(bus=1, addr=0x27, cols=16, rows=2)
    line1 = "               H"
    line2 = "              Hi"
    line3 = "             Hiy"
    line4 = "            Hiya"
    line5 = "           Hiyas"
    line6 = "          Hiyash"
    line7 = "         Hiyashi"
    line8 = "        Hiyashi "
    line9 = "       Hiyashi C"
    lineA = "      Hiyashi Ch"
    lineB = "     Hiyashi Chu"
    lineC = "    Hiyashi Chu-"
    lineD = "   Hiyashi Chu-k"
    lineE = "  Hiyashi Chu-ka"
    lineF = " Hiyashi Chu-ka "
    lineG = "Hiyashi Chu-ka A"
    lineH = "iyashi Chu-ka AR"
    lineI = "yashi Chu-ka ARI"
    lineJ = "ashi Chu-ka ARIM"
    lineK = "shi Chu-ka ARIMA"
    lineL = "hi Chu-ka ARIMAS"
    lineM = "i Chu-ka ARIMASU"
    lineN = " Chu-ka ARIMASU "
    lineO = "Chu-ka ARIMASU !"
    lineP = "hu-ka ARIMASU !!"
    lineQ = "u-ka ARIMASU !! "
    lineR = "-ka ARIMASU !!  "
    lineS = "ka ARIMASU !!   "
    lineT = "a ARIMASU !!    "
    lineU = " ARIMASU !!     "
    lineV = "ARIMASU !!      "
    lineW = "RIMASU !!       "
    lineX = "IMASU !!        "
    lineY = "MASU !!         "
    lineZ = "ASU !!          "
    line10 = "SU !!           "
    line11 = "U !!            "
    line12 = " !!             "
    line13 = "!!              "
    line14 = "!               "
    line15 = "                "
    line0 = "TEL(03)5308-8741"
    screen.enable_backlight()
    while True:
        screen.display_data(line1, line0)
        sleep(1)
        screen.display_data(line2, line0)
        sleep(1)
        screen.display_data(line3, line0)
        sleep(1)
        screen.display_data(line4, line0)
        sleep(1)
        screen.display_data(line5, line0)
        sleep(1)
        screen.display_data(line6, line0)
        sleep(1)
        screen.display_data(line7, line0)
        sleep(1)
        screen.display_data(line8, line0)
        sleep(1)
        screen.display_data(line9, line0)
        sleep(1)
        screen.display_data(lineA, line0)
        sleep(1)
        screen.display_data(lineB, line0)
        sleep(1)
        screen.display_data(lineC, line0)
        sleep(1)
        screen.display_data(lineD, line0)
        sleep(1)
        screen.display_data(lineE, line0)
        sleep(1)
        screen.display_data(lineF, line0)
        sleep(1)
        screen.display_data(lineG, line0)
        sleep(1)
        screen.display_data(lineH, line0)
        sleep(1)
        screen.display_data(lineI, line0)
        sleep(1)
        screen.display_data(lineJ, line0)
        sleep(1)
        screen.display_data(lineK, line0)
        sleep(1)
        screen.display_data(lineL, line0)
        sleep(1)
        screen.display_data(lineM, line0)
        sleep(1)
        screen.display_data(lineN, line0)
        sleep(1)
        screen.display_data(lineO, line0)
        sleep(1)
        screen.display_data(lineP, line0)
        sleep(1)
        screen.display_data(lineQ, line0)
        sleep(1)
        screen.display_data(lineR, line0)
        sleep(1)
        screen.display_data(lineS, line0)
        sleep(1)
        screen.display_data(lineT, line0)
        sleep(1)
        screen.display_data(lineU, line0)
        sleep(1)
        screen.display_data(lineV, line0)
        sleep(1)
        screen.display_data(lineW, line0)
        sleep(1)
        screen.display_data(lineX, line0)
        sleep(1)
        screen.display_data(lineY, line0)
        sleep(1)
        screen.display_data(lineZ, line0)
        sleep(1)
        screen.display_data(line11, line0)
        sleep(1)
        screen.display_data(line12, line0)
        sleep(1)
        screen.display_data(line13, line0)
        sleep(1)
        screen.display_data(line14, line0)
        sleep(1)
        screen.display_data(line15, line0)
        sleep(1)
#        screen.display_data(line, line[::-1])
#        sleep(1)
#        screen.display_data(line[::-1], line)
#        sleep(1)      
