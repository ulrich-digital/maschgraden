# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/blob/main/examples/servokit_all_servos_sequential.py

"""Example that iterates through a servo on every channel, sets 10 Degrees steps to 180 and then back to 0."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

for i in range(len(kit.servo)):  # pylint: disable=consider-using-enumerate
    kit.servo[i].angle = 10
    time.sleep(1)
    kit.servo[i].angle = 20
    time.sleep(1)
    kit.servo[i].angle = 30
    time.sleep(1)
    kit.servo[i].angle = 40
    time.sleep(1)
    kit.servo[i].angle = 50
    time.sleep(1)
    kit.servo[i].angle = 60
    time.sleep(1)
    kit.servo[i].angle = 70
    time.sleep(1)
    kit.servo[i].angle = 80
    time.sleep(1)
    kit.servo[i].angle = 90
    time.sleep(1)
    kit.servo[i].angle = 100
    time.sleep(1)
    kit.servo[i].angle = 110
    time.sleep(1)
    kit.servo[i].angle = 120
    time.sleep(1)
    kit.servo[i].angle = 130
    time.sleep(1)
    kit.servo[i].angle = 140
    time.sleep(1)
    kit.servo[i].angle = 150
    time.sleep(1)
    kit.servo[i].angle = 160
    time.sleep(1)
    kit.servo[i].angle = 170
    time.sleep(1)
    kit.servo[i].angle = 180
    time.sleep(1)
    kit.servo[i].angle = 0
    time.sleep(1)
