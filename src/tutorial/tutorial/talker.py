import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__("talker")
        self.publisher = self.create_publisher(String, "rp2", 10)
        timer_period = 0.0001
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Bong: {self.i}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    publisher = Talker()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
