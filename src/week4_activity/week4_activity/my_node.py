"""Minimal ROS 2 node for the Week 4 package exercise."""

import rclpy
from rclpy.node import Node


class Week4Node(Node):
    """A node that confirms the package executable was started."""

    def __init__(self):
        super().__init__('week4_activity_node')
        self.get_logger().info('Week 4 activity package node is running.')


def main(args=None):
    """Start the Week 4 activity node and keep it alive until interrupted."""
    rclpy.init(args=args)
    node = Week4Node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
