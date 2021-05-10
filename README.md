# path-planner-Fetch-navigation
Developed a global path-planner plugin for ROS. Integrating that into Fetch Navigation. Path-planner algorithm tested with relaxed A*, A* and then eventually IIG (sampling based motion planning algorithm based on RRT*).


INSTRUCTIONS ON HOW TO RUN FETCH NAVIGATION WITH A* IN GAZEBO, AND MORE


1. DO FETCH NAVIGATION

-Run the following in terminal 1,

cd catkin_ws
catkin_make
source devel/setup.bash
roslaunch fetch_gazebo playground.launch

-In a separate terminal 2, run

roslaunch fetch_gazebo_demo fetch_nav.launch

-In a separate terminal 3, run

cd src/fetch_ros/fetch_navigation && rviz -d config/navigation.rviz


2. DO FETCH NAVIGATION WITH A* PLANNER PLUGIN

!Note: This does not work at this time. It will be fixed soon. But in general, instructions would be as follows

-Run the following in terminal 1,

cd catkin_ws
catkin_make
source devel/setup.bash

- Go to catkin_ws>src>fetch_ros>fetch_navigation>launch>include>"move_base.launch.xml"
- Uncomment line 13 (<param name="base_global_planner" value="Astar_planner/AstarPlannerROS"/>) and save file
- Now, run the following in terminal 1,

cd ws_moveit
catkin_make
source devel/setup.bash
roslaunch fetch_gazebo playground.launch

-In a separate terminal 2, run

roslaunch fetch_gazebo_demo fetch_nav.launch

-In a separate terminal 3, run

cd src/fetch_ros/fetch_navigation && rviz -d config/navigation.rviz
