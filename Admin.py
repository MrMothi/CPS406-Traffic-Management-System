from TrafficSystem import *
from Intersection import *

class Admin: 
    
    #function to change the intersections total vehicle count
    def changeVechicleCount(newCount, inter):
        inter.totalVehicleCount = newCount

    def changeTrafficLightTiming(newTime, inter):
        inter.trafficlightTiming = newTime



