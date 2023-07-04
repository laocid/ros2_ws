import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from chatter import Talker

class MyNode(Node):
    def __init__(self, linear_velocity, wheel_distance):
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
                
        # Low factor for gentler turning; high factor for sharper turning
        self.adjustment_factor = 0.5

        # Create object to talk to motors
        self.talker = Talker(linear_velocity, wheel_distance)

        # Obligatory initialization 
        self.lcr = ""
        self.rcr = ""
        
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.line_follower)

    # Save color readings from sensors
    def left_color_callback(self, msg):
        #self.get_logger().info(f"Called: left_color_callback()")
        self.lcr = msg.data
    def right_color_callback(self, msg):
        #self.get_logger().info(f"Called: right_color_callback()")
        self.rcr = msg.data
    
    # Spin constantly and control car direction
    def line_follower(self):            
        if self.lcr == "white" and self.rcr != "white":
            self.get_logger().info(f"L:WHITE/R:NOT -> turning left!")
            self.talker.update_velocity(self.talker.linear_velocity*self.adjustment_factor, -self.talker.angular_velocity)
        elif self.lcr != "white" and self.rcr == "white":
            self.get_logger().info(f"L:NOT/R:WHITE -> turning right!")
            self.talker.update_velocity(self.talker.linear_velocity*self.adjustment_factor, self.talker.angular_velocity)
        else:
            self.talker.update_velocity(self.talker.linear_velocity, 0.0)
            self.get_logger().info(f"L == R -> GOING STRAIGHT!")

def main(args=None):
    rclpy.init(args=args) 

    mynode = MyNode(80, 0.95)			# arg1/limit, arg2 dm

    rclpy.spin(mynode) # start listening for sensor readings
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()