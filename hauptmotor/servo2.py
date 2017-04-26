import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  count=10
  while count>0:
    p.ChangeDutyCycle(1)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    count-=1
  p.stop()
  GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
