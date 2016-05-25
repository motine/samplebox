# Development notes

<!-- wifi: ssh pi@192.168.77.181 -->
<!-- lan: ssh pi@192.168.77.195 -->

## Sound

We use [pygame](https://wiki.python.org/moin/PyGame) for playing sounds. Please also see this [tutorial](http://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python).
For driving the volume we call the shell commands

Run these commands to test your audio jack:

```bash
sudo -i
raamixer # show settings/volume
amixer set PCM -- -500 # set jack volume to -500 (defaults to -2000)
mplayer samples/01.mp3
```

## GPIO

We use the [GPIO](https://pypi.python.org/pypi/RPi.GPIO) ([wiki examples](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/)) Python package.
Please also refer to this [tutorial](http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)/

Please see to the pinout [here](http://pinout.xyz/) and run `raspi-gpio get` to check the status of the pins.

## Resources

Options to make the connection to the Pinout more stable are
[1](https://www.reichelt.de/Leiterplattenverbinder-LPV-/PRBL-40D/3/index.html?&ACTION=3&LA=2&ARTICLE=14804&GROUPID=5221&artnr=PRBL+40D),
[2](https://www.reichelt.de/Buchsenleisten/BL-2X10G-SMD2-00/3/index.html?&ACTION=3&LA=2&ARTICLE=51841&GROUPID=3221&artnr=BL+2X10G+SMD2%2C00),
[3](https://www.reichelt.de/Buchsenleisten/BL-2X20G-SMD2-00/3/index.html?&ACTION=3&LA=2&ARTICLE=51842&GROUPID=3221&artnr=BL+2X20G+SMD2%2C00).
