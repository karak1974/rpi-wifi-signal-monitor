import RPi.GPIO as GPIO
import os
from time import sleep
import signal_package as sp

lv = 1
while True:
    level = sp.getLevel()

    # Check level if it's not the same with the previous
    if level != lv:
        sp.printLV(level)
        lv = level

    sleep(1)