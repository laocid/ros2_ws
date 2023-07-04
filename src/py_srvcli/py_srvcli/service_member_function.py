# Importing the necessary modules
import rclpy
from rclpy.node import Node
from nav_msgs.srv import GetMap
from nav_msgs.msg import OccupancyGrid
import numpy as np

class MapProviderService(Node):
    def __init__(self):
        super().__init__('map_provider_service')
        # Creating a service that provides map data to 'get_map' service requests
        self.srv = self.create_service(GetMap, 'get_map', self.get_map_callback)

        # Assuming we create a 3m x 3m grid with 0.1m resolution, which gives a 15x15 grid.
        # Here, we're just initializing an empty grid.
        # In a real application, this would be replaced by the actual occupancy grid data.
        self.grid = np.zeros((30, 30), dtype=np.int8)

    def get_map_callback(self, request, response):
        # When a request to 'get_map' service comes, we provide the occupancy grid.

        # Here, we create a OccupancyGrid message to send as a response
        response.map = OccupancyGrid()

        # We fill the data of the OccupancyGrid with our grid data.
        # Here, 'ravel' is used to flatten the 2D grid into 1D, because OccupancyGrid.data is a 1D array.
        response.map.data = self.grid.ravel().tolist()

        # In a real application, additional map metadata (like the resolution, width, height, etc.) should be filled here.
        # TODO: Fill the rest of the map metadata

        # We return the response.
        return response

def main():
    # Initialize the ROS client library for Python
    rclpy.init()

    # Create our service node
    map_provider_service = MapProviderService()

    # Spin the node so it can process callbacks
    rclpy.spin(map_provider_service)

    # Cleanup and shutdown
    rclpy.shutdown()

if __name__ == '__main__':
    main()
