# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-stepper-motors

# import and initialize the MotorKit
print("import and initialize the MotorKit")

import time
import board

from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Initialise the first hat on the default address
kit0 = MotorKit() # binary 0000 (no jumpers required)

# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/stacking-hats

# Initialise the second hat on a different address
# kit1 = MotorKit(address=0x61) # binary 0001 (bridge A0)

# Initialise the third hat on a different address
# kit2 = MotorKit(address=0x62) # binary 0010 (bridge A1, the one above A0)

# Initialise the third hat on a different address
# kit3 = MotorKit(address=0x63) # binary 0011 (bridge A0 & A1, two bottom jumpers)

# Initialise the third hat on a different address
# kit4 = MotorKit(address=0x64) # binary 0100 (bridge A2, middle jumper)

# stepper1 -> M1
# stepper2 -> M2

# direction, which should be one of the following constant values:
# stepper.FORWARD (default)
# stepper.BACKWARD
# style, which should be one of the values:
# stepper.SINGLE (default) for a full step rotation to a position where one single coil is powered
# stepper.DOUBLE for a full step rotation to position where two coils are powered providing more torque
# stepper.INTERLEAVE for a half step rotation interleaving single and double coil positions and torque
# stepper.MICROSTEP for a microstep rotation to a position where two coils are partially active
# release() which releases all the coils so the motor can free spin, and also won't use any power

#loop stepper1 continuously forward
print("Double coil steps @ stepper 1")
for i in range(220):
    kit0.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    time.sleep(0.04)
    
# loop stepper2 continuously forward
print("Double coil steps @ stepper 2")
for i in range(220):
    kit0.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    time.sleep(0.04)
    
#loop stepper1 continuously backward
print("Double coil steps @ stepper 1")
for i in range(220):
    kit0.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(0.01)
    
#loop stepper2 continuously backward
print("Double coil steps @ stepper 2")
for i in range(220):
    kit0.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(0.01)




