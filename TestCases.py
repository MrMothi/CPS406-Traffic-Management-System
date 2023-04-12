#PHASE 5 TestCase Class
#Consists of both 11 unittests (2 of them are in the same function) and 4 functional tests
import unittest
import time
from Intersection import *
from Pedestrian import *
from Vehicle import *
from Admin import *

class TestCases(unittest.TestCase):
    """
    USECASE TESTS
    """
    #USECASE 1 UNITTEST: Testing if pedestrian crosses on red
    def test_Pedestrian_Red(self):
        #initialising intersection obj, where pedestrian lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=1, totalVehicleCount=0)
        #adding single pedestrian to intersection
        inter.sidewalksObj[1].sidewalk2.append(Pedestrian(2, inter, 1, interimage.png.sidewalksObj[1], 2, 12))
        #prompting the pedestrian to cross if clear
        inter.sidewalksObj[1].sidewalk2[0].tryCrossRoad()
        #checking if the pedestrian crossed, expected to no cross
        self.assertEqual(inter.passedPedestrians,[])


    #USECASE2 UNITTEST: Testing if pedestrian crosses on green
    def test_Pedestrian_Green(self):
        #initialising intersection obj, where pedestrian lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=1, totalVehicleCount=0)
        #adding single pedestrian to intersection
        inter.sidewalksObj[0].sidewalk2.append(Pedestrian(2, inter, 0, inter.sidewalksObj[0], 2, 8))
        inter.pedLightObj[0].signalColour = "green"
        #prompting the pedestrian to cross if clear
        inter.sidewalksObj[0].sidewalk2[0].tryCrossRoad()
        #checking if the pedestrian crossed, expected to no cross
        self.assertEqual(len(inter.passedPedestrians), 1)


    #USECASE3 UNITTEST: Vehicle going straight on green light
    def test_Vehicle_Straight_Green(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single pedestrian to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 2, 1))
        inter.trafficLightObj[0].signalColour = "green"
        inter.trafficLightObj[1].signalColour = "red"
        #prompting the pedestrian to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the pedestrian crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 1)


    #USECASE4 UNITTEST: Vehicle going straight on red light
    def test_Vehicle_Straight_Red(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single vehicle to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 2, 1))
        inter.trafficLightObj[0].signalColour = "red"
        inter.trafficLightObj[1].signalColour = "green"
        #prompting the vehicle to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the vehicle crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 0)


    #USECASE5 UNITTEST: Vehicle going right on green light
    def test_Vehicle_Right_Green(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single vehicle to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 3, 1))
        inter.trafficLightObj[0].signalColour = "green"
        inter.trafficLightObj[1].signalColour = "red"
        #prompting the vehicle to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the vehicle crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 1)


    #USECASE6 UNITTEST: Vehicle going right on red light
    def test_Vehicle_Right_Red(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single vehicle to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 3, 1))
        inter.trafficLightObj[0].signalColour = "red"
        inter.trafficLightObj[1].signalColour = "green"
        #prompting the vehicle to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the vehicle crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 0)


    #USECASE7 UNITTEST: Vehicle going left on green light
    def test_Vehicle_Left_Green(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single vehicle to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 1, 1))
        inter.trafficLightObj[0].signalColour = "green"
        inter.trafficLightObj[1].signalColour = "red"
        #prompting the vehicle to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the vehicle crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 1)


    #USECASE8 UNITTEST: Vehicle going left on red light
    def test_Vehicle_Left_Red(self):
        #initialising intersection obj, where stop lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        #adding single vehicle to intersection
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 1, 1))
        inter.trafficLightObj[0].signalColour = "red"
        inter.trafficLightObj[1].signalColour = "green"
        #prompting the vehicle to cross if clear
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        #checking if the vehicle crossed, expected to no cross
        self.assertEqual(len(inter.passedVehicles), 0)


    #USECASE 9 and 10 UNITTEST: Emergency Vehicle and Accident Testing
    def test_Emergency(self):
        #initialising intersection obj, setting lights and adding vehicle and pedestrian
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=1)
        inter.trafficLightObj[1].signalColour = "green"
        inter.pedLightObj[0].signalColour = "green"
        #spawning and prompting vehicle and pedestrian
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 1, 1))
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        inter.sidewalksObj[0].sidewalk2.append(Pedestrian(2, inter, 0, inter.sidewalksObj[0], 2, 8))
        inter.sidewalksObj[0].sidewalk2[0].tryCrossRoad()
        #calling the function for emergency
        inter.requestEmergency()
        #Taking note of passed vehicle and pedestrian amounts
        tempCar = len(inter.passedVehicles)
        tempPed = len(inter.passedPedestrians)
        #spawning and prompting new vehicles
        inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",inter, inter.roadsObj[0], 1, 1))
        inter.roadsObj[0].vehiclesInLane1[0].doAction()
        inter.sidewalksObj[0].sidewalk2.append(Pedestrian(2, inter, 0, inter.sidewalksObj[0], 2, 8))
        inter.sidewalksObj[0].sidewalk2[0].tryCrossRoad()
        time.sleep(4)
        #checking traffic lights
        self.assertEqual(inter.trafficLightObj[0].signalColour, "red")
        self.assertEqual(inter.trafficLightObj[1].signalColour, "red")
        #checking if any vehicles passed
        self.assertEqual(len(inter.passedVehicles), tempCar)


    #USECASE 12 UNITTEST: Testing admin changing intersection totalVehicleCount
    def test_Admin_totalVehicleCount(self):
        #init intersection via TrafficSystem, setting vehicle count to 0 intitally
        inter = TrafficSystem.initializeIntersection()
        Admin.changeVechicleCount(10, inter)
        self.assertEqual(inter.totalVehicleCount, 10)


    #USECASE 13 UNITTEST: Testing admin changing intersection trafficLightTiming
    def test_Admin_trafficLightTiming(self):
        #init intersection via TrafficSystem, setting vehicle count to 0 intitally
        inter = TrafficSystem.initializeIntersection()
        Admin.changeTrafficLightTiming(30, inter)
        self.assertEqual(inter.trafficlightTiming, 30)


    """
    FUNCTIONAL TESTS
    """

    #Functional 14 UNITTEST: Testing if the function adds the same amount of vehicles as the totalVehicleCount
    def test_addVehicles(self):
        #init intersection via TrafficSystem, setting vehicle count to 0 intitally
        inter = Intersection(10, 4, "", totalPedestrianCount=0, totalVehicleCount=30)
        inter.addVehicles()
        self.assertEqual(inter.vehicleCount, 30)


    #Functional 15 UNITTEST: Testing if the initalization of the intersection object has created sidewalk objects
    def test_intersectionInit(self):
        #init intersection via TrafficSystem, setting vehicle count to 0 intitally
        inter = Intersection(10, 4, "", totalPedestrianCount=30, totalVehicleCount=0)
        self.assertEqual(len(inter.sidewalksObj), 4)


    #Functional 16 UNITTEST: Testing if trycross road function works for pedestrian, checking to see if the occupancy variable has been set
    def test_Pedestrian_Occ(self):
        #initialising intersection obj, where pedestrian lights are by default red
        inter = Intersection(10, 4, "", totalPedestrianCount=1, totalVehicleCount=0)
        #setting the pedestrian light to green to allow for pedestrian to cross
        inter.pedLightObj[0].signalColour = "green"
        #adding single pedestrian to intersection
        inter.sidewalksObj[0].sidewalk2.append(Pedestrian(2, inter, 0, inter.sidewalksObj[0], 2, 8))
        #prompting the pedestrian to cross if clear, which is expected to cross
        inter.sidewalksObj[0].sidewalk2[0].tryCrossRoad()
        #checking if the pedestrian crossed, expected to no cross
        self.assertGreater(inter.occ[7], 0)



    #Functional 17 UNITTEST: Testing if the function adds the same amount of pedestrians as the totalPedestrianCount
    def test_addPedestrians(self):
        #init intersection via TrafficSystem, setting vehicle count to 0 intitally
        inter = Intersection(10, 4, "", totalPedestrianCount=30, totalVehicleCount=0)
        inter.addPedestrians()
        self.assertEqual(inter.pedestrianCount, 30)



if __name__ == '__main__':
    unittest.main()