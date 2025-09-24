#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from phidgets_msgs.msg import MotorVelocities
import time

# initialize ROS2
rclypy.init()
node = Node('motor_control')
pub = node.create_publisher(MotorVelocities, '/motors/set_velocity', 10)

# wait for connection
time.sleep(1)

# turn motor ON (forward at speed 100)
msg = MotorVelocities()
msg.motors = [0] # motor 0
msg.velocities = [100.0] # speed 100
pub.publish(msg)
print("Motor ON")

# wait 3 seconds
time.sleep(3)

# turn motor OFF
msg.velocities = [0.0]
pub.publish(msg)
print("Motor OFF")

# cleanup
rclpy.shutdown()
