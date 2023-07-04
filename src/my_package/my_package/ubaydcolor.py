# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Int32, String, Float32
# import time

# class Linefollower(Node):
#     def __init__(self):
#         super().__init__('linefollower')

#         # uncomment these lines if you have a color sensor on your robot
#         # self.cleft = self.create_subscription(String, '/rp3/left/color', self.color_left_callback, 100)
#         # self.cright = self.create_subscription(String, '/rp3/right/color', self.color_right_callback, 100)

#         self.ultrasonic = self.create_subscription(Float32, '/rp3/ultrasonic', self.ultrasonic_callback, 10)
#         self.publisher_speed_left = self.create_publisher(Int32, "/rp3/l_speed/speed", 10)
#         self.publisher_speed_right = self.create_publisher(Int32, "/rp3/r_speed/speed", 10)

#         timer_period = 1  # seconds
#         self.speed_timer = self.create_timer(timer_period, self.speed_callback)

#         self.l_color = None
#         self.r_color = None
#         self.distance = None

#     def ultrasonic_callback(self, msg):
#         self.distance = msg.data
#         self.process_color()

#     def speed_callback(self):
#         msg = Int32()
#         msg.data = 200
#         self.publisher_speed_left.publish(msg)
#         self.publisher_speed_right.publish(msg)

#     def process_color(self):
#         l_speed = Int32()
#         r_speed = Int32()

#         l_color = self.l_color
#         r_color = self.r_color

#         if self.distance and self.distance < 1:  # Assume stopping distance is 1 meter
#             l_speed.data = 0
#             r_speed.data = 0
#         elif l_color == "red" or r_color == "red":  # Avoid red color
#             l_speed.data = -100  # Go backward
#             r_speed.data = -100  # Go backward

#         self.publisher_speed_left.publish(l_speed)
#         self.publisher_speed_right.publish(r_speed)

#         self.get_logger().info(f"data: {l_speed.data} and {r_speed.data}")


# def main(args=None):
#     rclpy.init(args=args)
#     linefollower = Linefollower()

#     try:
#         rclpy.spin(linefollower)
#     except KeyboardInterrupt:
#         pass
#     linefollower.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
