#!/bin/bash

# Navigate to the source directory of the ROS 2 workspace
cd /home/ubuntu/ros2_ws/src || exit 1

# Remove the existing package directory and clone the latest from the repository
rm -rf ros2_for_waveshare_alphabot2 && git clone https://github.com/cl-ire/ros2_for_waveshare_alphabot2.git || exit 1

# Navigate to the install directory
cd /home/ubuntu/ros2_ws/install || exit 1

# Remove the existing package installation
rm -rf ros2_for_waveshare_alphabot2 || exit 1

# Navigate to the build directory
cd /home/ubuntu/ros2_ws/build || exit 1

# Remove the existing build
rm -rf ros2_for_waveshare_alphabot2 || exit 1

# Navigate back to the ROS 2 workspace
cd /home/ubuntu/ros2_ws || exit 1

# Build the ROS 2 workspace using colcon with symlink installation
colcon build --symlink-install || exit 1

# Source the setup file to make the changes take effect
source install/setup.bash || exit 1

echo "ros2_for_waveshare_alphabot2 cleaned and rebuilt successfully."
