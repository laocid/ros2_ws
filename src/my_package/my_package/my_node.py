#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from nav_msgs.msg import Odometry
import numpy as np

#  Class for handle My Node
class MyNode(Node):

    def __init__(self):
        super().__init__('my_node')
        
        self.cmd_data = Twist()
        self.odom_data = Odometry()
        self.target_distance = 0.5

        # Setup cmd publisher
        self.cmd_publisher = self.create_publisher(Twist, 'cmd', 10)

        # Setup odom subscription
        self.odom_subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10
        )
        
        # Set velocities to zero
        self.reset_movement()
        
        self.update_speed(lx=0.1, ly=self.cmd_data.linear.y, lz=self.cmd_data.linear.z,ax=self.cmd_data.angular.x,ay=self.cmd_data.angular.y,az=self.cmd_data.angular.z)

        # Setup timer callback
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
                
    # Call every 0.05 seconds
    def timer_callback(self):
        if self.odom_data.pose.pose.position.x > self.target_distance:
            self.reset_movement()
        self.cmd_publisher.publish(self.cmd_data)

    # Invoke on every odometer reading
    def odom_callback(self, msg):
        self.odom_data = msg
        self.get_logger().info(f"posx: {self.odom_data.pose.pose.position.x}")
    
    def update_speed(self, lx, ly, lz, ax, ay, az):
        self.cmd_data.linear.x = lx
        self.cmd_data.linear.y = ly        
        self.cmd_data.linear.z = lz        
        self.cmd_data.angular.x = ax        
        self.cmd_data.angular.y = ay        
        self.cmd_data.angular.z = az        
    
    def reset_movement(self):
        self.update_speed(0.0,0.0,0.0,0.0,0.0,0.0)
        
# Main function
def main(args = None):
    rclpy.init(args = args)

    my_node = MyNode()

    try:
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        pass
        
    # Destroy the node (explicitly)
    my_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
