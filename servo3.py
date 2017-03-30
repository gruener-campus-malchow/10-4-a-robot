from multiprocessing import Process
import time

def rotate_motor(duration,sleeptime):
   import RPi.GPIO as GPIO
   #import time

   servoPIN = 17
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(servoPIN, GPIO.OUT)

   p = GPIO.PWM(servoPIN, 500) # GPIO 18 als PWM mit 50Hz
   p.start(2.5) # Initialisierung
   try:
      
      while duration > 0:
        p.ChangeDutyCycle(1)
	print 'motor running'+str(duration)
        time.sleep(sleeptime)
        duration -= 1
      p.stop()
      GPIO.cleanup()
   except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()

if __name__ == '__main__':
   while 1:
      command = raw_input('type: "start" or "stop"')
      if command == 'start':
         print 'starting motor if not started yet'
         #if p.is_alive() != 1:
         motor = Process(target=rotate_motor, args=(55,1))
         motor.start()
      else:
         print 'stopping motor'
         motor.terminate()
   # p.join()
    
    #q = Process(target=rotate_motor, args=(55,3))
    #q.start()
    #q.join()
