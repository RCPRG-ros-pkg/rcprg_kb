cmake_minimum_required(VERSION 3.5)
project(rcprg_kb)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(action_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
# Add any other required dependencies here

# Uncomment if the package has messages, services or actions
# generate_messages(DEPENDENCIES std_msgs geometry_msgs action_msgs)

# Include CMake module for Python
ament_python_install_package(${PROJECT_NAME})

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
  PATTERN ".svn" EXCLUDE)

# Uncomment if the package has executable Python nodes
# install(PROGRAMS
#   nodes/rosplan_sys_control
#   DESTINATION lib/${PROJECT_NAME}
# )

ament_package()