from TrafficLight import *

class PedestrianLight:
    greenTime = TrafficLight.signalTime - (TrafficLight.signalTime/4)   #default signal time for PedestrianLight
    redTime = TrafficLight.signalTime + (TrafficLight.signalTime/4)
    
    def __init__(self, operational, hasAudibleSignal, signalColour):           #timeToWalk, walkTiming
        self.operational = operational
        self.hasAudibleSignal = hasAudibleSignal #bool
        self.signalColour = signalColour #string either walk or stop
        self.walkTimeRemaining = 0
        self.greenTime = PedestrianLight.greenTime
        self.redTime = PedestrianLight.redTime


    #Two cycleLight methods to have two separate running loops which are opposite to eachother in signal colour
    def cycleLight2(self):
        self.redTime = TrafficLight.signalTime
        while (self.operational):                       #trafficlight is signaltime 
            self.signalColour = "red"
            print("Now stop2", flush=True)
            time.sleep(self.redTime)  #running red for the trafficSignal Time
            self.redTime = PedestrianLight.redTime
            self.signalColour = "green"                                                            #plus any left over from pedestrian signal time    
            print("Now walk2", flush=True)
            time.sleep(self.greenTime)
        return
    
    def cycleLight1(self):
        while (self.operational):
            self.signalColour = "green"                                                            
            print("Now walk1", flush=True)  
            time.sleep(self.greenTime)
            self.signalColour = "red"
            print("Now stop1", flush=True)
            time.sleep(self.redTime) 
        return















    def setStop(self):
        return True
    
    def setGo(self):
        return True
    
     #NOTE: JUST SKELETON CODE FOR NOW, WILL NEED TO IMPLEMENT THEM LATER WHEN WRITING MAIN CODE