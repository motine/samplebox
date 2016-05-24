# samplebox

A little device with four buttons to play music/effect samples.

<!-- ssh pi@192.168.77.181 -->

## Installation

We tested with a Raspberry PI 2 with [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) Jessie (lite image).

```bash
sudo -i
dpkg-reconfigure locales # choose your keyboard layout and language (I prefer en_US.UTF-8)
# install dependencies
sudo apt-get install python3 python3-pygame
# install convenience packages
apt-get install vim
```

## Sound

```bash
# initial testing...
sudo -i
apt-get install mplayer # install mplayer2 for testing
amixer # show settings/volume
amixer set PCM -- -500 # set jack volume to -500 (defaults to -2000)
mplayer samples/01.mp3
```

To add/change sounds, please create files under samples. Their filename should be a number between 1 and 8 with a leading 0. The sound files must be uncompressed wav files. Example filename: `samples/02.wav`.

## Circuit

...TODO...

Options to make the connection to the Pinout more stable are
[1](https://www.reichelt.de/Leiterplattenverbinder-LPV-/PRBL-40D/3/index.html?&ACTION=3&LA=2&ARTICLE=14804&GROUPID=5221&artnr=PRBL+40D),
[2](https://www.reichelt.de/Buchsenleisten/BL-2X10G-SMD2-00/3/index.html?&ACTION=3&LA=2&ARTICLE=51841&GROUPID=3221&artnr=BL+2X10G+SMD2%2C00),
[3](https://www.reichelt.de/Buchsenleisten/BL-2X20G-SMD2-00/3/index.html?&ACTION=3&LA=2&ARTICLE=51842&GROUPID=3221&artnr=BL+2X20G+SMD2%2C00).

## Resources

- Sounds: http://www.orangefreesounds.com/category/sound-effects/funny-sounds/page/2/
- GPIO Python Package: https://pypi.python.org/pypi/RPi.GPIO ([wiki examples](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/))
- GPIO in Python Tutorial: http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
- Play audio files: http://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python