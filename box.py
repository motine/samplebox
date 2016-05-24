#!/usr/bin/env python3

# docs: http://devdocs.io/python~3.5/

import os
import pygame

class SoundPlayer:
    """Handles the interaction with pygame"""
    def __init__(self):
        pygame.mixer.init()
        self.sounds = pygame.mixer.Sound(SoundPlayer.path_for_sound(1))
    
    def play(self, number):
        self.sounds.play()
        # pygame.mixer.music.load("samples/01.mp3")
        # pygame.mixer.music.play()

    @classmethod
    def path_for_sound(cls, number):
        base_path = os.path.dirname(os.path.realpath(__file__))
        sample_rel_path = "samples"
        return os.path.join(base_path, sample_rel_path, "%02d.wav" % (number,))
        
# while pygame.mixer.music.get_busy() == True:
#     continue

player = SoundPlayer()
player.play(1)

# main loop
import time
time.sleep(2)