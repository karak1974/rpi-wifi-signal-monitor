import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

# Max value is 70
def getQuality():
    quality = os.popen("sudo iwlist wlan0 scan | grep 'Quality' | head -1 | awk '{print $1}' | cut -c 9- | cut -c -2").read()
    return int(quality)

# Return a number between 1 and 4
def getLevel():
    #70/4
    q = getQuality()
    if q <= 17:
        return 1
    elif q <= 34:
        return 2
    elif q <= 51:
        return 3
    else:
        return 4

def resetLV():
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)

def level1():
    GPIO.output(18,GPIO.HIGH)

def level2():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)

def level3():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)

def level4():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)

def printLV(num):
    resetLV()
    print("[SIGNAL LEVEL {}]".format(num))
    if num == 1:
        level1()
    elif num == 2:
        level2()
    elif num == 3:
        level3()
    elif num == 4:
        level4()
