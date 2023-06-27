import sys
import time
import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self, wheel_distance: float, linear_velocity: float):
        super().__init__("mynode_talker")
        self.wheel_distance = wheel_distance # Distance between wheel centers in mm
        self.linear_velocity = linear_velocity
        self.angular_velocity = linear_velocity * (wheel_distance / 2) # Use w=vr

        self.lw_publisher = self.create_publisher(Int32, "/rp2/left/speed", 10)
        self.rw_publisher = self.create_publisher(Int32, "/rp2/right/speed", 10)

        self.i = 0
    
    def update_speed(self, lw_speed, rw_speed):
        # Differential drive kinematics
        self.lw_speed = lw_speed
        self.rw_speed = rw_speed
        
        lw_msg = Int32()
        rw_msg = Int32()

        lw_msg.data = int(self.lw_speed)
        rw_msg.data = int(self.rw_speed)

        self.lw_publisher.publish(lw_msg)
        self.rw_publisher.publish(rw_msg)
        
    def update_velocity(self, linear_velocity, angular_velocity):
        # Differential drive kinematics
        self.lw_speed = linear_velocity - (angular_velocity * (self.wheel_distance / 2))
        self.rw_speed = linear_velocity + (angular_velocity * (self.wheel_distance / 2))
        
        lw_msg = Int32()
        rw_msg = Int32()

        lw_msg.data = int(self.lw_speed)
        rw_msg.data = int(self.rw_speed)

        self.lw_publisher.publish(lw_msg)
        self.rw_publisher.publish(rw_msg)
        
        # self.get_logger().info(f"{self.i}: {lw_msg.data}/{rw_msg.data} ")
        # self.get_logger().info(f"\tLeft wheel: {lw_msg.data}")
        # self.get_logger().info(f"\tRight wheel: {rw_msg.data}")
        
        self.i += 1
    
    def stop_movement(self):
        self.update_velocity(0,0)
        
    def go_straight(self):
        # D = s*t
        self.update_velocity(self.linear_velocity, 0.0)

    def turn_left(self):
        self.update_velocity(self.linear_velocity, -self.angular_velocity)
        
    def turn_right(self):
        self.update_velocity(self.linear_velocity, self.angular_velocity)
        
    def turn_deg(self, degrees, direction):
        radians = math.radians(degrees)
        
        # Calculate time taken until turn completion
        coeff = 2.5
        time_required = abs(float(radians / self.angular_velocity)) * coeff

        self.update_velocity(0.0, self.angular_velocity) 
        self.stop_movement()
    
    def turn_left_deg(self, degrees):
        self.turn(degrees, -1)
        
    def turn_right_deg(self, degrees):
        self.turn(degrees, 1)
        
    def draw_square(self, length):
        time_required = float(length)/self.linear_velocity
        self.go_straight(length)
        for i in range(3):
            time.sleep(time_required)
            self.turn_left(90)
            self.go_straight(length)
        time.sleep(time_required)
        self.stop_movement()
    
    def draw_circle(self, radius, direction):
        angular_velocity = self.linear_velocity / radius # w=vr
        time_required = float(2 * math.pi * radius) / self.linear_velocity

        if direction > 0:
            self.update_velocity(self.linear_velocity, angular_velocity)
        elif direction < 0:
            self.update_velocity(-self.linear_velocity, -angular_velocity)
            
        time.sleep(time_required)
        self.stop_movement()
    
    def draw_infinity(self, radius, linear_velocity):
        self.draw_circle(radius, linear_velocity)
        self.draw_circle(radius, -linear_velocity)
        self.stop_movement()
    
def main():
    rclpy.init()

    print("Don't forget to measure the wheel distance.")

    publisher = Talker(linear_velocity=100, wheel_distance=9.5)

    # publisher.go_straight()
    # time.sleep(2)
    # publisher.turn_left()
    # publisher.update_speed(30, 2)
    # time.sleep(5)
    
    publisher.stop_movement()
    publisher.stop_movement()
    publisher.stop_movement()
    publisher.stop_movement()

    # publisher.turn(360, 50)
    # publisher.draw_square(length=7.5, linear_velocity=50, angular_velocity=20)
    # publisher.draw_circle(0.5, 0.3)
    # publisher.draw_infinity(0.5, 0.3)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

