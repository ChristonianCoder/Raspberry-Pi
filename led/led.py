#!/usr/bin/env python

import time
import RPi.GPIO as GPIO, feedparser, time

DEBUG = 1

GPIO.setmode(GPIO.BCM)
BLUE = 18
YELLOW = 23
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

x = True

while True:
		GPIO.output(BLUE, x)
		GPIO.output(YELLOW, x)
		time.sleep(1)
		x = False
		GPIO.output(BLUE, x)
		GPIO.output(YELLOW, x)
		time.sleep(1)
		x = True

