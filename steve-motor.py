#import RPi.GPIO as GPIO
#import time
import math

#servoPIN = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)


pwm_frequency = 50 #i.d.R zwischen 40Hz-50Hz (25ms - 20ms)
duty_cycle = 6.2 #Tastgrad = Impulsdauer/Impulsabstand
pause = 1 #seconds

rate = 0.1
DC_FW_MAX = 7
DC_FW_MIN = 5.1
DC_STOP = 5
DC_BW_MIN = 4.9
DC_BW_MAX = 3


#Value between -1 and 1
def acc(val):
	if (val > 0 and val <= 1):
		return translate(val, 0, 1, DC_FW_MIN, DC_FW_MAX)
	elif (val < 0 and val >= -1):
		return translate(math.fabs(val), 1, 0, DC_BW_MAX, DC_BW_MIN)
	elif (val == 0):
		return DC_STOP
	else:
		return "invalid value"

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

print(acc(input("Value from -1 to 1: ")))
