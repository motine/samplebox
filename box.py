#!/usr/bin/env python3

# docs: http://devdocs.io/python~3.5/

SOUND_PINS = [11,12,13,15] # using board numbering (see here: http://pinout.xyz/)
SHIFT_PIN = 16 # please see README.md for how shift works
CTRL_PIN = 18 # also, please see README.md
BOUNCE_TIME = 400 # ms

from soundplayer import SoundPlayer
from shellstuff import ShellStuff

player = SoundPlayer(len(SOUND_PINS) * 2) # double the number of sounds, because we allow to use shift
shell = ShellStuff()

import RPi.GPIO as GPIO

def sound_callback(pin):
    """Called by GPIO for sound buttons."""
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

def ctrl_callback(pin):
    """Called by GPIO for the control button."""
    player.stop_all()

def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SOUND_PINS + [SHIFT_PIN, CTRL_PIN], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for pin in SOUND_PINS:
        GPIO.add_event_detect(pin, GPIO.RISING, callback=sound_callback, bouncetime=BOUNCE_TIME)
    GPIO.add_event_detect(CTRL_PIN, GPIO.RISING, callback=ctrl_callback, bouncetime=BOUNCE_TIME)

def main_loop():
    # TODO catch SIGTERM/SIGINT
    print('waiting...')
    import time
    while True:
        time.sleep(0.2)
    print('exiting...')

init_gpio()
main_loop()
GPIO.cleanup()
