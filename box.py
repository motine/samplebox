#!/usr/bin/env python3

# docs: http://devdocs.io/python~3.5/

import os
import pygame

SOUND_PINS = [11,12,13,15]
SHIFT_PIN = 16 # TODO document function
CTRL_PIN = 18 # TODO document function

NUMBER_OF_SOUNDS = len(SOUND_PINS) * 2 # double the number of sounds, because we can use shift

class SoundPlayer:
    """Handles the interaction with pygame"""
    def __init__(self):
        pygame.mixer.init()
        self.sounds = []
        for i in range(NUMBER_OF_SOUNDS):
            self.sounds.append(pygame.mixer.Sound(SoundPlayer.path_for_sound(i+1))) # TODO error checking
    
    def play(self, number):
        """Plays the given sound with the given number. Called with 0 it will play 1.wav. Called with 1 it will play 2.wav..."""
        print("playing %d" % (number+1,))
        self.sounds[number].play()
        # pygame.mixer.music.load("samples/01.mp3")
        # pygame.mixer.music.play()

    @classmethod
    def path_for_sound(cls, number):
        base_path = os.path.dirname(os.path.realpath(__file__))
        sample_rel_path = "samples"
        return os.path.join(base_path, sample_rel_path, "%02d.wav" % (number,))

player = SoundPlayer()

import subprocess
class ShellStuff:
    def __init__(self):
        self.volume = 70 # in percent
        self.set_volume()
        
    def louder(self):
        print("louder...")
        self.volume = min(100, self.volume + 5)
        self.set_volume()
    
    def quieter(self):
        print("quieter...")
        self.volume = max(0, self.volume - 5)
        self.set_volume()
        
    def shutdown(self):
        subprocess.call(["shutdown", "-h", "0"])
        
    def set_volume(self):
        subprocess.call(["amixer", "set", "PCM", "--", "%d%%" % (self.volume,)])

shell = ShellStuff()

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO. Probably because script was run without 'sudo'")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SOUND_PINS + [SHIFT_PIN, CTRL_PIN], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def sound_callback(pin):
    print(pin)
    no = SOUND_PINS.index(pin)
    # TODO check if SHIFT or CTRL is down
    if GPIO.input(CTRL_PIN) == 0:
        if no == 0: # should be done with a dict
            shell.louder()
        elif no == 1:
            shell.quieter()
        elif no == 3:
            shell.shutdown()
        return
    if GPIO.input(SHIFT_PIN) == 0:
        no += len(SOUND_PINS)
    player.play(no)

for pin in SOUND_PINS:
    GPIO.add_event_detect(pin, GPIO.RISING, callback=sound_callback, bouncetime=400)

print('waiting...')
import time
# time.sleep(30)
while True:
    time.sleep(0.2)
print('exiting...')

GPIO.cleanup()
