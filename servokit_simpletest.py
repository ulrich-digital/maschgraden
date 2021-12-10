# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/blob/main/examples/servokit_simpletest.py
# Servo: https://www.adafruit.com/product/5298

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# Betätigungsbereich auf 160 Grad einzustellen
# kit.servo[0].actuation_range = 160

# Oftmals unterscheidet sich die Reichweite, die ein einzelnes Servo erkennt,
# etwas von anderen Servos. Wenn das Servo nicht den gesamten erwarteten Bereich durchläuft,
# versuchen Sie, die minimale und maximale Impulsbreite mit anzupassen
# kit.servo[0].set_pulse_width_range(1000, 2000)

kit.servo[0].angle = 180 # Servo 0 =>180 Grad
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.continuous_servo[1].throttle = -1
time.sleep(1)
kit.servo[0].angle = 0
kit.continuous_servo[1].throttle = 0
