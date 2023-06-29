#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np

#  Class for handle My Node
class MyNode(Node):

    def __init__(self, coordinates):
        super().__init__('my_node')
        # For motors
        self.cmd_data = Twist()

        # From odometer
        self.odom_data = Odometry()

        # For path
        self.coord = coordinates
        
        self.limit = 0.1
        self.epsilon = 0.1
        self.original_Z = 0
        self.count = 0
        self.i = 0

        # Setup cmd publisher
        self.cmd_publisher = self.create_publisher(Twist, 'cmd', 10)

        # Setup odom subscription
        self.odom_subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10
        )

        # <Setup ultrasonic sensor>
        # <Setup color sensors>
        # <Setup gyroscope>
        
        # Define initial velocities
        self.update_speed(lx=0.1, ly=0.0, lz=0.0, ax=0.0, ay=0.0, az=0.0)
        
        # Setup timer callback
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
            
        
    # Convert quaternions to euler angles for Z plane only
    def convert_quaternion_to_euler(self):
        w = self.odom_data.pose.pose.orientation.w
        x = self.odom_data.pose.pose.orientation.x
        y = self.odom_data.pose.pose.orientation.y
        z = self.odom_data.pose.pose.orientation.z
        ysqr = y * y
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (ysqr + z * z)
        return math.atan2(t3, t4)
        
    # Call every 0.05 seconds
    def timer_callback(self):
        # Most recent data (position and orientation)
        msg = Twist()

        # Save current position
        posx = self.odom_data.pose.pose.position.x # Y coordinate
        posy = self.odom_data.pose.pose.position.y # X coordinate

        # Calculate linear velocity proportionate to distance
        if self.count % 10 == 0:
            self.get_logger().info(f"Coords: {self.coord[self.i][0]}")
            self.get_logger().info(f"Coords: {self.coord[self.i][1]}")
        dx = self.coord[self.i][0] - posx
        dy = self.coord[self.i][1] - posy
        msg.linear.x = math.sqrt(dx**2+dy**2)

        if msg.linear.x < self.epsilon:
            self.i += 1
            self.get_logger().info(f"Updating i to {self.i}")

        if msg.linear.x > self.limit:
            msg.linear.x = self.limit

        # Calculate angular velocity
        yaw = self.convert_quaternion_to_euler() # Orientation on Z plane 
        av = math.atan2(dy, dx) - yaw
        
        # Correct angular velocity
        if av > math.pi:
            av = av - 2 * math.pi
        elif av < -math.pi:
            av = av + 2 * math.pi

        msg.angular.z = av

        if self.count % 10 == 0:
            self.get_logger().info(f"linear:{msg.linear.x}; angular:{av}")
            self.get_logger().info(f"yaw:{yaw}")
            self.get_logger().info(f"(posx,posy)=({round(posx,2)},{round(posy,2)}) where (goalx,goaly)=({self.coord[self.i][0]},{self.coord[self.i][1]})")

        if self.i >= len(self.coord):
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.count += 1
        self.cmd_publisher.publish(msg)
        
    # Invoke on every odometer reading
    def odom_callback(self, msg):
        self.odom_data = msg

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

    coordinates = [(1,0), (1, 1), (0,1), (0,0)]
    my_node = MyNode(coordinates)

    try:
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        pass
        
    # Destroy the node (explicitly)
    my_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
