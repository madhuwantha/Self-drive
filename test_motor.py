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
    
    
    
        
    
