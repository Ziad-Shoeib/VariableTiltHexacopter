from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'geometric_controllers'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools', 'rclpy', 'actuator_msgs', 'numpy', 'scipy'],
    zip_safe=True,
    maintainer='Farooq Olanrewaju',
    maintainer_email='olanrewajufarooq@yahoo.com',
    description='Geometric Control of Variable Tilt Hexacopter',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hover_control_node = geometric_controllers.hover_control_node:main',
            'path_following_node = geometric_controllers.path_following_node:main',
            'adaptive_path_following_node = geometric_controllers.adaptive_path_following_node:main',
        ],
    },
)
