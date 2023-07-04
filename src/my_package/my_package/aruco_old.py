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

    def __init__(self):
        super().__init__('my_node')

        self.cmd_data = Twist()
        self.odom_data = Odometry()
        self.aruco_data = ArucoMarkers()
        
        self.robot_id = 10
        self.target_id = 8
        
        self.limit = 0.2
        self.epsilon = 0.3
        self.reached_destination = False
        
        self.cmd_publisher = self.create_publisher(Twist, '/rp2/cmd', 10)
        
        # Setup aruco subscription
        self.aruco_subscription = self.create_subscription(
            ArucoMarkers,
            '/robot_location',
            self.aruco_callback,
            10
        )

        # <Setup ultrasonic senso>r
        # <Setup color sensors>
        # <Setup gyroscope>
      
    # Convert quaternions to euler angles for Z plane only
    def quaternion_to_yaw(self, orientation):
        q = orientation

        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)

        return math.atan2(siny_cosp, cosy_cosp)

    # Call every 0.05 seconds
    def aruco_callback(self, msg):
        # Most recent data (position and orientation)
        cmd_msg = Twist()
        
        # Get current position x, y and orientation z of robot
        try:
            robot_marker_index = msg.marker_ids.index(self.robot_id)
        except:
            print("No robot recognized")
            return
        try:
            target_marker_index = msg.marker_ids.index(self.target_id)
        except:
            print("No target recognized")
            return
        
        current_pos = (msg.poses[robot_marker_index].position.x, msg.poses[robot_marker_index].position.y) 
        target_pos = (msg.poses[target_marker_index].position.x, msg.poses[target_marker_index].position.y)
        #target_pos = (0, 0)

        theta = self.quaternion_to_yaw(msg.poses[robot_marker_index].orientation)
            
        # 1/2 Calculate the distance
        dx = target_pos[0] - current_pos[0]
        dy = target_pos[1] - current_pos[1]
        print("theta: " + str(theta))
        distance = np.hypot(dx, dy)

        # Once in range, stop robot
        if distance < self.epsilon:
            self.reached_destination = True
        if self.reached_destination:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 0.0

        # 2/2 Calculate the angle
        angle = math.atan2(dy, dx) - theta
        if angle > math.pi:
            angle = angle - 2 * math.pi
        elif angle < -math.pi:
            angle = angle + 2 * math.pi
        print("angle:"+str(angle))

        # Set linear and angular velocities
        cmd_msg.linear.x = self.limit if distance > self.limit else distance
        cmd_msg.angular.z = angle

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
        self.cmd_publisher.publish(cmd_msg)

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

