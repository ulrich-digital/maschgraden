# import libraries 
import board
import RPi.GPIO as GPIO
import time
from pygame import mixer
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
# address = siehe Nummer auf Servo Hat => 0x[Nummer]
# kit = ServoKit(channels=16)
kit = ServoKit(address=0x47, channels=16)

# Initialise the first stepper hat on the default address
kit1 = MotorKit(address=0x61) # binary 0001 (bridge A0)

#Release the holding torque on the motor.  This reduces heating and current demand, but the motor will not actively resist rotation.
kit1.stepper1.release();   

# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
# sound settings

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("/home/pi/Music/SchwyzerNarrentanznurTambouren.mp3")

# Setting the volume
mixer.music.set_volume(1)


# SW-420 Vibration sensor with the Raspberry Pi.
# http://www.piddlerintheroot.com/vibration-sensor/

# Pin Map
# https://wiki.seeedstudio.com/Grove-Vibration_Sensor_SW-420/

#!/usr/bin/python

while True:
    
    #GPIO SETUP
    channel = 20 # Signal Vibrationssensor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    GPIO.wait_for_edge(channel, GPIO.BOTH)
    print("Input is LOW (Vibrationsalarm)")


    # Start playing the song
    mixer.music.play()
    print("Musik abspielen...")

    # http://www.piddlerintheroot.com/5v-relay/
    channel = 21 # GPIO 21 für Relais / Licht

    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    # PIN Belegung Relais:
    # NC - Pin (Normally Connected)
    # NO - Pin (Normally Open) 
    # COM - Pin (Wenn das Relais gesetzt ist, wird NC von COM getrennt und NO wird mit COM . verbunden)

    def light_on(pin):
        GPIO.output(pin, GPIO.HIGH)  # Switch Relais on (NO / COM)


    def light_off(pin):
        GPIO.output(pin, GPIO.LOW)  # Switch Relais off


    if __name__ == '__main__':
        try:
            light_on(channel)
            print("Licht an")
            # time.sleep(10) # 10 Sek.
            # light_off(channel)
            # time.sleep(1)
            # GPIO.cleanup()
        except KeyboardInterrupt:
            print("Licht aus")
            light_off(channel)
            print("Stop Musik")
            mixer.music.stop()
            GPIO.cleanup()


    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT
    # https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/blob/main/examples/servokit_all_servos_synchronised.py

    """Example that rotates servos on every channel to 180 and then back to 0."""

    # actuation range
    # https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library
    # kit.servo[0].actuation_range = 160
    """
    Rumpf_winkel = 90
    kit.servo[0].angle = Rumpf_winkel
    kit.servo[1].angle = Rumpf_winkel
    kit.servo[2].angle = Rumpf_winkel
    print("Rumpf_startWinkel", Rumpf_winkel)
    time.sleep(4)

    from sys import exit
    exit()
    """
    
    Rumpf_sek = .3 # Wartezeit nach Winkel anfahren defnieren
    Rumpf_maxValue = 28 # max value for range
    Rumpf_schrittWinkel = 3 # Winkelgrad
    Rumpf_startWinkel = 90 # Startwinkel
    print("Rumpf_startWinkel", Rumpf_startWinkel)

    for i in range(1, Rumpf_maxValue + 1):
        Rumpf_winkel = Rumpf_startWinkel - Rumpf_schrittWinkel * i # Schritte
        print(i, ":", Rumpf_winkel, "Grad") # Winkel ausgeben
        kit.servo[0].angle = Rumpf_winkel
        kit.servo[1].angle = Rumpf_winkel
        kit.servo[2].angle = Rumpf_winkel
        time.sleep(Rumpf_sek) # Warte

    Rumpf_winkel_neu = Rumpf_winkel # wird zum Zurückfahren benötigt (gleicher Winkel)
    print("Winkel", Rumpf_winkel_neu)
    
    sek = .5 # Wartezeit nach Winkel anfahren defnieren
    maxValue = 12 # max value for range (12 * 10 = 120 Grad)
    schritt =  2 # Winkelgrad
    
    # vorwärts Arm
    for i in range(1, maxValue + 1):
        winkel = i * schritt # zehner Schritte vorwärts
        print(i, winkel, " Grad") # Winkel ausgeben
        kit.servo[3].angle = winkel
        time.sleep(sek) # Warte

    # https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-stepper-motors

    # Kopfschütteln
    # 1: 60° 2: -120° 3: 120° 4: -120 5: 60°
    mSek = 1 # Millisekunden
    mSek2 = 50 # Millisekunden
    Grad = 60 # 180 Winkelgrad -> 100 / 360 Winkelgrad -> 200
    Wert = int(Grad * 5 / 9) # Umrechnung
   
    #loop stepper1 continuously forward (CCW - gegenuhrzeigersinn)
    print("Double coil steps @ stepper 1")
    for i in range(Wert):
        position = kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        # kit1.stepper1.onestep(style=stepper.MICROSTEP)
        print("Position in microsteps", position)
        time.sleep(mSek / 1000)
        
    time.sleep(mSek2 / 1000)
    
    #loop stepper1 continuously backward (CW - uhrzeigersinn)
    Grad = 120
    Wert = int(Grad * 5 / 9)
    print("Double coil steps @ stepper 1")
    for i in range(Wert):
        position = kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        print("Position in microsteps", position)
        time.sleep(mSek / 1000)
        
    time.sleep(mSek2 / 1000)
    
   
    Grad = 120
    Wert = int(Grad * 5 / 9)
    #loop stepper1 continuously forward (CCW - gegenuhrzeigersinn)
    print("Double coil steps @ stepper 1")
    for i in range(Wert):
        position = kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        # kit1.stepper1.onestep(style=stepper.MICROSTEP)
        print("Position in microsteps", position)
        time.sleep(mSek / 1000)
        
    time.sleep(mSek2 / 1000)
    
    Grad = 120
    Wert = int(Grad * 5 / 9)
    #loop stepper1 continuously backward (CW - uhrzeigersinn)
    print("Double coil steps @ stepper 1")
    for i in range(Wert):
        position = kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        print("Position in microsteps", position)
        time.sleep(mSek / 1000)
        
    time.sleep(mSek2 / 1000)
    
    Grad = 60
    Wert = int(Grad * 5 / 9)
    #loop stepper1 continuously forward (CCW - gegenuhrzeigersinn)
    print("Double coil steps @ stepper 1")
    for i in range(Wert):
        position = kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        # kit1.stepper1.onestep(style=stepper.MICROSTEP)
        print("Position in microsteps", position)
        time.sleep(mSek / 1000)
        
    time.sleep(mSek2 / 1000)    
        
    # loop stepper2 continuously forward
    """
    print("Double coil steps @ stepper 2")
    for i in range(Grad):
        kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(mSek / 1000)
    """
        
    #loop stepper2 continuously backward
    """
    print("Double coil steps @ stepper 2")
    for i in range(Grad):
        kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(mSek / 1000)
    """
    # stop music
    mixer.music.stop()
    print("Ton aus")
    
    print("Licht aus")
    light_off(channel)

    # rückwärts Arm
    sek = .5 # Wartezeit nach Winkel anfahren defnieren
    maxValue = 12 # max value for range (12 * 10 = 120 Grad)
    schritt =  2 # Winkelgrad
    for i in range(1, maxValue + 1):
        winkel = schritt * maxValue - schritt * i # zehner Schritte rückwärts
        print(i, winkel, " Grad") # Winkel ausgeben
        kit.servo[3].angle = winkel
        time.sleep(sek) # Warte

    # Rumpf gegen uhrzeigersinn CCW
    for i in range(1, Rumpf_maxValue + 1):
        Rumpf_winkel = Rumpf_winkel_neu + Rumpf_schrittWinkel * i # Schritte
        print(i, ":", Rumpf_winkel, "Grad") # Winkel ausgeben
        kit.servo[0].angle = Rumpf_winkel
        kit.servo[1].angle = Rumpf_winkel
        kit.servo[2].angle = Rumpf_winkel
        time.sleep(Rumpf_sek) # Warte




    # relais / light off

    time.sleep(1)
    GPIO.cleanup()



    wartezeit = 20
    print("Warte für", wartezeit, "Sekunden")
    time.sleep(wartezeit) # Warte für 20 Sekunden
    
    
    
    # programm beenden
    from sys import exit
    exit()

