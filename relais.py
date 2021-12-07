# http://www.piddlerintheroot.com/5v-relay/
import RPi.GPIO as GPIO
import time

channel = 21 # GPIO 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# PIN Belegung Relais:
# NC - Pin (Normally Connected)
# NO - Pin (Normally Open) 
# COM - Pin (Wenn das Relais gesetzt ist, wird NC von COM getrennt und NO wird mit COM . verbunden)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Switch Relais on (NO / COM)


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Switch Relais off


if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
