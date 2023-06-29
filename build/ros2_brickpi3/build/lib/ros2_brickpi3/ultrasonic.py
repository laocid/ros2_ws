#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import brickpi3

# Class for handle EV3 Ultrasonic sensor inputs
class UltrasonicSensor(Node):

    def __init__(self):
        super().__init__('lego_ultrasonic_sensor')

        # Declare port parameter
        self.declare_parameter('port', 1)
        
        # Init BrickPi3 instance and set up sensor port
        self.brick = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class.
        port = self.get_parameter('port').value
        if port == 1:
            self.port = self.brick.PORT_1
        if port == 2:
            self.port = self.brick.PORT_2
        elif port == 3:
            self.port = self.brick.PORT_3
        elif port == 4:
            self.port = self.brick.PORT_4
        self.get_logger().info(f"Ultrasonic sensor input port: {port}")
        self.brick.set_sensor_type(self.port, self.brick.SENSOR_TYPE.EV3_ULTRASONIC_CM)
        
        # Setup ROS publisher
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.callback)

    # Read and publish sensor value
    def callback(self):
        try:
            msg = Float32()
            msg.data = self.brick.get_sensor(self.port)
            self.publisher_.publish(msg)
        except brickpi3.SensorError as e:
            self.get_logger().error(f"Ultrasonic sensor: {e}", throttle_duration_sec = 1)
            self.brick.set_sensor_type(self.port, self.brick.SENSOR_TYPE.EV3_ULTRASONIC_CM)

    # Reset all sensor ports
    def reset(self):
        self.brick.set_sensor_type(self.port, self.brick.SENSOR_TYPE.NONE)

                                                                                                                                    
# Main function
def main(args = None):
    rclpy.init(args = args)

    ultrasonic_sensor = UltrasonicSensor()

    try:
        rclpy.spin(ultrasonic_sensor)
    except KeyboardInterrupt:
        pass
        
    # Stop the sensor and destroy the node (explicitly)
    ultrasonic_sensor.reset()
    ultrasonic_sensor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
