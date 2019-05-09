#!/usr/bin/env python
import glob
import os
import sys
import rospy
from  std_msgs.msg import Int32
import carla
import random
import time

try:
	sys.path.append(glob.glob('**/%d.%d-%s.egg' % (
		sys.version_info.major,
		sys.version_info.minor,
		'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
	pass

class Subscriber:
	myCar = None
	camera = None
	spectator = None

	throttle = 0.0
	steer = 0.0
	brake = 0.0
	reverse = False

	def __init__(self):
		self.spawnCar()
		self.listener()

	def spawnCar(self):
		client = carla.Client('127.0.0.1',2000)
		client.set_timeout(2.0)
		world = client.get_world()
		self.spectator = world.get_spectator()
		blueprint_library = world.get_blueprint_library()
		car = blueprint_library.find('vehicle.audi.a2')
		spawn_points = list(world.get_map().get_spawn_points())
		self.myCar = world.try_spawn_actor(car,spawn_points[0])
		camera_bp = blueprint_library.find('sensor.camera.rgb')
		camera_bp.set_attribute('sensor_tick','.001')
		transform = carla.Transform(carla.Location(x=-4,z=3))
		self.camera = world.spawn_actor(camera_bp, transform, attach_to=self.myCar)

	def callback(self,data):
		#This callback is called whenever subscriber gets new data from the topic	

		#Use global variables so we can remember previous car directions.
		#Use global variables camera, spectator so we can update the spectator to follow the car
		#This is done by attachiing a camera sensor to the car and setting the spectator viewport
		#in reference to the camera which moves along with the car.
		#Theres probably a better way to do that but I couldn't find the API for it
		#Another problem is that I don't know how to get multiple key presses at once.
		#I think that you can use multiple getch(). Should try that later

		#0 for nothing. 1 for forwards. 2 for left. 3 for backwards. 4 for right
		direction = data.data	

		if self.camera is not None and self.spectator is not None:
			self.spectator.set_transform(self.camera.get_transform())
	
		if direction == 1:
			if self.reverse == True and self.throttle == 0:
				self.reverse = False
				self.throttle += .1
			elif self.reverse == False:
				self.throttle += .1
			else:
				self.throttle -= .1
		elif direction == 3:
			#Backwards
			if self.reverse == False and self.throttle == 0:
				self.reverse = True
				self.throttle += .1
			elif self.reverse == True:
				self.throttle += .1
			else:
				self.throttle -= .1
		elif direction == 2:
			self.steer -= .01 #left
		elif direction == 4:
			self.steer += .01 #right
		elif direction == 0:
			self.throttle = 0
			self.steer = 0
	
		self.myCar.apply_control(carla.VehicleControl(throttle = self.throttle,
				steer = self.steer, reverse = self.reverse))
	
	

	def listener(self):
		rospy.init_node('subscriber') #name this node subscriber
		rospy.Subscriber('keyboard',Int32,self.callback) #Subscribe to the 'keyboard' topic
		rospy.spin()

if __name__ == '__main__':
	subscriberInstance = Subscriber()







