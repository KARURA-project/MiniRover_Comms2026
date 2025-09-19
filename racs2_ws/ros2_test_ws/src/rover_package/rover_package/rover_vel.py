#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class vel_subscriber(Node):
    def __init__(self):
        super().__init__('rover_vel_subscriber')
        self.subscription_ = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.get_logger().info("rover_vel_subscriber node has been started.")

    def listener_callback(self, msg):
        self.get_logger().info(f'Received velocity command: linear={msg.linear.x}, angular={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    rover_vel_subscriber = vel_subscriber()
    rclpy.spin(rover_vel_subscriber)
    rover_vel_subscriber.destroy_node()
    rclpy.shutdown()