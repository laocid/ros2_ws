import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String
from .chatter import Talker

class Line(Node):
    def __init__(self):
        super().__init__('line') # Initialize node with name, 'line'

        # Subscribe to left encoder 
        self.left_encoder_subscriber = self.create_subscription(
            String, 
            '/rp2/left/encoder',
            self.left_encoder_subscriber, 
            100)
        self.left_encoder_subscriber # prevent unused variable warning

        # Subscribe to right encoder 
        self.right_encoder_subscriber = self.create_subscription(
            String, 
            '/rp2/right/encoder',
            self.right_encoder_subscriber, 
            100)
        self.right_encoder_subscriber # prevent unused variable warning

        self.declare_parameter('linear_velocity', 0.2) # default value is 0.2ms-1
        self.lv = self.get_parameter('linear_velocity').value
        self.declare_parameter('distance', 0.5) # default value is 0.5m
        self.distance = self.get_parameter('distance').value

        self.started = False

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.run)
    
    # Save color readings from sensors
    def left_encoder_callback(self, msg):
        self.get_logger().info(f"Called: left_encoder_callback()")
        self.lcr = msg.data
    
    def right_encoder_callback(self, msg):
        self.get_logger().info(f"Called: right_encoder_callback()")
        self.rcr = msg.data
    
    # Spin constantly and control car direction
    def run(self):      
        if not self.started:
            self.initial_left_ticks = self.lt
            self.initial_right_ticks = self.rt
            self.started = True
        else:
            lt_diff = self.lt - self.initial_left_ticks
            rt_diff = self.rt - self.initial_right_ticks
            if lt_diff < self.ticks_per_meter * self.distance or rt_diff < self.ticks_per_meters * self.distance:
                go_straight()
            else
                stop()
            
            

def main(args=None):
    rclpy.init(args=args) 

    line = Line()
    rclpy.spin(line)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
