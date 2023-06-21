import sys
import time
import rclpy
import math
from rclpy.node import Node
from enum import Enum

from std_msgs.msg import Int32

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class Talker(Node):

    def __init__(self, wheel_distance, wheel_radius):
        super().__init__("talker")
        self.wheel_distance = wheel_distance # Distance between wheel centers in mm
        self.wheel_radius = wheel_radius # Radius of wheel in mm
        self.wheel_circumference = 2 * math.pi * self.wheel_radius

        self.lw_publisher = self.create_publisher(Int32, "/rp2/left/speed", 10)
        self.rw_publisher = self.create_publisher(Int32, "/rp2/right/speed", 10)

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0

    def timer_callback(self):
        lw_msg = Int32()
        lw_msg.data = self.lw_speed
        self.lw_publisher.publish(lw_msg)
        
        rw_msg = Int32()
        rw_msg.data = self.rw_speed
        self.rw_publisher.publish(rw_msg)
        
        self.get_logger().info(f"Spin #{self.i} ")
        self.get_logger().info(f"\tLeft wheel: {lw_msg.data}")
        self.get_logger().info(f"\tRight wheel: {rw_msg.data}")

        self.i += 1

    def update_speed(self, lw_speed, rw_speed):
        self.lw_speed = lw_speed
        self.rw_speed = rw_speed
        rclpy.spin_once(self)
    
    def stop_movement(self):
        self.update_speed(0, 0)
        
    def move_straight(self, speed, distance):
        self.update_speed(speed, speed)

        # Calculate time required to travel a given distance
        delay = float(distance) / speed

        time.sleep(delay)
        self.stop_movement()
    
    def turn(self, direction, speed, angle):
        # Calculate distance for wheel to travel to finish its turn
        distance = (float(angle) / 360) * self.wheel_circumference

        # Choose which direction to turn
        if direction == Direction.LEFT:
            self.update_speed(speed, -speed)
        elif direction == Direction.RIGHT:
            self.update_speed(-speed, speed)

        # Calculate time required to turn a given angle
        delay = float(distance) / speed

        time.sleep(delay)
        self.stop_movement()
    
    def draw_square(self, speed, direction=Direction.RIGHT):
        self.move_straight(speed, 100)
        for i in range(3):
            self.turn(direction, speed, 90)
            self.move_straight(speed, 100)
    
    def draw_circle(self, speed, radius=10, direction=Direction.RIGHT, degrees=360):
        # Calculate circumference each wheel must travel
        inner_circumference = 2 * math.pi * radius 
        outer_circumference = 2 * math.pi * (radius + self.wheel_distance)

        # Use ratio between circumferences to displace the wheel speeds
        inner_speed = speed
        outer_speed	= speed * (float(outer_circumference) / inner_circumference)

        # Anticlockwise, left wheel takes long path and right takes short path
        if direction == Direction.LEFT:
            lw_speed = inner_speed
            rw_speed = outer_speed
        # Clockwise, right wheel takes long path and left takes short path
        elif direction == Direction.RIGHT:
            lw_speed = outer_speed
            rw_speed = inner_speed

        # Calculate time to draw circle
        delay = (float(outer_circumference) / outer_speed) * (float(degrees)/360)
        
        # Begin drawing it
        self.update_speed(int(lw_speed), int(rw_speed))

        time.sleep(delay)

        # Stop drawing it
        self.stop_movement()

    def draw_infinity(self, speed, radius=10):
        self.draw_circle(speed, radius, Direction.LEFT)
        self.draw_circle(speed, radius, Direction.RIGHT)
    
    def draw_robot(self, speed, height):
        # Draw R
        half_height = float(height) / 2
        self.move_straight(speed, height)
        self.turn(Direction.RIGHT, speed, 90)
        self.draw_circle(speed, float(half_height)/2, Direction.RIGHT, 180) # Draw semicircle
        self.turn(Direction.LEFT, speed, 135)
        self.move_straight(speed, sqrt(half_height*half_height + half_height*half_height))

        # Move to next letter
        self.turn(Direction.LEFT, speed, 45)
        self.move_straight(speed, half_height)

        # Draw O
        self.draw_circle(speed, half_height, Direction.LEFT)

        # Move to next letter
        self.move_straight(speed, height)

        # Draw B
        self.turn(Direction.LEFT, speed, 90)
        self.move_straight(speed, height)
        self.draw_circle(speed, float(half_height)/2, Direction.RIGHT, 180) # Draw semicircle
        self.turn(Direction.LEFT, speed, 90)
        self.draw_circle(speed, float(half_height)/2, Direction.RIGHT, 180) # Draw semicircle
        self.turn(Direction.RIGHT, speed, 180)

        # Move to next letter
        self.move_straight(speed, height + half_height)

        # Draw O
        self.draw_circle(speed, half_height, Direction.LEFT)

        # Move to next letter
        self.move_straight(speed, height)

        # Draw T
        self.turn(Direction.LEFT, speed, 90)
        self.move_straight(speed, height)
        self.turn(Direction.LEFT, speed, 90)
        self.move_straight(speed, half_height)
        self.turn(Direction.RIGHT, speed, 180)
        self.move_straight(speed, half_height)
    
    def draw_spiral(self, speed, radius):
        if radius < float(self.wheel_distance) / 2:
            radius = float(self.wheel_distance) / 2

        print("Unfinished method")
        
    
def main():
    rclpy.init()

    print("Don't forget to measure the wheel distance.")

    publisher = Talker(wheel_distance=30, wheel_radius=5)

    #publisher.draw_square(speed=30)
    #publisher.draw_circle(speed=30, radius=5)
    #publisher.draw_infinity(speed=30)
    #publisher.draw_robot(speed=30, height=100)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

