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

        self.original_Z = 0
        self.epsilon = 0.1

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
        self.update_speed(lx=0.0, ly=0.2, lz=0.0, ax=0.0, ay=0.0, az=2.0)
        
        # Setup timer callback
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.count = 0
            
    # Convert quaternions to euler angles for Z plane only
    def convert_quaternion_to_euler(self):
        w = self.odom_data.pose.pose.orientation.w
        x = self.odom_data.pose.pose.orientation.x
        y = self.odom_data.pose.pose.orientation.y
        z = self.odom_data.pose.pose.orientation.z
        ysqr = y * y
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (ysqr + z * z)
        return math.degrees(math.atan2(t3, t4))
        
    # Call every 0.05 seconds
    def timer_callback(self):
        Z = self.convert_quaternion_to_euler() # Orientation on Z plane 
        posx = self.odom_data.pose.pose.position.x # Y coordinate
        posy = self.odom_data.pose.pose.position.y # X coordinate
        
        # Correction from -180 to 180 to 0 to 360
        if Z < 0:
            Z += 360

        # Current position is on the boundary of the threshold
        if (
                posx < self.coord[self.i][0]+self.epsilon and posx > self.coord[self.i][0]-self.epsilon and 
                posy < self.coord[self.i][1]+self.epsilon and posy > self.coord[self.i][1]-self.epsilon
            ):
            self.original_Z = Z

            # The moment the robot is in range, update the target coordinate, once.
            if self.previous_Z is not self.original_Z:
                self.i += 1

        # Calculate the angle from original pose to next coordinate
        dx = self.coord[self.i][0] - posx
        dy = self.coord[self.i][1] - posy
        theta = math.atan2(dy, dx) * (180 / math.pi)

        # Go straight once it rotates past the angle
        if Z > self.original_Z + theta:
            self.update_speed(lx=0.2, ly=0.0, lz=0.0,ax=0.0,ay=0.0,az=0.0)
        # Rotate towards next point if not past the angel
        else:
            self.update_speed(lx=0.0, ly=0.0, lz=0.0,ax=0.0,ay=0.0,az=2.0)

        # Debugging
        if self.count % 5 == 0:
            self.get_logger().info(f"dx=c[{self.i}][0]-xpos :: {self.coord[self.i][0]}-{posx}")
            self.get_logger().info(f"dy=c[{self.i}][1]-ypos :: {self.coord[self.i][1]}-{posy}")
            self.get_logger().info(f"Z is {Z}; original_Z is {self.original_Z}; theta is {theta}")
        self.cmd_publisher.publish(self.cmd_data)
        
        self.previous_Z = Z
        self.count += 1

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

    coordinates = [(0.3,0), (0.3,-0.3), (0,-0.3), (0,0)]
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
