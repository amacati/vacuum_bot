cmake_minimum_required(VERSION 2.8.3)
project(vacuum_bot)

find_package(catkin REQUIRED COMPONENTS
	urdf
	xacro
	robot_state_publisher
	joint_state_publisher
	rviz
	tf
	gazebo_ros
	controller_manager
	moveit_ros_move_group
	rospy
	moveit_commander
	moveit_ros_planning_interface
	)

find_package(gazebo REQUIRED)

link_directories(${GATEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

catkin_python_setup()

catkin_package()
