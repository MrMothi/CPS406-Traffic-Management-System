from TrafficSystem import *
from Intersection import *
import time

inter = TrafficSystem.initializeIntersection()
# inter.run()

inter.createTrafficLightThreads()

time.sleep(1)
print("Changing...")
inter.changeLights("red", "yellow")
print(inter.trafficLightThreads)

# currently testing the new cycleLight function
# if it works then the next step would be to
# implement a working button for admin to auto
# change the light from green to yellow, breaking
# the sleep for both roads (use events instead of
# sleep function)

# after that, finish up accelLights function
# to accelerate the changing of lights when there
# are pedestrians waiting to cross, then change
# cycle time back to original
# testing for it is below

# time.sleep(5)
# print("Accel")
# inter.accelLights()