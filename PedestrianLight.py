from TrafficLight import *

class PedestrianLight:
    # timers correspond to the length of the trafficlight class timers
    greenTime = TrafficLight.greenTime   #default signal time for PedestrianLight
    redTime = TrafficLight.redTime + TrafficLight.yellowTime # account for both yellow lights

    def __init__(self, operational, hasAudibleSignal, signalColour, inter):           #timeToWalk, walkTiming
        self.operational = operational
        self.hasAudibleSignal = hasAudibleSignal #bool
        self.resetColour = signalColour
        self.signalColour = self.resetColour #string either walk or stop
        self.walkTimeRemaining = 0
        self.inter = inter
        self.timer = 0
        self.reset()
    
    # change the colour
    def setColour(self, colour):
        self.signalColour = colour

    # main function for the thread to cycle 
    def cycle(self):
        while (self.inter.notfinished):
            # update timer and colour when operational
            if (self.operational):
                if self.signalColour == "black":
                    self.reset()
                elif self.timer <= 0:
                    print(f"Ped {self.signalColour}", flush=True)
                    if self.signalColour == "green":
                        self.setColour("red")
                        self.timer = PedestrianLight.redTime
                    elif self.signalColour == "red":
                        self.setColour("green")
                        self.timer = PedestrianLight.greenTime
                else:
                    self.timer -= 1
                    time.sleep(1)
            else:
                if(self.inter.emergency == True):
                    self.setColour("red")
                    time.sleep(1)
                else:
                    self.setColour("black")
                    self.timer = 0
                    time.sleep(1)
    
    def cycleNext(self):
        self.timer = 0
        return self.signalColour

    # set signal colour and timer to preset
    def reset(self):
        if self.resetColour == "red":
            self.timer = PedestrianLight.redTime - TrafficLight.yellowTime # doesnt account for first yellow timer on initial
        elif self.resetColour == "green":
            self.timer = PedestrianLight.greenTime
        self.signalColour = self.resetColour

    def setStop(self):
        return True
    
    def setGo(self):
        return True
    
     #NOTE: JUST SKELETON CODE FOR NOW, WILL NEED TO IMPLEMENT THEM LATER WHEN WRITING MAIN CODE