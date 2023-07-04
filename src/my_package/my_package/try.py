# #!/usr/bin/env python3
# import rclpy
# import math
# from std_msgs.msg import String
# from rclpy.node import Node
# from geometry_msgs.msg import Twist, Pose2D
# from nav_msgs.msg import Odometry
# import numpy as np
# from ros2_aruco_interfaces.msg import ArucoMarkers

# #  Class for handle My Node
# class Aruco(Node):

#     def __init__(self):
#         super().__init__('aruco')
        
#         super().__init__('color_listener')
#         self.cleft = self.create_subscription(
#             String, "/rp2/left/color", self.color_left_callback, 100
#         )
#         self.cright = self.create_subscription(
#             String, "/rp2/right/color", self.color_right_callback, 100
#         )
        
        
        
#         self.robot_id = 10
#         self.target_id = 1
        
#         self.limit = 0.2 # max linear velocity 
#         # self.epsilon = 0.3 # distance to stop robot

#         self.previous_target = (0,0) # initial value; not great
        
#         self.cmd_publisher = self.create_publisher(Twist, '/rp2/cmd', 10)
        
#         # Setup aruco subscription
#         self.aruco_subscription = self.create_subscription(
#             ArucoMarkers,
#             '/robot_location',
#             self.aruco_callback,
#             10
#         )
        
#         self.current_odometry: Odometry = None
#         self.r_color = None
#         self.l_color = None
        

#     def color_right_callback(self, msg):
#         self.r_color = msg.data

#     def color_left_callback(self, msg):
#         self.l_color = msg.data

#         # <Setup ultrasonic sensor>
#         # <Setup color sensors>
#         # <Setup gyroscope>
        
      
#     # Convert quaternions to euler angles for Z plane only
#     def quaternion_to_yaw(self, orientation):
#         q = orientation

#         siny_cosp = 2 * (q.w * q.z + q.x * q.y)
#         cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)

#         return math.atan2(siny_cosp, cosy_cosp)
    
#     def get_marker_index(self, msg, marker_id):
#         try:
#             marker_index = msg.marker_ids.index(marker_id)
#         except:
#             return -1
#         return marker_index
    
#     # Distance from robot to target
#     def calc_distance(self, dx, dy):
#         return np.hypot(dx, dy)

#     # Rotation needed for robot to face the target
#     def calc_angle(self, dx, dy, theta):
#         angle = math.atan2(dy, dx) - theta
#         if angle > math.pi:
#             angle = angle - 2 * math.pi
#         elif angle < -math.pi:
#             angle = angle + 2 * math.pi
#         return angle

#     def left_color_callback(self, msg):
#         print("lcr")
#         self.lcr = msg.data

#     def right_color_callback(self, msg):
#         print("rcr")
#         self.rcr = msg.data
        
#     def collision_check(self, lv, av):
#         if self.lcr == "red" or self.rcr == "red":
#             print("found red")
#             lv = -lv # reverse ...
#             av = -av * 2 # ... with twice turning force
#         return (lv, av)

#     def collision_check2(self, lv, av):
#         if self.lcr == "red" and self.rcr != "red":
#             lv = 0.1
#             av = -av
#         elif self.lcr != "red" and self.rcr == "red":
#             lv = 0.1
#             av = -av
#         return (lv, av)
        
#     def aruco_callback(self, msg):
#         # Get marker indexes
#         robot_marker_index = self.get_marker_index(msg, self.robot_id)
#         target_marker_index = self.get_marker_index(msg, self.target_id)

#         if robot_marker_index == -1: # skip if robot not found
#             return
#         else: # store robot and target position
#             current = (msg.poses[robot_marker_index].position.x, msg.poses[robot_marker_index].position.y) 
#             if target_marker_index == -1:
#                 target = self.previous_target
#             else:
#                 target = (msg.poses[target_marker_index].position.x, msg.poses[target_marker_index].position.y)
#                 # target = (0, 0)

#         # Find angle relative to original pose
#         theta = self.quaternion_to_yaw(msg.poses[robot_marker_index].orientation)

#         # Calculate difference between x's and y's
#         dx = target[0] - current[0]
#         dy = target[1] - current[1]

#         # Calculate distance to target
#         distance = self.calc_distance(dx, dy)

#         # Set linear velocity
#         cmd_data = Twist()
#         cmd_data.linear.x = distance
#         cmd_data.linear.x = cmd_data.linear.x if cmd_data.linear.x < self.limit else self.limit

#         # Set angular velocity
#         angle = self.calc_angle(dx, dy, theta)
#         k =  0.3 * distance
#         cmd_data.angular.z = angle * k
        
#         # # Once in range, terminate robot movement
#         # if cmd_data.linear.x < self.epsilon:
#         #     cmd_data.linear.x = 0.0
#         #     cmd_data.angular.z = 0.0

#         self.collision_check(cmd_data.linear.x, cmd_data.angular.z)

#         # For correcting drift
#         self.previous_target = target

#         self.cmd_publisher.publish(cmd_data)

# # Main function
# def main(args = None):
#     rclpy.init(args = args)

#     aruco = Aruco()

#     try:
#         rclpy.spin(aruco)
#     except KeyboardInterrupt:
#         pass
        
#     # Destroy the node (explicitly)
#     aruco.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
