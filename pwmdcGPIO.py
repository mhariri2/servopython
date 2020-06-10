import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
my_pwm=GPIO.PWM(25,100)
my_pwm.start(0)
while(1):
        fast=input("How fast? (20-100)")
        my_pwm.ChangeDutyCycle(float(fast))
my_pwm.stop()
GPIO.cleanup()
