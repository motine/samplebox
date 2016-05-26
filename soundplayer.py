import os
import pygame

class SoundPlayer:
    """Handles the interaction with pygame for playing sounds."""
    
    def __init__(self, number_of_sounds):
        """Initialize the pygame and load all sounds."""
        pygame.mixer.init()
        self.sounds = []
        for i in range(number_of_sounds):
            self.sounds.append(pygame.mixer.Sound(SoundPlayer.path_for_sound(i+1))) # TODO error checking
    
    def play(self, number):
        """Plays the given sound with the given number. Called with 0 it will play 1.wav. Called with 1 it will play 2.wav..."""
        print("playing %d" % (number+1,))
        self.sounds[number].play()
        
    def stop_all(self):
        for sound in self.sounds:
            sound.stop()

    @classmethod
    def path_for_sound(cls, number):
        """Returns the full path for the sound corresponding to the given int."""
        base_path = os.path.dirname(os.path.realpath(__file__))
        sample_rel_path = "samples"
        return os.path.join(base_path, sample_rel_path, "%02d.wav" % (number,))
