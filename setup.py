from setuptools import find_packages, setup

package_name = 'rover_control_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samer',
    maintainer_email='samer.mohamed600012@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "joystick_node = rover_control_system.joystick_node:main",
            "navigation_node = rover_control_system.navigation_node:main",
            "thruster_controller_node = rover_control_system.thruster_controller_node:main",
        ],
    },
)
