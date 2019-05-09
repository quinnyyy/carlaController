# carlaController
ROS keyboard controller for CARLA simulator

# Todo list
Write instructions for setup.
Add ability to hold multiple keys in curses.

## Instructions for setup
1. Make sure you have CARLA installed
2. Navigate to catkin_ws directory and `source devel/setup.bash`
3. I wrote down that I did this but I don't exactly remember what it does or if it's necessary:  
`echo "source ~/path_to_carlaController/carlaController/catkin_ws/devel/setup.bash >> ~/.bashrc`  
  
Not really sure if these are all the setup instructions because I'm not familiar with using catkin_ws and I forgot exactly what I did but should be able to find solutions for problems on stackoverflow or GitHub issues pretty easily. Sorry about that.
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
