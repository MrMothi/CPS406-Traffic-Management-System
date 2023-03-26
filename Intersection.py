import threading
import time                                    #put the traffic and pedestrian lights here maybe 
import random
from Road import *
from TrafficLight import *


class Intersection:

    def __init__(self, trafficlightTiming: int, pedestrianLightTiming: int, weather: str, running: bool = False,
        pedestrianCount: int = 0, vehicleCount: int = 0, incident: bool = False, crossSignalRequested: bool = False, speedsData = []):

        self.trafficlightTiming = trafficlightTiming
        self.pedestrianLightTiming = pedestrianLightTiming
        self.pedestrianCount = pedestrianCount
        self.vehicleCount = vehicleCount
        self.weather = weather
        self.running = True   #running
        self.incident = incident
        self.crossSignalRequested = crossSignalRequested
        self.speedsData = speedsData
        # self.roads = constructObjects()

        # self.roads =  roads: tuple(Road, Road)
    

        #array holding trafficlights
        self.trafficLightObj = []
        self.trafficLightObj.append(TrafficLight(True, "red"))    #TrafficLight for road1
        self.trafficLightObj.append(TrafficLight(True, "red"))    #TrafficLight for road2

        #array holding all trafficlight thread variables
        self.trafficLightThreads = []
        #array holding all pedestrianlight thread variables
        self.pedLightThreads = []
        #array holding all other running threads
        self.otherThreads = []

        #Variables for indicating occupancy of the various locations in the intersection (ie Turning left area for Rd1 IncomingLane#3)
        self.occ1 = False                                               #   occ# occupancy where  #mod4 = 
        self.occ2 = False                                               # 1 is turning left
        self.occ3 = False                                               # 2 is going straight
        self.occ4 = False                                               # 3 is turning right
        self.occ5 = False                                               # 4 is pedestrian walking
        self.occ6 = False      
        self.occ7 = False
        self.occ8 = False
        self.occ9 = False
        self.occ10 = False
        self.occ11 = False
        self.occ12 = False
        self.occ13 = False
        self.occ14 = False
        self.occ15 = False
        self.occ16 = False

    def constructObjects(self):
    #     r1 = Road(self)     #has vehicle arrays 1 and 3                            #implement this later after threads
    #     r2 = Road(self)     #has vehicle arrays 2 and 4
        return None

    #Creates threads for the two trafficlights, cycling through colours while also being opposite
    def createTrafficLightThreads(self):
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[0].cycleLight1))
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[1].cycleLight2))
        self.trafficLightThreads[0].start()
        self.trafficLightThreads[1].start()

    def createPedestrianLightThreads(self):
        pass

    #Thread function to update a variable after a given time
    def updateAfterTime(self, var, t):        #pass in reference to instance variable and time to wait until making it false again
        var = True
        time.sleep(t)
        var = False                        


    #Main loop for the intersection
    def run(self):
        
        #STARTING THREADS FOR LIGHTS
        self.createTrafficLightThreads()


        #LOOP FOR THE INTERSECTION
        while(self.running):
            self.running = False
        for i in range(50):
            print("1", end="", flush=True)
            time.sleep(.25)


        #ENDING AND CATCHING THREADS
        #ending the trafficlight cycling threads
        self.trafficLightObj[0].operational = False
        self.trafficLightObj[1].operational = False
        # trafflightR1.join()

        #Printing done when the main loop is ended
        print("Done")
        return None








    #methods from UML
    def checkTrafficSignal(self, rd: Road):
        # skeleton atm, rd will be grabbed from one of the roads of the intersection: self.road
        return rd.getStatus
    
    def checkPedestrianSignal(self, rd: Road):
        # checks for pSignal from sidewalk linked to rd
        return
    
    def requestEmergencySignal(self, rd: Road):
        return
    

#manages the creation of vehicles and pedestrians
#manages the timings of signals, events and also changes made by the admin
#sets variables used by the vehicles and pedestrians
   #these variables allow them to determine when to go into the intersection or not



   # 12-16 threads for locations on the roads at the intersection, 4 for sidewalks, 3 per enterance for cars on the intersections
   # are joined after the end of the loop
   # have a while loop for the whole system here, possibly treat this class as a object, run threads within while maybe or by methods??
   # other objects such as cars and such check the variables changed by the threads to move through the intersection or not
   # ie for emergencies, we can set x areas of the 16 to be filled for y amount of time

   #4 threads for the 4 sets of lights (1 of each per road), 2 stoplights, 2 pedestrianlights
   #these threads will source info for multiple light objects
   #can be terminated here, and run with ifstatements for the light timings, and or possibly the sleep timings to adjust the durations
 
    #all pedestrians(maybe just 1, which induces others if leaving queue) and vehicles 1st in queue run on busy wait queues, and
    #based on thier action will check the appropriate queue & stoplight timing variables both within intersection, before moving
   #MAKE NOTE OF CHANGES IN REPORT SUBMISSION
   


   #make object get out of list/dequeue, after creating thread in intersection for the time occupied



#-____________________________________________________________________________________________________________________________
#FIRST SET UP THREADS FOR THE LOCATION OCCUPIED VARS, THEN SET UP OBJECTS, LIGHTS, LIGHT THREADS, THEN CAR AI, THEN PEDESTRIAN AI
                                            #DONT FORGET PEDESTRIAN THREADS AND AI, GIVE PEDESTRIANS RIGHT OF WAY


                                            #emergency all location variables now True (indicating area is taken)
                                            #4 way stop and call new method in vehicle whihc is force action, give wait between loop 2 seconds
                                                #cycle through vehicle arrays per road in circle
                                                #force action just goes without checking



                                        #function for creating all 2 stoplight threads and function for pedeslight threads,
                                        #instance variable for threads
                                        #so that admin may control 
                                        #maybe have timings for each light (or kill thread, send set red function)
                                        

                                        #for finding appropirate occupancy variables, maybe hardcode(need to have variable to determine which vehicle
                                        # array)
                                        #otherwise find formula to find the road then work from that road#



                                        # have while conditions in threads to end them externally (like while occupied# != 0)


                                        #have a separate lights setup function here that runs to offset the light timings
                                        # green =   x - (x/2)         yellow = x/2

                                        #make the occupancy threads based on time instead, to allow for multiple cars from the same intersection to go
                                        # also maybe assume that same intersection can go concurrently after .25 seconds  (dont need to check if current lane is in intersection?)

                                        #vehicle AI is a big set of if statments
                                        #first checking road, then if light is green/yellow (maybe allow green only?/check lightTimeleft instance variable/just dont go on yellows yet)
                                        #then check which array of the road its in
                                        #then check appropirate variables of occ#

                                        #pass in object of intersection to each lower object
                                        #pass in road for cars and maybe sidewalk for pedestrian along with intersection
                                        #intersection holds the lights
                                        #add function in intersection to give timings & signal color or set them as global variables

                                        #read all these notes