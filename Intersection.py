import threading
from threading import Thread
import time                                    
import random
import string
from Road import *
from Sidewalk import *
from TrafficLight import *
from PedestrianLight import *
from Vehicle import *
from Pedestrian import *

class Intersection:

    def __init__(self, trafficlightTiming: int, pedestrianLightTiming: int, weather: str, running: bool = False,
        totalPedestrianCount: int = 6, totalVehicleCount: int = 20, incident: bool = False, crossSignalRequested: bool = False, speedsData = []):

        # REGULAR INSTANCE VARIABLES----------------------------------------------------------------------------
        self.trafficlightTiming = trafficlightTiming
        self.pedestrianLightTiming = pedestrianLightTiming
        self.pedestrianCount = 0 
        self.totalPedestrianCount = totalPedestrianCount
        self.vehicleCount = 0
        self.totalVehicleCount = totalVehicleCount
        self.weather = weather
        self.running = True   #running
        self.incident = incident
        self.crossSignalRequested = crossSignalRequested
        self.speedsData = speedsData
        self.passedVehicles = [] #holds all vehicles which have passed through the intersection, allows data gathering
        self.passedPedestrians = [] #holds all the pedestrians that have passed through the intersection
        self.vehicleId = 0  #variable for the IDs of the vehicles
        self.pedId = 0 #variable for the IDs of the pedestrians
        self.notfinished = True  # Variable which the pedestrianLight and TrafficLight check (If true they continue running, if false then they end)
        self.autoVehicles = False
        self.autoPedestrians = False

        # OBJECT REFERENCE LISTS--------------------------------------------------------------------------------
        #array holding TrafficLightsights
        self.trafficLightObj = []
        #array holding PedestrianLights
        self.pedLightObj = []
        #array holding Roads
        self.roadsObj = [] #roads: tuple(Road, Road)
        #array holding Sidewalks (Acting as crosswalks)
        self.sidewalksObj = []
        
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
        self.occ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]     #Test [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]          
        #   occ# occupancy where  #mod4+1 = 
        # 1 is turning left
        # 2 is going straight
        # 3 is turning right
        # 4 is pedestrian walking
        # <=0 means open, >0 means occupied for x seconds more 


        self.countForCarAdd = 0 #variable used to iterate 15 times before creating new vehicles in the system
        self.countForPedAdd = 0 #variable used to iterate 30 times before creating new vehlices in the system
        self.temp = 0





    #creates all the stationary objects for the intersection (Trafficlights, PedestrianLights, Roads, Sidewalks)
    def constructObjects(self):
        #Lights are only made if they run at a separate colour cycle, other objects can reference the same light if they follow the same signal
        #making trafficlights
        TrafficLight.signalTime = self.trafficlightTiming
        self.trafficLightObj.append(TrafficLight(True, "red", self))    #TrafficLight for road1
        self.trafficLightObj.append(TrafficLight(True, "green", self))    #TrafficLight for road2
        
        #making pedestrianlights
        PedestrianLight.signalTime = self.pedestrianLightTiming
        self.pedLightObj.append(PedestrianLight(True, True, "red", self))  #Pedestrian Lights for rd1 (for signalling across rd1)
        self.pedLightObj.append(PedestrianLight(True, True, "red", self))  #Pedestrian Lights for rd2 (for signalling across rd2)

        # #making sidewalks (Passing in intersection object reference)
        self.sidewalksObj.append(SideWalk(self, True, [], []))   #Sidewalk #1  for rd1      parallel to respectively numbered vehicle array
        self.sidewalksObj.append(SideWalk(self, True, [], []))   #Sidewalk #2  for rd2      each sidewalk has two arrays which, represent pedestrians on either side of the road
        self.sidewalksObj.append(SideWalk(self, True, [], []))   #Sidewalk #3  for rd1
        self.sidewalksObj.append(SideWalk(self, True, [], []))   #Sidewalk #4  for rd2

        #making roads  (Passing in intersection object reference)
        self.roadsObj.append(Road(self, True, False, False, ['''sidewalks?'''], [], [], 1))     #has vehicle arrays 1 and 3   
        self.roadsObj.append(Road(self, True, False, False, [], [], [], 2))     #has vehicle arrays 2 and 4

        return None



    #Creates threads for the two trafficlights, cycling through colours while also being opposite
    def createTrafficLightThreads(self, modify1=False, modify2=False):
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[0].cycleLight, args=(modify1,)))
        self.trafficLightThreads.append(threading.Thread(target=self.trafficLightObj[1].cycleLight, args=(modify2,)))
        self.trafficLightThreads[0].start()
        self.trafficLightThreads[1].start()

    def createPedestrianLightThreads(self):
        self.pedLightThreads.append(threading.Thread(target=self.pedLightObj[0].cycleLight1))  #PedestrianLight for going across rd1
        self.pedLightThreads.append(threading.Thread(target=self.pedLightObj[1].cycleLight2))  #PedestrianLight for going across rd2
        self.pedLightThreads[0].start()
        self.pedLightThreads[1].start()

    #Thread function to keep decreasing variable until its <= 0, decreasing by 1 each time, and waiting 1 second each time
    def updateAfterTime(self, var):        #pass in reference to instance variable
        self.otherThreads.append(threading.Thread(target=self.updateVar, args=[var]))
        self.otherThreads[-1].start()

    #Thread function, called by the updateAfterTime function
    def updateVar(self, var):  
        while(self.occ[var]>0):
            self.occ[var] = self.occ[var]-1
            time.sleep(1)
        return                     

    # maybe another function to change lights seperately

    def changeLights(self, colour1, colour2):
        # this function essentially changes the lights of the intersection while in sync
        # so if one light is red and the other is green, immediately change green to yellow
        # and let the red one sit for the duration that yellow is idle, then switch red to
        # green when yellow cycles to red
        # note: trafficLights still run as threads so we can just kill them and remake them
        # to instantly change the colours, but we would need to break the delay of red
        # to shorten it so it stays only for the duration of yellow

        # kill threads
        self.trafficLightObj[0].operational = False
        self.trafficLightObj[1].operational = False
        self.trafficLightThreads = []

        self.trafficLightObj[0].setColour(colour1)
        self.trafficLightObj[1].setColour(colour2)
        self.trafficLightObj[0].operational = True
        self.trafficLightObj[1].operational = True
        if colour1 == "yellow" and colour2 == "red":
            self.createTrafficLightThreads(modify2=True)
        elif colour1 == "red" and colour2 == "yellow":
            self.createTrafficLightThreads(modify1=True)
        else:
            self.createTrafficLightThreads()


    def accelLights(self):
        # get the traffic light that is green
        # accelerate both time until green becomes yellow
        # set back time to regular (only green is accelerated, red time matches at the same time)
        # this is basically a switch function for pedestrians ex. if there are pedestrians waiting
        # or an admin button
        # ideally admin will be able to automatically switch the lights so green will automatically change
        # to yellow and follow the cycle for both sides
        
        # utilizes changeLight function after increasing the speed the lights

        if self.trafficLightObj[0].colour == "green":
            time.sleep(2)
            self.changeLights("yellow", "red")
        elif self.trafficLightObj[1].colour == "green":
            time.sleep(2)
            self.changeLights("red", "yellow")
        return





    #Main loop for the intersection
    def run(self):
        #Try Catch block for breaking out of the loop via ctrl-c, and error catching
        try:

            # #STARTING THREADS FOR LIGHTS
            # self.createTrafficLightThreads()
            # self.createPedestrianLightThreads()
            
            #Adding all the random vehicles before starting
            if(self.autoVehicles):
                self.addVehicles()
                # self.testVehicles()

            #Adding all the random pedestrians before starting
            if(self.autoPedestrians):
                self.addPedestrians()
                # self.testPedestrians()


            self.running = True
            #MAIN LOOP FOR THE INTERSECTION--------------------------------------
            while(self.running):
                # print(self.trafficLightObj[0].signalColour)
                # print(self.trafficLightObj[1].signalColour)
                #Pinging every car first in the queue for each car array in the two roads
                #Going clockwise from C1, C2, C3, C4 : where C1 and C3 are in rd1 and C2 and C4 are in rd2
                print(self.roadsObj[0].vehiclesInLane1)   
                print(self.roadsObj[1].vehiclesInLane1)
                print(self.roadsObj[0].vehiclesInLane2)
                print(self.roadsObj[1].vehiclesInLane2)
                print(self.occ)


                #Prompting pedestrians (before vehicles) to go if the way is clear and light is green
                #SIDEWALK1(TOP)
                if(len(self.sidewalksObj[0].sidewalk1) > 0):
                    self.sidewalksObj[0].sidewalk1[0].tryCrossRoad()
                
                if(len(self.sidewalksObj[0].sidewalk2) > 0):
                    self.sidewalksObj[0].sidewalk2[0].tryCrossRoad()

                #SIDEWALK2(RIGHT)
                if(len(self.sidewalksObj[1].sidewalk1) > 0):
                    self.sidewalksObj[1].sidewalk1[0].tryCrossRoad()
                
                if(len(self.sidewalksObj[1].sidewalk2) > 0):
                    self.sidewalksObj[1].sidewalk2[0].tryCrossRoad()

                #SIDEWALK3(BOTTOM)
                if(len(self.sidewalksObj[2].sidewalk1) > 0):
                    self.sidewalksObj[2].sidewalk1[0].tryCrossRoad()
                
                if(len(self.sidewalksObj[2].sidewalk2) > 0):
                    self.sidewalksObj[2].sidewalk2[0].tryCrossRoad()

                #SIDEWALK4(LEFT)
                if(len(self.sidewalksObj[3].sidewalk1) > 0):
                    self.sidewalksObj[3].sidewalk1[0].tryCrossRoad()
                
                if(len(self.sidewalksObj[3].sidewalk2) > 0):
                    self.sidewalksObj[3].sidewalk2[0].tryCrossRoad()


                #Prompting Vehicles to go through intersection
                #calling C1
                if (len(self.roadsObj[0].vehiclesInLane1) > 0):           #arrays are checked if they have any cars, if so then prompts first car from [0]
                    self.roadsObj[0].vehiclesInLane1[0].doAction()

                #calling C2
                if (len(self.roadsObj[1].vehiclesInLane1) > 0):
                    self.roadsObj[1].vehiclesInLane1[0].doAction()

                #calling C3
                if (len(self.roadsObj[0].vehiclesInLane2) > 0):
                    self.roadsObj[0].vehiclesInLane2[0].doAction()

                #calling C4
                if (len(self.roadsObj[1].vehiclesInLane2) > 0):
                    self.roadsObj[1].vehiclesInLane2[0].doAction()

                # print(self.occ) #TESTING
                # print(self.roadsObj[0].vehiclesInLane1)  


                #1 second wait between pings (Tick rate of the simulation)
                time.sleep(1)
                
                # adding vehicles back into the system every 15 seconds
                self.countForCarAdd = self.countForCarAdd + 1
                if(self.countForCarAdd >= 15 and self.autoVehicles == True):
                    self.addVehicles()
                    self.countForCarAdd = 0


                #adding pedestrians back into system every 30 seconds        was>=30                   
                self.countForPedAdd = self.countForPedAdd + 1
                if(self.countForPedAdd >= 30 and self.autoPedestrians == True):
                    self.addPedestrians()
                    self.countForPedAdd = 0


                #Automatically ending the program after 100s (Just in case there is a infinite loop)
                self.temp = self.temp + 1
                if(self.temp == 1000):
                    self.running = False

                #cleanup of passed_ arrays
                if len(self.passedPedestrians) >= 100:
                    self.passedPedestrians = []
                if len(self.passedVehicles) >= 100:
                    self.passedVehicles = []

                #Testing prints
                print(self.occ)
                print(self.passedVehicles)
                print("---------")
            
            #FOR TESTING THREADS++++++++++++++++++++++++++++++++++
            # for i in range(100):
            #     print("1", end="", flush=True)
            #     # print(self.checkTrafficSignal(self.roadsObj[1]))
            #     time.sleep(.25)
        except KeyboardInterrupt:
            #ENDING AND CATCHING THREADS
            #ending the trafficlight cycling threads
            self.trafficLightObj[0].operational = False
            self.trafficLightObj[1].operational = False
            self.pedLightObj[0].operational = False
            self.pedLightObj[1].operational = False                                
            #MAYBE INSTALL PACKAGE WHICH ENDS THE THREADS BY THROWING EXCEPTION IN THEM                    -------------------------------------
        #else:

        #Printing done when the main loop is ended
        print("Done")
        print(self.passedVehicles)
        #HAVE FUNCTION WHICH STOPS ALL THE OBJECTS &  THREADS? THOUGH THE LOOP NOT PINGING DOES THAT ANYWAY
        return None





    #Function to create multiple vehicles
    def addVehicles(self):
        tem = self.totalVehicleCount-self.vehicleCount   
        for i in range(tem):
            self.addSingleVehicle()
    
    #method which calls the randomize vehicles function based on how many more vehicles are needed in the system
    #Vehicle parameters randomiser, creates then adds vehicle object which has been created with random paramteres with set probabilities for some
    def addSingleVehicle(self):
        newId = self.vehicleId
        self.vehicleId += 1

        x = random.randint(1,100)
        if x <= 88:
            randType = "car"
        elif x <= 98:
            randType = "publicTransit"
        else:
            randType = "emergencyVehicle"

        y = random.randint(1,10)
        randAction = 2
        if y == 9:
            randAction = 1
        elif y == 10:
            randAction = 3
        else:
            randAction = 2

        randPlate = (''.join(random.choices(string.ascii_uppercase + string.digits, k=7)))
        randRd = (random.randint(0, 1))
        randCarArrayNum = (random.randint(1,4))

        #Adding vehicle to the respective arrays in the roads
        if(randCarArrayNum == 1 or randCarArrayNum == 2): #if car is in vehicle arrays 1
            if(randCarArrayNum == 1):
                self.roadsObj[0].vehiclesInLane1.append(Vehicle(True, False, newId, 40, randType, randPlate, self, self.roadsObj[0], randAction, randCarArrayNum))
            else:
                self.roadsObj[1].vehiclesInLane1.append(Vehicle(True, False, newId, 40, randType, randPlate, self, self.roadsObj[1], randAction, randCarArrayNum))
        else: #if cars are in vehicle arrays 2
            if(randCarArrayNum == 3):
                self.roadsObj[0].vehiclesInLane2.append(Vehicle(True, False, newId, 40, randType, randPlate, self, self.roadsObj[0], randAction, randCarArrayNum))
            else:
                self.roadsObj[1].vehiclesInLane2.append(Vehicle(True, False, newId, 40, randType, randPlate, self, self.roadsObj[1], randAction, randCarArrayNum))
        self.vehicleCount = self.vehicleCount + 1


    #Function which holds an example of a vehicle in each location doing each action
    def testVehicles(self):
        #TESTING
        #cars in C1
        self.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"1",20,"type","ABC",self, self.roadsObj[0], 1, 1))   #going left from c1  
        self.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"2",20,"type","ABC",self, self.roadsObj[0], 2, 1))   #going straight from c1
        self.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"3",20,"type","ABC",self, self.roadsObj[0], 3, 1))   #going right from c1
        #cars in C2
        self.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"4",20,"type","ABC",self, self.roadsObj[1], 1, 2))   #going left from c2  
        self.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"5",20,"type","ABC",self, self.roadsObj[1], 2, 2))   #going straight from c2
        self.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"6",20,"type","ABC",self, self.roadsObj[1], 3, 2))   #going right from c2
        # cars in C3
        self.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"7",20,"type","ABC",self, self.roadsObj[0], 1, 3))   #going left from c3  
        self.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"8",20,"type","ABC",self, self.roadsObj[0], 2, 3))   #going straight from c3
        self.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"9",20,"type","ABC",self, self.roadsObj[0], 3, 3))   #going right from c3
        #cars in C4
        self.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"10",20,"type","ABC",self, self.roadsObj[1], 1, 4))   #going left from c4  
        self.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"11",20,"type","ABC",self, self.roadsObj[1], 2, 4))   #going straight from c4
        self.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"12",20,"type","ABC",self, self.roadsObj[1], 3, 4))   #going right from c4





    #function to create multiple pedestrians
    def addPedestrians(self):
        tem = self.totalPedestrianCount-self.pedestrianCount
        for i in range(tem):
            self.addSinglePedestrian()


    #Method to randomly add pedestrians
    def addSinglePedestrian(self):
        print(self.totalPedestrianCount, "   ",  self.pedestrianCount)
        #getting and updating ID variable
        newId = self.pedId
        self.pedId += 1
        #getting random sidewalk obj number
        sidewalkNum = random.randint(0,3)
        #getting random sidewalk array number
        arrNum = random.randint(1,2)
        
        #if statements for each possibility
        if(sidewalkNum == 0): #adding to road 1, sidewalk obj 1
            if(arrNum == 1):
                self.sidewalksObj[0].sidewalk1.append(Pedestrian(newId, self, 0, self.sidewalksObj[0], 1, 8))
            else:
                self.sidewalksObj[0].sidewalk2.append(Pedestrian(newId, self, 0, self.sidewalksObj[0], 2, 8))
        elif(sidewalkNum == 1): #sidewalk obj2
            if(arrNum == 1):
                self.sidewalksObj[1].sidewalk1.append(Pedestrian(newId, self, 1, self.sidewalksObj[1], 1, 12))   
            else:
                self.sidewalksObj[1].sidewalk2.append(Pedestrian(newId, self, 1, self.sidewalksObj[1], 2, 12))
        elif(sidewalkNum == 2): #sidewalk obj3
            if(arrNum == 1):
                self.sidewalksObj[2].sidewalk1.append(Pedestrian(newId, self, 0, self.sidewalksObj[2], 1, 16))  
            else:
                self.sidewalksObj[2].sidewalk2.append(Pedestrian(newId, self, 0, self.sidewalksObj[2], 2, 16))
        elif(sidewalkNum == 3): #sidewalk obj4
            if(arrNum == 1):
                self.sidewalksObj[3].sidewalk1.append(Pedestrian(newId, self, 1, self.sidewalksObj[3], 1, 4))   
            else:
                self.sidewalksObj[3].sidewalk2.append(Pedestrian(newId, self, 1, self.sidewalksObj[3], 2, 4))
        self.pedestrianCount = self.pedestrianCount + 1
    

    def testPedestrians(self):
        #TESTING
        #Adding Pedestrians to every sidewalk array within the 4 sidewalk objects (2 per obj)
        #using indexes to denote rdnum/rdcross in pedestrian
        #rd1 [0] has sidewalk obj of index 0 and 2   #aka c1 and c3
        #rd2 [1] has sidewalk obj of index 1 and 3   #aka c2 and c4
        #pedestrians in sidewalk 1
        self.sidewalksObj[0].sidewalk1.append(Pedestrian(1, self, 0, self.sidewalksObj[0], 1, 8))                         #make sure about rdcross corresponding to sidew (need to be from same part of intersection)
        self.sidewalksObj[0].sidewalk2.append(Pedestrian(2, self, 0, self.sidewalksObj[0], 2, 8))
        #pedestrians in sidewalk 2
        self.sidewalksObj[1].sidewalk1.append(Pedestrian(3, self, 1, self.sidewalksObj[1], 1, 12))                       
        self.sidewalksObj[1].sidewalk2.append(Pedestrian(4, self, 1, self.sidewalksObj[1], 2, 12))
        #pedestrians in sidewalk 3
        self.sidewalksObj[2].sidewalk1.append(Pedestrian(5, self, 0, self.sidewalksObj[2], 1, 16))                       
        self.sidewalksObj[2].sidewalk2.append(Pedestrian(6, self, 0, self.sidewalksObj[2], 2, 16))
        #pedestrians in sidewalk 4
        self.sidewalksObj[3].sidewalk1.append(Pedestrian(7, self, 1, self.sidewalksObj[3], 1, 4))                       
        self.sidewalksObj[3].sidewalk2.append(Pedestrian(8, self, 1, self.sidewalksObj[3], 2, 4))





    #methods from UML

    #Given a Road object, it returns the current signal colour string for its respective trafficLights
    def checkTrafficSignal(self, rd: Road):
        return self.trafficLightObj[rd.rdNum-1].signalColour
    
    def checkPedestrianSignal(self, rd: Road):
        # checks for pSignal from sidewalk linked to rd
        return self.pedLightObj[rd.rdNum-1].signalColour
    

    #Function for emergency vehicle or accident on road, which immediately sets all lights to red, thus halting the intersection
    #Run as thread, set all occupancy variables to 1, wait x amount of seconds before restarting loop
    #spawn emergency vehicle to front of one of the vehicle arrays
    def requestEmergency(self):
        self.running = False
        self.pedLightObj[0].signalColour = "red"
        self.pedLightObj[1].signalColour = "red"
        self.trafficLightObj[0].signalColour = "red"
        self.trafficLightObj[1].signalColour = "red"

    

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