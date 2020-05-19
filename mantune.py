import numpy
import RPi.GPIO as GPIO
import time
 
servo = 5
servo2= 13
servo3= 26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
GPIO.setup(servo3,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%
freq=50
strt=7.3
p=GPIO.PWM(servo,freq)# 50hz frequency
p2=GPIO.PWM(servo2,freq)
p3=GPIO.PWM(servo3,freq)
p.start(strt)# starting duty cycle ( it set the servo to 0 degree )
p2.start(strt)
p3.start(strt)

#angle= float(input("angle(5=0 --> 10=180: "))
try:
    while True:
       degreetext=input("Degree: ")
       degree=float(degreetext)
       angle=((degree+135)/27)+2.3
       p.ChangeDutyCycle(angle)
       p2.ChangeDutyCycle(angle)
       p3.ChangeDutyCycle(angle)
       #degree=(angle-2.3)*27-135
       print("Angle: "+str(angle)+">>"+str(degree))
except KeyboardInterrupt:
    GPIO.cleanup()
