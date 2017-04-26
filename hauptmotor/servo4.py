from multiprocessing import Process
import time
import RPi.GPIO as GPIO

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 100) # GPIO 18 als PWM mit 50Hz
p.start(5) # Initialisierung
p.ChangeDutyCycle(0)

def rotate_motor(duration,sleeptime):
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

def rotate_motor_angle(angle):
   #angle = 45
   print
   duty = float(angle) / 10.0 + 2.5
   p.ChangeDutyCycle(duty)

def rotate_left():
   p.ChangeDutyCycle(0.01)
   p.ChangeDutyCycle(0)


if __name__ == '__main__':
   while 1:
      command = raw_input('type: "left" or "right" or "center"')
      if command == 'right':
         print 'starting motor if not started yet'
         #if p.is_alive() != 1:
         motor = Process(target=rotate_motor_angle, args=(45))
         motor.start()
      elif command == 'left':
         motor = Process(target=rotate_left, args=())
         motor.start()
      else:
         print 'stopping motor'
         motor.terminate()
   # p.join()

    #q = Process(target=rotate_motor, args=(55,3))
    #q.start()
    #q.join()


