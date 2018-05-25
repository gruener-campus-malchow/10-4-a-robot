import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm_frequency = 40 #i.d.R zwischen 40Hz-50Hz (25ms - 20ms)
duty_cycle = 0 #Tastgrad = Impulsdauer/Impulsabstand
pause = 1 #seconds
rate = 0.25

p = GPIO.PWM(servoPIN, pwm_frequency) # GPIO 18 als PWM mit 50Hz
p.start(duty_cycle) # Initialisierung
try:
  while True:
    print 'freq=' + str(pwm_frequency) + ' dc=' + str(duty_cycle) + ' wait=' + str(pause)
    p.ChangeDutyCycle(duty_cycle)
    time.sleep(pause)
    duty_cycle = duty_cycle + rate
    
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
