from TrafficSystem import *
from Intersection import *

inter = TrafficSystem.initializeIntersection()
# inter.run()

inter.createTrafficLightThreads()
print(inter.trafficLightThreads[0].target)