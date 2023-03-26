import threading
import time                                    
import random
from Road import *
from Sidewalk import *
from TrafficLight import *
from PedestrianLight import *


class Intersection:

    def __init__(self, trafficlightTiming: int, pedestrianLightTiming: int, weather: str, running: bool = False,
        pedestrianCount: int = 0, vehicleCount: int = 0, incident: bool = False, crossSignalRequested: bool = False, speedsData = []):


        # REGULAR INSTANCE VARIABLES----------------------------------------------------------------------------
        self.trafficlightTiming = trafficlightTiming
        # TrafficLight.signalTime = trafficlightTiming #for some reason it doesnt work down there --------------------------------------
        self.pedestrianLightTiming = pedestrianLightTiming
        self.pedestrianCount = pedestrianCount
        self.vehicleCount = vehicleCount
        self.weather = weather
        self.running = True   #running
        self.incident = incident
        self.crossSignalRequested = crossSignalRequested
        self.speedsData = speedsData
    

        # OBJECT REFERENCE LISTS--------------------------------------------------------------------------------
        #array holding TrafficLightsights
        self.trafficLightObj = []
        #array holding PedestrianLights
        self.pedLightObj = []
        #array holding Roads
        self.roadsObj = [] #roads: tuple(Road, Road)
        #array holding Sidewalks
        self.sidewalkObj = []
        
        #calling method to create all objects
        self.constructObjects()


        #THREAD VARIABLES AND OCCUPANCY VARIABLES---------------------------------------------------------------
        #array holding all trafficlight thread variables
        self.trafficLightThreads = []
        #array holding all pedestrianlight thread variables
        self.pedLightThreads = []
        #array holding all other running threads
        self.otherThreads = []

        #Variables for indicating occupancy of the various locations in the intersection (ie Turning left area for Rd1 IncomingLane#3)
        self.occ1 = 0                                               #   occ# occupancy where  #mod4 = 
        self.occ2 = 0                                               # 1 is turning left
        self.occ3 = 0                                               # 2 is going straight
        self.occ4 = 0                                               # 3 is turning right
        self.occ5 = 0                                               # 4 is pedestrian walking
        self.occ6 = 0     
        self.occ7 = 0                                               # <=0 means open, >0 means occupied for x seconds more 
        self.occ8 = 0
        self.occ9 = 0
        self.occ10 = 0
        self.occ11 = 0
        self.occ12 = 0
        self.occ13 = 0
        self.occ14 = 0
        self.occ15 = 0
        self.occ16 = 0




    #creates all the stationary objects for the intersection (Trafficlights, PedestrianLights, Roads, Sidewalks)
    def constructObjects(self):
        #Lights are only made if they run at a separate colour cycle, other objects can reference the same light if they follow the same signal
        #making trafficlights
        TrafficLight.signalTime = self.trafficlightTiming
        self.trafficLightObj.append(TrafficLight(True, "red"))    #TrafficLight for road1
        self.trafficLightObj.append(TrafficLight(True, "red"))    #TrafficLight for road2
        
        # #making pedestrianlights
        # self.pedLightObj.append(PedestrianLight())  #Pedestrian Lights for rd1 (for signalling across rd1)
        # self.pedLightObj.append(PedestrianLight())  #Pedestrian Lights for rd2 (for signalling across rd2)

        # #making sidewalks (Passing in intersection object reference)
        # self.sidewalksObj.append(SideWalk())   #Sidewalk #1  for rd1      parallel to respectively numbered vehicle array       -----------implement more after car stuff finished---------
        # self.sidewalksObj.append(SideWalk())   #Sidewalk #2  for rd2
        # self.sidewalksObj.append(SideWalk())   #Sidewalk #3  for rd1
        # self.sidewalksObj.append(SideWalk())   #Sidewalk #4  for rd2

        #making roads  (Passing in intersection object reference)
        self.roadsObj.append(Road(self, True, False, False, ['''sidewalks?'''], [], [], 1))     #has vehicle arrays 1 and 3   
        self.roadsObj.append(Road(self, True, False, False, [], [], [], 2))     #has vehicle arrays 2 and 4
        return None

    #Creates threads for the two trafficlights, cycling through colours while also being opposite
    def createTrafficLightThreads(self):
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[0].cycleLight1))
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[1].cycleLight2))
        self.trafficLightThreads[0].start()
        self.trafficLightThreads[1].start()

    def createPedestrianLightThreads(self):
        pass

    #Thread function to keep decreasing variable until its <= 0, decreasing by 1 each time, and waiting 1 second each time
    def updateAfterTime(self, var):        #pass in reference to instance variable
        while(t>0):
            t = t-1
            time.sleep(1)                     


    #Main loop for the intersection
    def run(self):
        try:#maybe keep this for error proofing

            #STARTING THREADS FOR LIGHTS
            self.createTrafficLightThreads()

            #MAIN LOOP FOR THE INTERSECTION--------------------------------------
            while(self.running):
                self.running = False
            for i in range(100):
                print("1", end="", flush=True)
                # print(self.checkTrafficSignal(self.roadsObj[1]))
                time.sleep(.25)

        except KeyboardInterrupt:
            #ENDING AND CATCHING THREADS
            #ending the trafficlight cycling threads
            self.trafficLightObj[0].operational = False
            self.trafficLightObj[1].operational = False
            #MAYBE INSTALL PACKAGE WHICH ENDS THE THREADS BY THROWING EXCEPTION IN THEM
        #else:

        #Printing done when the main loop is ended
        print("Done")
        return None








    #methods from UML

    #Given a Road object, it returns the current signal colour string for its respective trafficLights
    def checkTrafficSignal(self, rd: Road):
        return self.trafficLightObj[rd.rdNum-1].signalColour
    
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


                                        #sidewalks hold 2 arrays for the two sides of the road, once pedestrian crosses, they get deleted from system& array

                                        #read all these notes











                                        #setup roading pinging then after do the ifstatements