#!/usr/bin/env python

import web  # web.py
import smbus

import bitify.python.sensors.imu as imu

urls = (
    '/', 'index'
)

bus = smbus.SMBus(1)
imu_controller = imu.IMU(bus, 0x68, 0x1e, "IMU")
imu_controller.set_compass_offsets(9830, -2814, 9848)

app = web.application(urls, globals())

class index:
    def GET(self):
        (pitch, roll, yaw) = imu_controller.read_pitch_roll_yaw()
        result = "%.2f %.2f %.2f" % (pitch, roll, yaw)
        return result

if __name__ == "__main__":
    app.run()