#!/usr/bin/env python
# Modified from https://github.com/fetchrobotics/fetch_gazebo/blob/49674b6c5f6ac5d6a649a8dc6a39f86e60515057/fetch_gazebo_demo/scripts/demo.py

import rospy
from fetch_gazebo_demo.democlients import *

if __name__ == "__main__":
    # Create a node
    rospy.init_node("demo2")

    # Make sure sim time is working
    while not rospy.Time.now():
        pass

    # Setup clients
    move_base = MoveBaseClient()
    torso_action = FollowTrajectoryClient("torso_controller", ["torso_lift_joint"])
    head_action = PointHeadClient()
    grasping_client = GraspingClient()

    # Move the base to be in front of the table
    # Demonstrates the use of the navigation stack

    # Raise the torso using just a controller
    rospy.loginfo("Raising torso...")
    torso_action.move_to([0.4, ])

    # Look below to find the block
    head_action.look_at(0.4, -0.2, 0.5, "base_link")

    # Get block to pick
    while not rospy.is_shutdown():
        rospy.loginfo("Picking object...")
        grasping_client.updateScene()
        cube, grasps = grasping_client.getGraspableCube()
        if cube == None:
            rospy.logwarn("Perception failed.")
            continue

    # Pick the block
    if grasping_client.pick(cube, grasps):
        break
    rospy.logwarn("Grasping failed.")

    # Tuck the arm
    grasping_client.tuck()
