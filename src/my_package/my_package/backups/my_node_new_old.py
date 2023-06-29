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
        
        self.pos_epsilon = 0.01
        self.ang_epsilon = 5
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
        return math.degrees(math.atan2(t3, t4))
        
    # Call every 0.05 seconds
    def timer_callback(self):
        # Most recent data (position and orientation
        Z = self.convert_quaternion_to_euler() # Orientation on Z plane 
        posx = self.odom_data.pose.pose.position.x # Y coordinate
        posy = self.odom_data.pose.pose.position.y # X coordinate

        # For less verbose debugging
        self.count += 1

        # Calculate angle from current orientation
        dx = self.coord[self.i][0] - posx
        dy = self.coord[self.i][1] - posy
        theta = math.atan2(dy, dx) * (180 / math.pi)

        if self.count % 5 == 0:
            self.get_logger().info(f"(posx,posy)=({round(posx,2)},{round(posy,2)}) where (goalx,goaly)=({self.coord[self.i][0]},{self.coord[self.i][1]})")

        distance = math.sqrt(dx**2+dy**2)
        # Rotate if within proximity of goal coordinate and orientation is not facing the next coordinate
        if (
                posx < self.coord[self.i][0]+self.pos_epsilon and posx > self.coord[self.i][0]-self.pos_epsilon and 
                posy < self.coord[self.i][1]+self.pos_epsilon and posy > self.coord[self.i][1]-self.pos_epsilon
            ):
        #if distance < self.pos_epsilon and distance > self.pos_epsilon:
            self.original_Z = Z
        
            # As soon as robot enters proximity, set new goal coordinate
            if self.previous_Z is not self.original_Z: 
                self.get_logger().info(f"Arrived at goal coordinate; (posx,posy)=({round(posx,2)},{round(posy,2)}) where (goalx,goaly)=({self.coord[self.i][0]},{self.coord[self.i][1]})")
                self.i += 1
        
        self.get_logger().info(f"Z:{Z}; Original_Z:{self.original_Z}; Theta:{theta}")
        # Turn the robot on the spot
        if Z > self.original_Z + theta:
            self.update_speed(lx=0.05, ly=0.0, lz=0.0, ax=0.0, ay=0.0, az=0.0)
        else:
            self.update_speed(lx=0.0, ly=0.0, lz=0.0, ax=0.0, ay=0.0, az=0.5)

        # Save the last orientation value
        self.previous_Z = Z

        self.cmd_publisher.publish(self.cmd_data)
        
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

    coordinates = [(0.3,0), (0,3, 0.3), (0,0.3), (0,0)]
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
