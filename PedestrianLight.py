class PedestrianLight:
    def __init__(self, operational, hasAudibleSignal, signalColour, timeToWalk, walkTiming):
        self.operational = operational
        self.hasAudibleSignal = hasAudibleSignal #bool
        self.signalColour = signalColour #string
        self.timeToWalk = timeToWalk #int
        self.walkTiming = walkTiming #int
    
    def setStop(self):
        return True
    
    def setGo(self):
        return True
    
     #NOTE: JUST SKELETON CODE FOR NOW, WILL NEED TO IMPLEMENT THEM LATER WHEN WRITING MAIN CODE
