import time
import board
from adafruit_motorkit import MotorKit
 
kit = MotorKit(i2c=board.I2C())
 
kit.motor1.throttle = 1.0
time.sleep(1)
kit.motor1.throttle = 1.0
kit.motor1.throttle = 0.0
