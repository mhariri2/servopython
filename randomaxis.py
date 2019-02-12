import numpy
import RPi.GPIO as GPIO
import time
import random
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

servo1 = 22
servo2= 18
servo3= 16
n=100
ax=3
pos = []
angle = 2.0
startangle=7.5

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
GPIO.setup(servo3,GPIO.OUT)
p1=GPIO.PWM(servo1,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)
p3=GPIO.PWM(servo3,50)
p1.start(startangle)
p2.start(startangle)
p3.start(startangle)
p1.ChangeDutyCycle(startangle)
p2.ChangeDutyCycle(startangle)
p3.ChangeDutyCycle(startangle)
       

def getrandom(maxdegree):
    return float("{0:.2f}".format(random.uniform(-1*maxdegree,maxdegree)))

def getdc(angle,maxdegree):
    return ((angle+maxdegree)/27)+2.3

def getangle(dc,maxdegree):
    return (dc-2.3)*27-maxdegree

def resetposition():
    print("going home")
    p1.ChangeDutyCycle(startangle)
    p2.ChangeDutyCycle(startangle)
    p3.ChangeDutyCycle(startangle)
    time.sleep(.5)
    print("done")
       
def positions():
       arr =[]
       for i in range(n):
          row = [getdc(getrandom(135),135),getdc(getrandom(135),135),getdc(getrandom(135),135)]
          arr += [row]
       return arr



pos=positions()
time.sleep(2)

try:
    i=0
    while i<n-1:
       p1.ChangeDutyCycle(pos[i][0])
       p2.ChangeDutyCycle(pos[i][1])
       p3.ChangeDutyCycle(pos[i][2])
       i+=1
       time.sleep(.5)
       print("Angle "+str(i)+" : "+str(getangle(pos[i][0],135))+" :: "+str(getangle(pos[i][1],135))+" :: "+str(getangle(pos[i][2],90)))
except KeyboardInterrupt:
       resetposition()
       

resetposition()
GPIO.cleanup()

