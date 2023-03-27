class PedestrianLight:
    signalTime = 4   #default signal time for PedestrianLight
    
    def __init__(self, operational, hasAudibleSignal, signalColour):           #timeToWalk, walkTiming
        self.operational = operational
        self.hasAudibleSignal = hasAudibleSignal #bool
        self.signalColour = signalColour #string either walk or stop
        self.walkTimeRemaining = 0
        # self.timeToWalk = timeToWalk #int
        # self.walkTiming = walkTiming #int
    


    #Two cycleLight methods to have two separate running loops which are opposite to eachother in signal colour
    def cycleLight1(self):
        while (self.operational):                       #trafficlight is signaltime 
            self.signalColour = "stop"
            print("Now red1", flush=True)
            time.sleep(self.signalTime)      
            self.signalColour = "green"
            print("Now green1", flush=True)
            time.sleep(self.signalTime - (self.signalTime/2))
        return
    
    def cycleLight2(self):
        while (self.operational):
            self.signalColour = "green"
            print("Now green2", flush=True)
            time.sleep(self.signalTime - (self.signalTime/2))
            self.signalColour = "red"
            print("Now red2", flush=True)
            time.sleep(self.signalTime)
        return















    def setStop(self):
        return True
    
    def setGo(self):
        return True
    
     #NOTE: JUST SKELETON CODE FOR NOW, WILL NEED TO IMPLEMENT THEM LATER WHEN WRITING MAIN CODE
