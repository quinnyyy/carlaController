# carlaController
ROS keyboard controller for CARLA simulator

# Todo list
Write instructions for setup.
Add ability to hold multiple keys in curses.

## Instructions for Running
1. Make sure CARLA simulator is already running. On the lab machine I use the command: `~/CarlaUE4.sh -windowed -ResX=600 -ResY=400` but it will differ based on where your CARLA is.

2. Run roscore: `roscore`

3. Run the launch file: `roslaunch carlaController keyboardStuff.launch`
This should spawn a car in the CARLA environment and change the spectator camera to view the car.

4. In the terminal where you ran the launch file you should be able to press keys to control the car.  
w = forward  
a = left  
s = backwards  
d = right  
