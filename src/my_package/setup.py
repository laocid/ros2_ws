import os
from glob import glob
from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='laocid@proton.me',
    description='My custom robot code',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_node = my_package.my_node:main",
            "planner_client = my_package.planner_client:main",
            "aruco = my_package.aruco:main",
            "maze = my_package.maze:main",
            "color = my_package.color:main",
            "drive = my_package.drive:main",
            "gyro = my_package.gyro:main",
            "motor = my_package.motor:main",
            "touch = my_package.touch:main",
            "ultrasonic = my_package.ultrasonic:main",
        ],
    },
)
