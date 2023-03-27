from TrafficLight import *

class PedestrianLight:
    signalTime = 4   #default signal time for PedestrianLight
    
    def __init__(self, operational, hasAudibleSignal, signalColour):           #timeToWalk, walkTiming
        self.operational = operational
        self.hasAudibleSignal = hasAudibleSignal #bool
        self.signalColour = signalColour #string either walk or stop
        self.walkTimeRemaining = 0
        self.trafficLightSigTime = TrafficLight.signalTime

    


    #Two cycleLight methods to have two separate running loops which are opposite to eachother in signal colour
    def cycleLight2(self):
        while (self.operational):                       #trafficlight is signaltime 
            self.signalColour = "red"
            print("Now stop2", flush=True)
            time.sleep(self.trafficLightSigTime + (self.trafficLightSigTime - self.signalTime))  #running red for the trafficSignal Time
            self.signalColour = "green"                                                            #plus any left over from pedestrian signal time    
            print("Now walk2", flush=True)
            time.sleep(self.signalTime)
        return
    
    def cycleLight1(self):
        while (self.operational):
            self.signalColour = "green"                                                            
            print("Now walk1", flush=True)
            time.sleep(self.signalTime)
            self.signalColour = "red"
            print("Now stop1", flush=True)
            time.sleep(self.trafficLightSigTime + (self.trafficLightSigTime - self.signalTime)) 
        return















    def setStop(self):
        return True
    
    def setGo(self):
        return True
    
     #NOTE: JUST SKELETON CODE FOR NOW, WILL NEED TO IMPLEMENT THEM LATER WHEN WRITING MAIN CODE