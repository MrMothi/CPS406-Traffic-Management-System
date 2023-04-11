import time
# from TrafficSystem import *
# import TrafficSystem

class TrafficLight:
    
    defaultTime = 10
    accelTime = 5
    signalTime = defaultTime #default class variable for the traffic signal timings, can be edited globally by the intersection class

    def __init__(self, operational, signalColour, inter):   
        self.operational = operational #bool
        self.signalColour = signalColour #string
        self.inter = inter
        if self.signalColour == "red":
            self.timer = self.signalTime
        elif self.signalColour == "yellow":
            self.timer = self.signalTime/4
        else:
            self.timer = self.signalTime - (self.signalTime/4)

    def setColour(self, colour):
        self.signalColour = colour
    
    # Implement general light cycle, makes it easier to accelerate and immediate change from admin
    def cycleLight(self, reduceRed=False):
        while (self.inter.notfinished):
            if (self.operational):
                print(self.signalTime)
                print(f"Now {self.signalColour}", flush=True)
                if self.signalColour == "green":
                    time.sleep(self.signalTime - (self.signalTime/4))
                    self.setColour("yellow")
                elif self.signalColour == "yellow":
                    time.sleep(self.signalTime/4)
                    self.setColour("red")
                elif self.signalColour == "red":
                    if reduceRed:
                        time.sleep(self.signalTime/4)
                        reduceRed = False
                    else:
                        time.sleep(self.signalTime)
                    self.setColour("green")
        return

    #implement methods for changing signal to specific colour, make this break the threads and apply to both?