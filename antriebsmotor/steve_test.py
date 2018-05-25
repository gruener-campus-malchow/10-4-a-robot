import curses
from threading import Thread
import RPi.GPIO as GPIO
import time

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

#curses.wrapper(main)

#servoPIN = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)


pwm_frequency = 50 #i.d.R zwischen 40Hz-50Hz (25ms - 20ms)
duty_cycle = 6.2 #Tastgrad = Impulsdauer/Impulsabstand
pause = 1 #seconds
rate = 0.1

def motor():
    print 'freq= ' + str(pwm_frequency) + ' dc=' + str(duty_cycle) + $


#p = GPIO.PWM(servoPIN, pwm_frequency) # GPIO 18 als PWM mit 50Hz
#p.start(duty_cycle) # Initialisierung

if __name__ == '__main__':
    p = GPIO.PWM(servoPIN, pwm_frequency)
    p.start(duty_cycle)
    thPWM = new Thread(target = motor)

try:
    while 1:
        print 'freq=' + str(pwm_frequency) + ' dc=' + str(duty_cycle) + $
        #p.ChangeDutyCycle(duty_cycle)
        #time.sleep(pause)
        #duty_cycle = duty_cycle + rate

except KeyboardInterrupt:
    pass
#p.stop()
#GPIO.cleanup()

