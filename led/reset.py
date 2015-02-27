#!/usr/bin/env python

import time
import RPi.GPIO as GPIO, feedparser, time

DEBUG = 1

GPIO.setmode(GPIO.BCM)
BLUE = 18
YELLOW = 23
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.output(BLUE, False)
GPIO.output(YELLOW, False)
