#!/usr/bin/env python3
#standard node imports
import rclpy
from rclpy.node import Node
#keyboard input imports
import sys
import termios
import tty
#message imports
from geometry_msgs.msg import Twist


def get_key():
    """Capture a single keypress from the terminal."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

class vel_publisher(Node):
    def __init__(self, node_name="cmd_vel"):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name} node has been started.")

    def publish_velocity(self):
        pub = self.create_publisher(Twist, 'cmd_vel', 10)
        try:
            while rclpy.ok():
                key = get_key()
                twist = Twist()

                if key == 'w':
                    twist.linear.x = 1.0   # forward
                elif key == 's':
                    twist.linear.x = -1.0  # backward
                elif key == 'a':
                    twist.angular.z = 1.0  # rotate left
                elif key == 'd':
                    twist.angular.z = -1.0 # rotate right
                elif key == 'q':
                    self.get_logger().info("Exiting teleop...")
                    break
                else:
                    # stop on any other key
                    twist.linear.x = 0.0
                    twist.angular.z = 0.0

                pub.publish(twist)
                self.get_logger().info(f"Published: linear={twist.linear.x}, angular={twist.angular.z}")

        except KeyboardInterrupt:
            pass


def main(args=None):
    rclpy.init(args=args)
    node = vel_publisher()
    node.publish_velocity()
    node.destroy_node()
    rclpy.shutdown()
    node.get_logger().info("Shutting down vel_publisher node.")


if __name__ == "__main__":
    main()