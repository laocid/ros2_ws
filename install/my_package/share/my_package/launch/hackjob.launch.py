#!/usr/bin/env python3
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():

    # Launch configuration
    robot_ns = LaunchConfiguration('robot_ns')
    left_motor_port = LaunchConfiguration('left_motor_port')
    right_motor_port = LaunchConfiguration('right_motor_port')
    wheel_radius = LaunchConfiguration('wheel_radius')
    base_distance = LaunchConfiguration('base_distance')
    left_color_port_launch_arg = LaunchConfiguration('left_color')
    right_color_port_launch_arg = LaunchConfiguration('right_color')

    # Launch arguments
    robot_ns_launch_arg = DeclareLaunchArgument(
        'robot_ns',
        default_value = 'rp2'
    )
    left_motor_port_launch_arg = DeclareLaunchArgument(
        'left_motor_port',
        default_value = 'A'
    )
    right_motor_port_launch_arg = DeclareLaunchArgument(
        'right_motor_port',
        default_value = 'D'
    )
    wheel_radius_launch_arg = DeclareLaunchArgument(
        'wheel_radius',
        default_value = '0.0275'
    )
    base_distance_launch_arg = DeclareLaunchArgument(
        'base_distance',
        default_value = '0.095'
    )
    
    # Launch motors
    motors = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('ros2_brickpi3'),
                'launch',
                'motors.launch.py'
            ])
        ]),
        launch_arguments = {
            'robot_ns': LaunchConfiguration('robot_ns'),
            'left_motor_port': LaunchConfiguration('left_motor_port'),
            'right_motor_port': LaunchConfiguration('right_motor_port')
        }.items()
    )

    # Differential drive node
    drive = Node(
        package = 'ros2_brickpi3',
        namespace = robot_ns,
        executable = 'drive',
        name = 'differential_drive_controller',
        parameters=[{
            'wheel_radius': LaunchConfiguration('wheel_radius'),
            'base_distance': LaunchConfiguration('base_distance')
        }]
    )
    
    # # Aruco node
    # aruco = Node(
    #     package = 'my_package',
    #     namespace = robot_ns,
    #     executable = 'aruco',
    #     name = 'aruco',
    # )
    
    # Left color node
    left_color = Node(
        package = 'my_package',
        namespace = robot_ns,
        executable = 'color',
        name = 'left_color',
        parameters=[{
            'port': 3,
        }],
        remappings=[
            ("color", "left/color"),
        ],
    )
    
    # Right color node
    right_color = Node(
        package = 'my_package',
        namespace = robot_ns,
        executable = 'color',
        name = 'right_color',
        parameters=[{
            'port': 1,
        }],
        remappings=[
            ("color", "right/color"),
        ],
    )
    
    return LaunchDescription([
        robot_ns_launch_arg,
        left_motor_port_launch_arg,
        right_motor_port_launch_arg,
        wheel_radius_launch_arg,
        base_distance_launch_arg,
        motors,
        drive,
        # aruco,
        left_color,
        right_color
    ])
