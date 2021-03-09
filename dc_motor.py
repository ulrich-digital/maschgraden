## Sytem (Tastendruck usw.)
import sys
import termios
import tty
inkey_buffer = 1

## Adafruit
import time
import board
from adafruit_motorkit import MotorKit
 
##
while 1:
    key = (inkey())
    if key in ['w','a','s','d']:
        print key
        kit.motor1.throttle = 0.0

    if key == 'q':
        exit()
      
 
kit = MotorKit(i2c=board.I2C())
 
kit.motor1.throttle = 1.0
time.sleep(1)
kit.motor1.throttle = 10.0
kit.motor1.throttle = 0.0
