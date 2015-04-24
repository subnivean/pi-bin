#!/usr/bin/python
# Example using a character LCD plate.
import math
import socket
import subprocess
import time

import Adafruit_CharLCD as LCD

lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

for i in range(10):
    ipadd = subprocess.check_output(['/bin/hostname', '-I'])
    if ipadd.strip() == '':
        ipadd = '???.???.???.???'
    else:
        break
    time.sleep(1)

lcd.set_color(0.0, 1.0, 1.0)
lcd.clear()
lcd.message(ipadd)

MAXSLEEP = 30  # Button hold ticks before reboot/halt
REBOOT = '/sbin/reboot'
HALT   = '/sbin/halt'

sleepcnt = 0
while True:
    if lcd.is_pressed(LCD.UP) and lcd.is_pressed(LCD.SELECT):
        # 'Reboot' button hold
        sleepcnt += 1
        if sleepcnt == MAXSLEEP:
            lcd.clear()
            lcd.set_color(1.0, 1.0, 0.0)
            lcd.message("Rebooting system")
            time.sleep(2.0)
            lcd.enable_display(False)
            lcd.clear()
            lcd.set_backlight(0)
            output = subprocess.check_output([REBOOT])
            break
    elif lcd.is_pressed(LCD.DOWN) and lcd.is_pressed(LCD.SELECT):
        # 'Halt' button hold
        sleepcnt += 1
        if sleepcnt == MAXSLEEP:
            lcd.clear()
            lcd.set_color(1.0, 0.0, 0.0)
            lcd.message("Halting system...")
            time.sleep(2.0)
            lcd.clear()
            lcd.set_backlight(0)
            output = subprocess.check_output([HALT])
            break
    else:
        sleepcnt = 0

    time.sleep(0.1)  # Lowers the CPU load
