import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String
from .chatter import Talker

class MyNode(Node):
    def __init__(self):
        super().__init__('mynode') # Initialize node with name, 'mynode'

        # Subscribe to left color
        self.left_color_subscriber = self.create_subscription(
            String, 
            '/rp2/left/color',
            self.left_color_callback, 
            100)
        self.left_color_subscriber # prevent unused variable warning

        # Subscribe to right color        
        self.right_color_subscriber = self.create_subscription(
            String, 
            '/rp2/right/color',
            self.right_color_callback, 
            100)
        self.right_color_subscriber # prevent unused variable warning
                
        # Create object to talk to motors
        self.linear_velocity = 80
        self.talker = Talker(linear_velocity=25, wheel_distance=9.5)

        self.lcr = "?"
        self.rcr = "?"
        
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.line_follower)
    
    # Save color readings from sensors
    def left_color_callback(self, msg):
        self.get_logger().info(f"Called: left_color_callback()")
        self.lcr = msg.data
    
    def right_color_callback(self, msg):
        self.get_logger().info(f"Called: right_color_callback()")
        self.rcr = msg.data
    
    # Spin constantly and control car direction
    def line_follower(self):      
        if self.lcr == self.rcr:      
            self.talker.update_velocity(self.linear_velocity, 0.0)
            self.get_logger().info(f"L == R -> GOING STRAIGHT!")
        elif self.lcr == "white" and self.rcr != "white":
            self.get_logger().info(f"L:WHITE/R:NOT -> turning left!")
            # self.talker.update_speed(self.linear_velocity*0.5, -self.linear_velocity)
            self.talker.update_velocity(self.linear_velocity*0.1, -40)
        elif self.lcr != "white" and self.rcr == "white":
            self.get_logger().info(f"L:NOT/R:WHITE -> turning right!")
            # self.talker.update_speed(-self.linear_velocity, self.linear_velocity*0.5)
            self.talker.update_velocity(self.linear_velocity*0.1, 40)

def main(args=None):
    rclpy.init(args=args) 

    mynode = MyNode()

    rclpy.spin(mynode) # start listening for sensor readings
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
