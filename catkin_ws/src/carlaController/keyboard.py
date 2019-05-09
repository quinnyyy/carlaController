#! /usr/bin/env python

import curses
import rospy
from std_msgs.msg import Int32

def controller():
	#Initialize ROS stuff
	pub = rospy.Publisher('keyboard', Int32, queue_size=1) #publish to the keyboard topic
	rospy.init_node('controller') #name this node controller
	rate = rospy.Rate(10)  #10hz
	
	#Initialize curses environment
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.nodelay(1)
	
	direction = 0	

	while not rospy.is_shutdown():
		c = stdscr.getch()
			
		#0 = No action. 1 = forwards. 2 = left. 3 = backwards. 4 = right. 5 for break. Press q to quit
		if c == ord('w') or c == curses.KEY_UP:
			direction = 1
		elif c == ord('a') or c == curses.KEY_LEFT:
			direction = 2
		elif c == ord('s') or c == curses.KEY_UP:
			direction = 3
		elif c == ord('d') or c == curses.KEY_DOWN:
			direction = 4
		elif c == ord(' '):
			direction = 5
		elif c == ord('q'):
			break;
		else:
			direction = 0
		
		#curses has a delay before registering a key as being held. Not sure best way to handle it
		curses.flushinp()
		pub.publish(direction)
		rate.sleep()
		

	#Close curses environment
	curses.nobreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

if __name__ == '__main__':
	try:
		controller()
	except rospy.ROSInterruptException:
		pass
