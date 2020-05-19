import numpy
import RPi.GPIO as GPIO
import time

servo = 5
servo2= 26
servo3= 13

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

p=GPIO.PWM(servo,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)
p3=GPIO.PWM(servo3,50)
p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )
p2.start(2.5)
p3.start(2.5)
angle = 2.0

matrix = [[0]*3 for i in range(6)]
matrix

#angle= float(input("angle(5=0 --> 10=180: "))
try:
    while True:
       if angle > 12.0:
          angle =2.0
          time.sleep(1.5)
       else:
          angle= angle+2
       p.ChangeDutyCycle(angle)
       p2.ChangeDutyCycle(angle)
       p3.ChangeDutyCycle(angle)
       time.sleep(.5)
       print("Angle: "+str(angle))
except KeyboardInterrupt:
    GPIO.cleanup()
