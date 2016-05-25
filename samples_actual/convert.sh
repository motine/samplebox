#!/bin/bash
# convert from mp3 to wav
# call with filename of the mp3 without the extension (.mp3)
# ./convert 01
ffmpeg -i $1.mp3 -ar 44100 -ac 2 $1.wav
