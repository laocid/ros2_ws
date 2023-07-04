#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D
from nav_msgs.msg import Odometry
import numpy as np
from ros2_aruco_interfaces.msg import ArucoMarkers

#  Class for handle My Node
class MyNode(Node):

    def __init__(self, coordinates):
        super().__init__('my_node')

        self.cmd_data = Twist()
        self.odom_data = Odometry()
        self.aruco_data = ArucoMarkers()

        self.coord = coordinates
        self.target = self.coord[0]
        
        self.limit = 0.2
        self.epsilon = 0.1

        # Setup cmd publisher
        # self.cmd_publisher = self.create_publisher(Twist, 'cmd', 10)

        # Setup odom subscription
        # self.odom_subscription = self.create_subscription(
        #     Odometry,
        #     'odom',
        #     self.odom_callback,
        #     10
        # )
        
        # Setup aruco subscription
        self.aruco_subscription = self.create_subscription(
            ArucoMarkers,
            '/robot_location',
            self.aruco_callback,
            10
        )

        # <Setup ultrasonic sensor>
        # <Setup color sensors>
        # <Setup gyroscope>
        
        # Setup timer callback
        # timer_period = 0.01  # seconds
        # self.timer = self.create_timer(timer_period, self.timer_callback)
    # Convert quaternions to euler angles for Z plane only
    def quaternion_to_yaw(self):
        q = self.odom_data.pose.pose.orientation

        siny_cosp = 2 * (q.w * q.z + q.x + q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)

        return math.atan2(siny_cosp, cosy_cosp)
        
    def get_pose(self):
        pose = Pose2D()
        # pose.x = self.odom_data.pose.pose.position.x
        # pose.y = self.odom_data.pose.pose.position.y
        
        
        pose.theta = self.quaternion_to_yaw()
        return pose

    # Call every 0.05 seconds
    def timer_callback(self):
        # Most recent data (position and orientation)
        msg = Twist()

        # Get current position x, y and orientation z
        pose = self.get_pose()

        # 1/2 Calculate the distance
        dx = self.target[0] - pose.x
        dy = self.target[1] - pose.y
        distance = np.hypot(dx, dy)

        # Once in range, update target coordinate
        if distance < self.epsilon:
            self.coord.pop(0)

        # 2/2 Calculate the angle
        angle = math.atan2(dy, dx) - pose.theta
        if angle > math.pi:
            angle = angle - 2 * math.pi
        elif angle < -math.pi:
            angle = angle + 2 * math.pi

        # Set linear and angular velocities
        msg.linear.x = self.limit if distance > self.limit else distance
        msg.angular.z = angle

        """"
        self.get_logger().info(
            str(
                {
                    "self.target": self.target,
                    "pose":pose,
                    "dx": dx,
                    "dy": dy,
                    "msg.linear.x": msg.linear.x,
                    "msg.angular.z": msg.angular.z,
                }
            ),
            throttle_duration_sec=0.1,
        )
        """

        # Once path finished, set to zero
        if len(self.coord) == 0:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        else:
            self.target = self.coord[0]

        self.cmd_publisher.publish(msg)
        
    # Invoke on every odometer reading
    def odom_callback(self, msg):
        self.odom_data = msg
        self.get_logger().info(f"(odom callback invoked)")
        
    def aruco_callback(self, msg: ArucoMarkers):
        self.aruco_data = msg
        print(msg)

# Main function
def main(args = None):
    rclpy.init(args = args)

    coordinates = [(0.5,0), (0.5, 0.5), (0,0.5), (0,0)]
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

