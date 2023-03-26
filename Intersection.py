import Road

class Intersection:
    def __init__(self, stoplightTiming: int, pedestrianLightTiming: int, weather: str, running: bool = False,
        pedestrianCount: int = 0, vehicleCount: int = 0, incident: bool = False, crossSignalRequested: bool = False, speedsData = []):

        self.stoplightTiming = stoplightTiming
        self.pedestrianLightTiming = pedestrianLightTiming
        self.weather = weather
        self.roads =  roads: tuple(Road, Road)
        self.running = running
        self.pedestrianCount = pedestrianCount
        self.vehicleCount = vehicleCount
        self.incident = incident
        self.crossSignalRequested = crossSignalRequested
        self.speedsData = speedsData

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
