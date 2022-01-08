# import libraries 
import board # stepper
import RPi.GPIO as GPIO
import time
import random
from pygame import mixer # sound
# from adafruit_motor import stepper # stepper
# from adafruit_motorkit import MotorKit # stepper
from adafruit_servokit import ServoKit # servo

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
# address = siehe Nummer auf Servo Hat => 0x[Nummer]
# kit = ServoKit(channels=16)
# kit46 = ServoKit(address=0x46, channels=16)
kit47 = ServoKit(address=0x47, channels=16)
kit46 = ServoKit(address=0x47, channels=16)

"""
time.sleep(4)
print("Programm beenden")
from sys import exit
exit()

kit47.servo[3].angle = 0
kit47.servo[9].angle = 0
kit47.servo[10].angle = 0
time.sleep(4)
kit47.servo[3].angle = 90
kit47.servo[9].angle = 90
kit47.servo[10].angle = 90
time.sleep(4)
kit47.servo[0].angle = 0
kit47.servo[1].angle = 0
kit47.servo[2].angle = 0
time.sleep(4)
kit47.servo[0].angle = 90
kit47.servo[1].angle = 90
kit47.servo[2].angle = 90
time.sleep(4)
"""
# programm beenden
# print("Programm beenden")
# from sys import exit
#exit()
# sevos kit 0x47:
# 0-2 -> Rumpf
# 3 -> Arm
# 4 -> Hand
# 5 -> Kopf

# Domino
#servo kit 0x46 PINs:
# 8/9/10 -> Rumpf
# 15 -> Arm
# 12 -> Kopf


# Parameter Rumpf47
Rumpf47_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Rumpf47_schrittWinkel = 3 # Winkelgrad
Rumpf47_startWinkel = 90 # Startwinkel
Rumpf47_servo1 = 0 # PINs
Rumpf47_servo2 = 1
Rumpf47_servo3 = 2

# Parameter Rumpf46
Rumpf46_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Rumpf46_schrittWinkel = 2 # Winkelgrad
Rumpf46_startWinkel = 90 # Startwinkel
Rumpf46_servo1 = 8 # PINs
Rumpf46_servo2 = 9
Rumpf46_servo3 = 10

# Paramter Arm47 nachlassen
Arm47_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Arm47_maxValue = 28 # max value for range
Arm47_schrittWinkel = 1 # Winkelgrad
Arm47_startWinkel = 28 # Startwinkel
Arm47_warte = 3
Arm47_servo = 3 # PIN

# Paramter Arm46 nachlassen
Arm46_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Arm46_maxValue = 28 # max value for range
Arm46_schrittWinkel = 2 # Winkelgrad
Arm46_startWinkel = 90 # Startwinkel
Arm46_warte = 3
Arm46_servo = 15 # PIN

# Paramter Arm47 heben
Arm47Hub_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Arm47Hub_maxValue = 45 # max value for range
Arm47Hub_schrittWinkel = 3 # Winkelgrad
Arm47Hub_startWinkel = 0 # Startwinkel
Arm47Hub_warte = 2 # Sekunden
Arm47Hub_servo = 3 # Pin
# kit47.servo[Arm47_servo].angle = 90

# Paramter Arm46 heben
Arm46Hub_sek = .05 # Wartezeit nach Winkel anfahren defnieren
Arm46Hub_schrittWinkel = 3 # Winkelgrad
Arm46Hub_startWinkel = 180 # Startwinkel
Arm46Hub_warte = 2 # Sekunden
Arm46Hub_servo = 15 # Pin

# Paramter Hand
Servo_1109mg_maxWinkel = 180
Servo_1109mg_minWinkel = 0
Hand_sek = .004 # Wartezeit nach Winkel anfahren defnieren
Hand_Value_min = 45 # min value for range
Hand_Value_max = 45 # max value for range
Hand_schrittWinkel = 2 # Winkelgrad
Hand_startWinkel = 90 # Startwinkel (Mitte)
Hand_warte = 0.25 # Wartezeit nach Drehung

#Kopf47 drehen
Servo_Kopf47_maxWinkel = 180
Servo_Kopf47_minWinkel = 0
KopfDrehen47_sek = .005 # Wartezeit nach Winkel anfahren defnieren
KopfDrehen47_Value_min = 35 # min value for range * 2
KopfDrehen47_Value_max = 35 # max value for range * 2
KopfDrehen47_schrittWinkel = 1 # Winkelgrad
KopfDrehen47_startWinkel = 90 # Startwinkel (Mitte)
KopfDrehen47_warte = 0.2 # Wartezeit nach Drehung
Kopf47_servo = 5

#Kopf46 drehen
Servo_Kopf46_maxWinkel = 180
Servo_Kopf46_minWinkel = 0
KopfDrehen46_sek = .005 # Wartezeit nach Winkel anfahren defnieren
KopfDrehen46_Value_min = 35 # min value for range * 2
KopfDrehen46_Value_max = 35 # max value for range * 2
KopfDrehen46_schrittWinkel = 1 # Winkelgrad
KopfDrehen46_startWinkel = 90 # Startwinkel (Mitte)
KopfDrehen46_warte = 0.2 # Wartezeit nach Drehung
Kopf46_servo = 12

#Kopf47 schütteln
Servo_Kopf47_maxWinkel = 180
Servo_Kopf47_minWinkel = 0
Kopf47_sek = .003 # Wartezeit nach Winkel anfahren defnieren
Kopf47_Value_min = 35 # min value for range * 2
Kopf47_Value_max = 35 # max value for range * 2
Kopf47_schrittWinkel = 1 # Winkelgrad
Kopf47_startWinkel = 90 # Startwinkel (Mitte)
Kopf47_warte = 0.2 # Wartezeit nach Drehung
Kopf47_servo = 5

Servo_Kopf46_maxWinkel = 180
Servo_Kopf47_minWinkel = 0
Kopf46_sek = .003 # Wartezeit nach Winkel anfahren defnieren
Kopf46_Value_min = 35 # min value for range * 2
Kopf46_Value_max = 35 # max value for range * 2
Kopf46_schrittWinkel = 1 # Winkelgrad
Kopf46_startWinkel = 90 # Startwinkel (Mitte)
Kopf46_warte = 0.2 # Wartezeit nach Drehung
Kopf46_servo = 12


kit46.servo[3].angle = 0
kit47.servo[15].angle = 180

# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
# sound settings
# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("/home/pi/Music/SchwyzerNarrentanznurTambouren.mp3")
# Setting the volume
mixer.music.set_volume(1)

# http://www.piddlerintheroot.com/5v-relay/
# PIN Belegung Relais:
# NC - Pin (Normally Connected)
# NO - Pin (Normally Open) 
# COM - Pin (Wenn das Relais gesetzt ist, wird NC von COM getrennt und NO wird mit COM . verbunden)

def light_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)  # Switch Relais on (NO / COM)
    print("Licht an")

def light_off(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Switch Relais off
    print("Licht aus")
    
def func_mountbody():
    print ("Aufsitzen:")
    
    light_on(21) # Licht an
    print("Licht an...")
    
    # Start playing the song
    mixer.music.play()
    print("Musik abspielen...")


    loop1_count = 28

    # Rumpf auf und Arm nachlassen
    for i in range(1, loop1_count):
        Rumpf47_winkel = Rumpf47_startWinkel - Rumpf47_schrittWinkel * i # Schritte
        Rumpf46_winkel = Rumpf46_startWinkel - Rumpf46_schrittWinkel * i # Schritte
        
        print(Rumpf47_winkel)
        
        Arm47_winkel = Arm47_startWinkel - i * Arm47_schrittWinkel # vorwärts
        Arm46_winkel = Arm46_startWinkel + i * Arm46_schrittWinkel # vorwärts
        
        # Rumpf 47
        kit47.servo[Rumpf47_servo1].angle = Rumpf47_winkel
        kit47.servo[Rumpf47_servo2].angle = Rumpf47_winkel
        kit47.servo[Rumpf47_servo3].angle = Rumpf47_winkel
        # Rumpf 46
        kit46.servo[Rumpf46_servo1].angle = Rumpf46_winkel
        kit46.servo[Rumpf46_servo2].angle = Rumpf46_winkel
        kit46.servo[Rumpf46_servo3].angle = Rumpf46_winkel
        
        #kit47.servo[Arm47_servo].angle = Arm47_winkel
        #kit46.servo[Arm46_servo].angle = Arm46_winkel
        
        time.sleep(Rumpf47_sek) # Warte

    time.sleep(0.5)

    Rumpf47_winkel_neu = Rumpf47_winkel # wird zum Zurückfahren benötigt (gleicher Winkel)
    Rumpf46_lastPosition = Rumpf46_winkel

    Arm47_lastPosition = Arm47_winkel # wird zum Zurückfahren benötigt (gleicher Winkel)
    Arm46_lastPosition = Arm46_winkel
    
    kit47.servo[3].angle = 100
    kit46.servo[15].angle = 90
    
    time.sleep(2)

    # Kopfdrehen *******************************************************************************************************
    # nach links
    for i in range(1, KopfDrehen47_Value_min):
        KopfDrehen47_winkel = KopfDrehen47_startWinkel + i * KopfDrehen47_schrittWinkel # 45° gegenuhrzeigersinn
        KopfDrehen46_winkel = KopfDrehen46_startWinkel - i * KopfDrehen46_schrittWinkel # 45° gegenuhrzeigersinn
        kit47.servo[Kopf47_servo].angle = KopfDrehen47_winkel
        kit46.servo[Kopf46_servo].angle = KopfDrehen46_winkel
        time.sleep(KopfDrehen47_sek) # Warte

    KopfDrehen47_lastDrehPosition = KopfDrehen47_winkel
    KopfDrehen46_lastDrehPosition = KopfDrehen46_winkel
    time.sleep(KopfDrehen47_warte)

    # Arm heben *******************************************************************************************************
    """
    for i in range(1, Arm47Hub_maxValue):
        Arm47Hub_winkel = Arm47_lastPosition + i * Arm47Hub_schrittWinkel # vorwärts
        Arm46Hub_winkel = Arm46_lastPosition - i * Arm46Hub_schrittWinkel # vorwärts
        print("Arm46Hub_winkel", Arm46Hub_winkel)
        kit47.servo[Arm47Hub_servo].angle = Arm47Hub_winkel
        kit46.servo[Arm46Hub_servo].angle = Arm46Hub_winkel
        time.sleep(Arm47Hub_sek) # Warte

    Arm47_lastPosition = Arm47Hub_winkel # wird zum Zurückfahren benötigt (gleicher Winkel)
    Arm46_lastPosition = Arm46Hub_winkel
    print(Arm47_lastPosition, "°") # Winkel ausgeben
    time.sleep(0.5)
    """
    # Hand drehen *******************************************************************************************************
    # Pin 4

    # nach links
    for i in range(1, Hand_Value_min):
        Hand_winkel = Hand_startWinkel + i * Hand_schrittWinkel # 45° gegenuhrzeigersinn
        if Hand_winkel < Servo_1109mg_minWinkel or Hand_winkel > Servo_1109mg_maxWinkel:
            break
        kit47.servo[4].angle = Hand_winkel
        time.sleep(Hand_sek) # Warte

    time.sleep(Hand_warte)

    for _ in range(2):
        # nach rechts
        for i in range(1, Hand_Value_max):
            Hand_winkel = Hand_startWinkel - i * Hand_schrittWinkel # 180° imuhrzeigersinn
            if Hand_winkel < Servo_1109mg_minWinkel or Hand_winkel > Servo_1109mg_maxWinkel:
                break
            kit47.servo[4].angle = Hand_winkel
            time.sleep(Hand_sek) # Warte
            
        time.sleep(Hand_warte)

        # nach links
        for i in range(1, Hand_Value_max):
            Hand_winkel = Hand_startWinkel + i * Hand_schrittWinkel # 180° imuhrzeigersinn
            if Hand_winkel < Servo_1109mg_minWinkel or Hand_winkel > Servo_1109mg_maxWinkel:
                break
            kit47.servo[4].angle = Hand_winkel
            time.sleep(Hand_sek) # Warte

        time.sleep(Hand_warte)


    Hand_winkel_neu = Hand_winkel # wird zum Zurückfahren benötigt (gleicher Winkel)

    # Hand zurückdrehen *******************************************************************************************************
    # Pin 4
    # nach rechts
    for i in range(1, Hand_Value_min):
        Hand_winkel = Hand_winkel_neu - i * Hand_schrittWinkel # vorwärts
        if Hand_winkel < Servo_1109mg_minWinkel or Hand_winkel > Servo_1109mg_maxWinkel:
            break
        kit47.servo[4].angle = Hand_winkel
        time.sleep(Hand_sek) # Warte

    # Kopf zurückdrehen *******************************************************************************************************
    for i in range(1, KopfDrehen47_Value_min):
        KopfDrehen47_winkel = KopfDrehen47_lastDrehPosition - i * KopfDrehen47_schrittWinkel # 45° gegenuhrzeigersinn
        KopfDrehen46_winkel = KopfDrehen46_lastDrehPosition + i * KopfDrehen46_schrittWinkel # 45° gegenuhrzeigersinn
        if KopfDrehen47_winkel < Servo_Kopf47_minWinkel or KopfDrehen47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = KopfDrehen47_winkel
        kit46.servo[Kopf46_servo].angle = KopfDrehen46_winkel
        time.sleep(KopfDrehen47_sek) # Warte

    time.sleep(KopfDrehen47_warte)


    # Arm auf Ausgangsposition ************************************************************************************************
    """
    for i in range(1, Arm47Hub_maxValue):
        Arm47Hub_winkel = Arm47_lastPosition - i * Arm47Hub_schrittWinkel # rückwärts
        print(Arm47Hub_winkel)
        Arm46Hub_winkel = Arm46_lastPosition + i * Arm46Hub_schrittWinkel # rückwärts
        kit47.servo[Arm47Hub_servo].angle = Arm47Hub_winkel
        kit46.servo[Arm46Hub_servo].angle = Arm46Hub_winkel #hier
        time.sleep(Arm47Hub_sek) # Warte


    Arm47_lastPosition = Arm47Hub_winkel
    Arm46_lastPosition = Arm46Hub_winkel

    time.sleep(1)
    """

    # Rumpf gegen uhrzeigersinn CCW *******************************************************************************************
    loop2_count = 28
    for i in range(1, loop2_count):
        Rumpf47_winkel = Rumpf47_winkel_neu + Rumpf47_schrittWinkel * i # Schritte
        Rumpf46_winkel = Rumpf46_lastPosition + Rumpf46_schrittWinkel * i # Schritte
        
        Arm47_winkel = Arm47_lastPosition + i * Arm47_schrittWinkel # vorwärts
        Arm46_winkel = Arm46_lastPosition - i * Arm46_schrittWinkel # vorwärts
        
        kit47.servo[Rumpf47_servo1].angle = Rumpf47_winkel
        kit47.servo[Rumpf47_servo2].angle = Rumpf47_winkel
        kit47.servo[Rumpf47_servo3].angle = Rumpf47_winkel
        
        kit46.servo[Rumpf46_servo1].angle = Rumpf46_winkel
        kit46.servo[Rumpf46_servo2].angle = Rumpf46_winkel
        kit46.servo[Rumpf46_servo3].angle = Rumpf46_winkel    
        
        # kit47.servo[Arm47_servo].angle = Arm47_winkel
        # kit47.servo[Arm47_servo].angle = Arm46_winkel
        
        time.sleep(Rumpf47_sek) # Warte

    # stop music
    mixer.music.stop()
    print("Ton aus")
    
    # relais / light off
    light_off(21)
    print ("Licht aus")

    time.sleep(2)
    # reset winkel (immer zurückstellen)

    kit46.servo[Rumpf46_servo1].angle = 90
    kit46.servo[Rumpf46_servo2].angle = 90
    kit46.servo[Rumpf46_servo3].angle = 90
    kit46.servo[Kopf46_servo].angle = 90

    kit47.servo[Arm47Hub_servo].angle = 0
    kit47.servo[Arm46Hub_servo].angle = 180

def func_shakehead():
    print ("Kopfschütteln:") # Kopfschütteln
    
    light_on(21) # Licht an


    # Kopf schütteln *******************************************************************************************************
    # Pin 5 & 12

    # nach links
    for i in range(1, Kopf47_Value_min):
        Kopf47_winkel = Kopf47_startWinkel - i * Kopf47_schrittWinkel # 90° imuhrzeigersinn
        Kopf46_winkel = Kopf46_startWinkel - i * Kopf46_schrittWinkel # 90° imuhrzeigersinn
        if Kopf47_winkel < Servo_Kopf47_minWinkel or Kopf47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = Kopf47_winkel
        kit46.servo[Kopf46_servo].angle = Kopf46_winkel
        time.sleep(Kopf47_sek) # Warte

    print(i, Kopf47_winkel, "°") # Winkel ausgeben
    time.sleep(Kopf47_warte/4)

    # nach rechts
    for i in range(1, Kopf47_Value_max):
        Kopf47_winkel = Kopf47_startWinkel + i * Kopf47_schrittWinkel # 180° gegenuhrzeigersinn
        Kopf46_winkel = Kopf46_startWinkel + i * Kopf46_schrittWinkel # 180° gegenuhrzeigersinn
        if Kopf47_winkel < Servo_Kopf47_minWinkel or Kopf47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = Kopf47_winkel
        kit46.servo[Kopf46_servo].angle = Kopf46_winkel
        time.sleep(Kopf47_sek) # Warte

    print(i, Kopf47_winkel, "°") # Winkel ausgeben
    time.sleep(Kopf47_warte)

    # nach links
    for i in range(1, Kopf47_Value_max):
        Kopf47_winkel = Kopf47_startWinkel - i * Kopf47_schrittWinkel # 180° imuhrzeigersinn
        Kopf46_winkel = Kopf46_startWinkel - i * Kopf46_schrittWinkel # 180° imuhrzeigersinn
        if Kopf47_winkel < Servo_Kopf47_minWinkel or Kopf47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = Kopf47_winkel
        kit46.servo[Kopf46_servo].angle = Kopf46_winkel
        time.sleep(Kopf47_sek) # Warte

    print(i, Kopf47_winkel, "°") # Winkel ausgeben
    time.sleep(Kopf47_warte)

    # nach rechts
    for i in range(1, Kopf47_Value_max):
        Kopf47_winkel = Kopf47_startWinkel + i * Kopf47_schrittWinkel # 180° gegenuhrzeigersinn
        Kopf46_winkel = Kopf46_startWinkel + i * Kopf46_schrittWinkel # 180° gegenuhrzeigersinn
        if Kopf47_winkel < Servo_Kopf47_minWinkel or Kopf47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = Kopf47_winkel
        kit46.servo[Kopf46_servo].angle = Kopf46_winkel
        time.sleep(Kopf47_sek) # Warte

    print(i, Kopf47_winkel, "°") # Winkel ausgeben
    time.sleep(Kopf47_warte)

    # nach links
    for i in range(1, Kopf47_Value_max):
        Kopf47_winkel = Kopf47_startWinkel - i * Kopf47_schrittWinkel # 180° imuhrzeigersinn
        Kopf46_winkel = Kopf46_startWinkel - i * Kopf46_schrittWinkel # 180° imuhrzeigersinn
        if Kopf47_winkel < Servo_Kopf47_minWinkel or Kopf47_winkel > Servo_Kopf47_maxWinkel:
            break
        kit47.servo[Kopf47_servo].angle = Kopf47_winkel
        kit46.servo[Kopf46_servo].angle = Kopf46_winkel
        time.sleep(Kopf47_sek) # Warte

    print(i, Kopf47_winkel, "°") # Winkel ausgeben
    time.sleep(Kopf47_warte)

    # Kopf zurückdrehen *******************************************************************************************************
    # Pin 4
    # nach rechts
    kit47.servo[Kopf47_servo].angle = 90 # Mitte
    kit46.servo[Kopf46_servo].angle = 90 # Mitte
    print("90°") # Winkel ausgeben
    time.sleep(.5)

    time.sleep(5)
    light_off(21) # Licht aus


while True:

    # SW-420 Vibration sensor with the Raspberry Pi.
    # http://www.piddlerintheroot.com/vibration-sensor/

    # Pin Map
    # https://wiki.seeedstudio.com/Grove-Vibration_Sensor_SW-420/
    
    #GPIO SETUP
    channel_vibr = 20 # Signal Vibrationssensor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel_vibr, GPIO.IN)
    
    #func_shakehead()
    #func_mountbody()
    # programm beenden
    print("Programm beenden")
    from sys import exit
    exit()
    
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    GPIO.wait_for_edge(channel_vibr, GPIO.BOTH)
    print("Input is LOW => Vibrationsalarm!!!")

    # my_list = [func_shakehead, func_mountbody]
    my_list = [func_shakehead, func_mountbody]
    random.choice(my_list)() # function func_shakehead oder func_mountbody nach Zufall aufrufen 

    # release -> Motor/Spulen ohne Strom (zum Drehen des Kopfes verwenden) 
    # https://forums.adafruit.com/viewtopic.php?f=50&t=185502&p=899416&hilit=stepper+release#p899416
    # kit1.stepper1.release(); 

    GPIO.cleanup()

    wartezeit = 1 # Sekunden
    print("Warte für", wartezeit, "Sekunden")
    time.sleep(wartezeit) # Warte für 20 Sekunden
        
    




