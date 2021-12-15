# MP3 playing
# https://www.it-swarm.com.de/de/python/wie-kann-ich-ein-mp3-mit-pygame-abspielen/939825751/

import pygame
file = '/home/pi/Music/audio.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()


# Wav playing
# https://brightersidetech.com/play-music-and-audio-file-in-python/

"""
import os, time
from pygame import mixer

def playSound():
    # Initialize pygame mixer
    mixer.init()
    # Load the sounds
    sound = mixer.Sound('/home/pi/Music/PinkPanther60.wav')
    # play sounds
    sound.play()
    # wait for sound to finish playing
    time.sleep(3)

if __name__ == '__main__':
    while(True):
        playSound() 
        time.sleep(10)
"""
