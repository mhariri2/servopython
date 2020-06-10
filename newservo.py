import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
while True:
    kit.servo[15].angle = 0
    #kit.servo[9].angle = 0
    #kit.servo[10].angle = 0
    time.sleep(3)
    print('0')

    kit.servo[15].angle = 90
    #kit.servo[9].angle = 90
    #kit.servo[10].angle = 90
    print('90')
    time.sleep(2)
    fast=input("How fast? (20-100)")
    kit.servo[15].angle = float(fast)
    #kit.servo[9].angle = 180
    #kit.servo[10].angle = 180
    time.sleep(2)
    print('180')

