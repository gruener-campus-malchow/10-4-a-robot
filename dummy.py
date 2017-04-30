#Main class
def mainEngineClass():

	#Initialisation Function
	def __init__():
	
		global DC_FW_MAX = 7.0		#Maximal Duty_Cycle-Value for moving forward
		global DC_FW_MIN = 5.1		#Minimal Duty_Cycle-Value for moving forward
		global DC_STOP   = 5.0		#Duty_Cycle-Value for stopping the motors
		global DC_BW_MIN = 4.9		#Minimal Duty_Cycle-Value for moving backwards
		global DC_BW_MIN = 3.0		#Maximal Duty_Cycle-Value for moving backwards

		return;

	#Function for importing checks and imports
	def importIt(importArray):
		import sys

		for singleImport in importArray:
			if singleImport not in sys.modules:
				import singleImport
		return;

	#Function to start the engine
	def startEngine():

		global turnedOn
		global motor

		toImportArray = ['RPi.GPIO as GPIO', 'time']
		importIt(toImportArray)
		
		servoPIN = 17
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(servoPIN, GPIO.OUT)

		pwm_frequency = 100 #Normally between 40Hz-50Hz (25ms - 20ms)
		duty_cycle = 0 #Tastgrad = Impulsdauer/Impulsabstand
		pause = 0.5 #Seconds
		rate = 0.1

		motor = GPIO.PWM(servoPIN, pwm_frequency) # GPIO 18 as PWM with 50Hz
		motor.start(duty_cycle)

		turnedOn = 1

		return;

	#Function to stop the engine
	def stopEngine():
		if turnedOn:

			global turnedOn

			motor.stop()
			GPIO.cleanup()

			turnedOn = 0

		else:
			print "WARNING: Motor is offline"

		return;

	#Function for acceleration
	#Acc is a number from -1 to 1 for accelerating
	def accelerateEngine(acc):

		if turnedOn:
		
			toImportArray = ['math']
			importIt(toImportArray)

			accelerationValue = float(acc)
			if (value > 0 and value <= 1):
				return remap(value, 0, 1, DC_FW_MIN, DC_FW_MAX)
			elif (value < 0 and value >= -1):
				return remap(math.fabs(value), 1, 0, DC_BW_MAX, DC_BW_MIN)
			elif (value == 0):
				return DC_STOP
			else:
				print "WARNING: Please enter a value between -1 and 1"
			
		else:
			print "WARNING: Motor is offline"

		return;
		
	#Function for remapping
	#Map series of numbers with other ones
	def remap(value, leftMin, leftMax, rightMin, rightMax):
		return rightMin + ((float(value - leftMin) / float(leftMax - leftMin)) * (rightMax - rightMin))

	#Function for turning
	#Accepts an angle of the tires (-90 until 90). Use negative to change to left or positive to change to right
	def changeDirEngine(angle):

		return;

	#Function for emergency stop by sonic distance
	def lookUpDistance():
		toImportArray = ['RPi.GPIO as GPIO', 'time']
		importIt(toImportArray)
		return;

	#Function for checkin g accelerations with gyro acceleration sensor
	def gyroAcceleration():
		toImportArray = ['smbus', 'math', 'time']
		importIt(toImportArray)
		return;
