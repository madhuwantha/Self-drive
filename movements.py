import numpy as np
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setwarnings(False)

LF = 21 
LB = 20
RB = 16
LR = 12

LPWM = 1
RPWM = 7


GPIO.setmode(GPIO.BCM)
GPIO.setup(LPWM,GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)

GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LR, GPIO.OUT)

GPIO.output(LF,GPIO.LOW)
GPIO.output(LB,GPIO.LOW)
GPIO.output(RB,GPIO.LOW)
GPIO.output(LR,GPIO.LOW)

p = GPIO.PWM(1, 1000) #left
p.start(0)

q = GPIO.PWM(7, 0.5)
q.start(0)



#while True:
class Movement(object):
	"""docstring for Movement"""
	def __init__(self, LPWM, RPWM):
		super(Movement, self).__init__()
		self.LPWM = LPWM
		self.RPWM = RPWM

	def turnLeft(speed):
		GPIO.output(RB, GPIO.LOW)
		GPIO.output(LF, GPIO.LOW)
		GPIO.output(LB, GPIO.HIGH)
		GPIO.output(RF, GPIO.HIGH)

		LPWM.ChangeDutyCycle(speed)
		RPWM.ChangeDutyCycle(speed)

	def turnRight(speed):
		GPIO.output(RB, GPIO.HIGH)
		GPIO.output(LF, GPIO.HIGH)
		GPIO.output(LB, GPIO.LOW)
		GPIO.output(RF, GPIO.LOW)

		LPWM.ChangeDutyCycle(speed)
		RPWM.ChangeDutyCycle(speed)

	def turnBack(speed):
		GPIO.output(RB, GPIO.LOW)
		GPIO.output(LF, GPIO.LOW)
		GPIO.output(LB, GPIO.HIGH)
		GPIO.output(RF, GPIO.HIGH)

		LPWM.ChangeDutyCycle(speed)
		RPWM.ChangeDutyCycle(speed)

	def brake():
		GPIO.output(LB, GPIO.HIGH)
		GPIO.output(RF, GPIO.HIGH)
		GPIO.output(RB, GPIO.HIGH)
		GPIO.output(LF, GPIO.HIGH)

		LPWM.ChangeDutyCycle(255)
		RPWM.ChangeDutyCycle(255)

	def stop():
		GPIO.output(LB, GPIO.LOW)
		GPIO.output(RF, GPIO.LOW)
		GPIO.output(RB, GPIO.LOW)
		GPIO.output(LF, GPIO.LOW)

    
    
        
    
