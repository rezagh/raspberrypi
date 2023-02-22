# basic working of a magnetic contact sensor
# set one end to a ground an another end to a GPIO pin

import RPi.GPIO as GPIO
import time
import sys
import signal

GPIO.setmode(GPIO.BCM)
DOOR_SENSOR_PIN=26
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    isOpen = GPIO.input(DOOR_SENSOR_PIN)

    if (isOpen):
        print "open"
    else:
        print "not open"
    time.sleep(1)


IO.cleanup()

