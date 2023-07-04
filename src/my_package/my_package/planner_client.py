import sys

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from ros2_path_planning.srv import PlanTrajectory

class PathPlanningClientAsync(Node):

    def __init__(self):
        super().__init__('path_planning_client_async')

        # Setup occupancy grid subscription
        self.og_subscription = self.create_subscription(
            OccupancyGrid,
            '/map/occupancy/grid',
            self.og_callback,
            10
        )

        self.cli = self.create_client(PlanTrajectory, 'plan_trajectory')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = PlanTrajectory.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

    def og_callback(self, msg):
        self.og = msg

def main():
    rclpy.init()

    path_planning_client = PathPlanningClientAsync()
    response = path_planning_client.send_request(int(sys.argv[1]), int(sys.argv[2]))

    path_planning_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
