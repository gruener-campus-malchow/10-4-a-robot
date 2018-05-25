#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import thread
from time import gmtime, strftime

pin = 40
interval = 3 #seconds

detected = False
counter = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print strftime('%d.%m.%Y: ', gmtime()) + 'rev counter started with an interval of ' + str(interval) + ' second(s)'
    
def loop():
    global detected
    global counter
    while True:
        if GPIO.input(pin) == GPIO.LOW:
            if not detected:
                detected = True
                counter += 1
        else:
            if detected:
                detected = False

def destroy():
    GPIO.cleanup()

def printCurrent():
    global counter
    while True:
        rPerSec = round((counter / float(interval)), 1)
        rPerMin = counter * 60 / interval
        counter = 0
        print strftime('%H:%M:%S: ', gmtime()) + str(rPerSec) + ' r/s || ' + str(rPerMin) + ' r/min'
        time.sleep(interval)
    
if __name__ == '__main__':
    setup()
    thread.start_new_thread(printCurrent, ())
    try:
        loop()
    except KeyboardInterrupt:
        destroy()