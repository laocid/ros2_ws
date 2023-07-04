#!/usr/bin/env python3
import rclpy
import math
from std_msgs.msg import String
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D
from nav_msgs.msg import Odometry
import numpy as np
from ros2_aruco_interfaces.msg import ArucoMarkers
from nav_msgs.msg import OccupancyGrid
from ros2_path_planning.srv import PlanTrajectory

class Maze(Node):


    def __init__(self):
        super().__init__('maze')
        
        self.debug = False

        self.robot_id = 10
        self.target_id = 1
        
        self.limit = 0.2 # max linear velocity 
        # self.epsilon = 0.3 # distance to stop robot
        
        self.cmd_publisher = self.create_publisher(Twist, '/rp2/cmd', 10)
        # self.lw_publisher = self.create_publisher(Int32, '/rp2/left/speed', 10)
        # self.rw_publisher = self.create_publisher(Int32, '/rp2/right/speed', 10)
        
        # Setup aruco subscription
        self.aruco_subscription = self.create_subscription(
            ArucoMarkers,
            '/robot_location',
            self.aruco_callback,
            10
        )

        # Setup left color subscription
        self.left_color_subscription = self.create_subscription(
            String,
            '/rp2/left/color',
            self.left_color_callback,
            10
        )

        # Setup right color subscription
        self.right_color_subscription = self.create_subscription(
            String,
            '/rp2/right/color',
            self.right_color_callback,
            10
        )
        
        # Setup occupancy grid subscription
        self.og_subscription = self.create_subscription(
            OccupancyGrid,
            '/map/occupancy/grid/large',
            self.og_callback,
            10
        )

        # <Setup ultrasonic sensor>
        # <Setup color sensors>
        # <Setup gyroscope>
        
      
    # Convert quaternions to euler angles for Z plane only
    def quaternion_to_yaw(self, orientation): 
        q = orientation

        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)

        return math.atan2(siny_cosp, cosy_cosp)
    
    def get_marker_index(self, msg, marker_id):
        try:
            marker_index = msg.marker_ids.index(marker_id)
        except:
            return -1
        return marker_index
    
    # Distance from robot to target
    def calc_distance(self, dx, dy):
        return np.hypot(dx, dy)

    # Rotation needed for robot to face the target
    def calc_angle(self, dx, dy, theta):
        angle = math.atan2(dy, dx) - theta
        if angle > math.pi:
            angle = angle - 2 * math.pi
        elif angle < -math.pi:
            angle = angle + 2 * math.pi
        return angle

    def update_velocity(self, lv, av):
        data = Twist()
        data.linear.x = lv
        data.angular.z = av
        self.cmd_publisher.publish(data)
        
    def left_color_callback(self, msg):
        if msg == "red":
            self.get_logger().info(f"Got red on left")
            self.update_velocity(0.0, -self.av)
    def right_color_callback(self, msg):
        if msg == "red":
            self.get_logger().info(f"Got red on left")
            self.update_velocity(0.0, -self.av)
            
    def og_callback(self, msg):
        self.get_logger().info(f"Got occupancy grid")

    # def right_color_callback(self, msg):
    #     if msg == "red":
    #         self.update_velocity(self.lv, self.av)
    #     print("lw", msg)
    # def right_color_callback(self, msg):
    #     print("rw", msg)
    # def left_color_callback(self, msg):
    #     if msg == "red":
    #         lw_speed = Int32()
    #         rw_speed = Int32()
    #         lw_speed = 
    #         rw_speed = -4
    #         self.lw_publisher.publish(lw_speed)
    #         self.lw_publisher.publish(rw_speed)

    # def right_color_callback(self, msg):
    #     if msg == "red":
    #         lw_speed = Int32()
    #         rw_speed = Int32()
    #         lw_speed = 0.1
    #         rw_speed = -4
    #         self.lw_publisher.publish(lw_speed)
    #         self.lw_publisher.publish(rw_speed)
        
    # def collision_check(self, lv, av):
    #     if self.lcr == "red" or self.rcr == "red":
    #         print("found red")
    #         lv = -lv # reverse ...
    #         av = -av * 2 # ... with twice turning force
    #     return (lv, av)

    # def collision_check2(self, lv, av):
    #     if self.lcr == "red" and self.rcr != "red":
    #         lv = 0.1
    #         av = -av
    #     elif self.lcr != "red" and self.rcr == "red":
    #         lv = 0.1
    #         av = -av
    #     return (lv, av)
        
    def aruco_callback(self, msg):
        # Get marker indexes
        robot_marker_index = self.get_marker_index(msg, self.robot_id)
        target_marker_index = self.get_marker_index(msg, self.target_id)
        
        # TODO: 

        if robot_marker_index == -1: # skip if robot not found
            return
        elif target_marker_index == -1:
            return
        
        current = (msg.poses[robot_marker_index].position.x, msg.poses[robot_marker_index].position.y) 
        target = (msg.poses[target_marker_index].position.x, msg.poses[target_marker_index].position.y)
        print("current:"+str(current))
        print("target:"+str(target))

        # Find angle relative to original pose
        theta = self.quaternion_to_yaw(msg.poses[robot_marker_index].orientation)

        # Calculate difference between x's and y's
        dx = target[0] - current[0]
        dy = target[1] - current[1]

        # Calculate distance to target
        distance = self.calc_distance(dx, dy)

        # Set linear velocity
        cmd_data = Twist()
        cmd_data.linear.x = distance
        cmd_data.linear.x = distance if distance < self.limit else self.limit
        print("lv:"+str(cmd_data.linear.x))

        # Set angular velocity
        k = 0.8
        angle = self.calc_angle(dx, dy, theta)
        cmd_data.angular.z = angle * k
        print("av:"+str(angle))
        
        # # Once in range, terminate robot movement
        # if cmd_data.linear.x < self.epsilon:
        #     cmd_data.linear.x = 0.0
        #     cmd_data.angular.z = 0.0

        # Give color callbacks access to velocities
        self.lv = cmd_data.linear.x
        self.av = cmd_data.angular.z
        
        if self.debug == True:
            cmd_data.linear.x = 0.0
            cmd_data.angular.z = 0.0
        self.cmd_publisher.publish(cmd_data)

# Main function
def main(args = None):
    rclpy.init(args = args)

    maze = Maze()

    try:
        rclpy.spin(maze)
    except KeyboardInterrupt:
        pass
        
    # Destroy the node (explicitly)
    maze.destroy_node()
    rclpy.try_shutdown()

if __name__ == '__main__':
    main()


