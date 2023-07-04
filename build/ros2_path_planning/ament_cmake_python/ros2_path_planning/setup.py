from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2_path_planning',
    version='0.0.1',
    packages=find_packages(
        include=('ros2_path_planning', 'ros2_path_planning.*')),
)
