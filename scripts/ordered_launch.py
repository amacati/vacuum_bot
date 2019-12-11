#! /usr/bin/env python
# coding: utf-8

## @file
# Contains a main function for the ordered launch of ROS Nodes in the contol.launch file depending on a running Gazebo simulation.

## @author Martin Schuck
# martin.schuck@tum.de

import roslaunch
import rospy
import time
import rospkg

## Cleanly starts the control launch file after gazebo comes up. Staging necessary because of long loading times and MoveIt! timeouts.
# @return Returns True in case of success and False in case of failure. Type bool.
def main():

    rospy.init_node('vacuum_bot_staged_launcher', anonymous=True)

    rospack = rospkg.RosPack()
    time.sleep(5) # Avoid catching emptyWorld as it comes up.
    service = '/gazebo/get_physics_properties'
    rospy.loginfo('waitForService /gazebo/get_physics_properties ...')
    try:
        rospy.wait_for_service(service, timeout=80)  # Might also be unavailable because of a paused simulation!
    except rospy.ROSException:
        rospy.logerr('Could not contact gazebo. Shutting down.')
        rospy.signal_shutdown('timeout')
        time.sleep(0.5)
        return False
    except rospy.ServiceException:
        rospy.logerr('Could not contact gazebo. Shutting down.')
        rospy.signal_shutdown('timeout')
        time.sleep(0.5)
        return False

    rospy.sleep(1)
    rospy.loginfo('/gazebo/get_physics_properties ready, starting..')
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [rospack.get_path('vacuum_bot')+'/launch/control.launch'])
    launch.start()
    rospy.loginfo("started")    

    while not rospy.is_shutdown():
        rospy.spin()

    launch.shutdown()
    return True

if __name__ == '__main__':
    main()