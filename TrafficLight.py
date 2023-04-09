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


    #Two cycleLight methods to have two separate running loops which are opposite to eachother in signal colour
    def cycleLight1(self):
        while (self.operational):
            print(self.signalTime)
            self.signalColour = "red"
            print("Now red1", flush=True)
            time.sleep(self.signalTime)
            self.signalColour = "green"
            print("Now green1", flush=True)
            time.sleep(self.signalTime - (self.signalTime/4))
            print("Now yellow1", flush=True)
            self.signalColour = "yellow"
            time.sleep(self.signalTime/4)
        return
    
    def cycleLight2(self):
        while (self.operational):
            print(self.signalTime)
            self.signalColour = "green"
            print("Now green2", flush=True)
            time.sleep(self.signalTime - (self.signalTime/4))
            self.signalColour = "yellow"
            print("Now yellow2", flush=True)
            time.sleep(self.signalTime/4)
            self.signalColour = "red"
            print("Now red2", flush=True)
            time.sleep(self.signalTime)
        return
    
    def setColour(self, colour):
        self.signalColour = colour
    
    # Implement general light cycle, makes it easier to accelerate and immediate change from admin
    def cycleLight(self, reduceRed=False):
        while( self.inter.notfinished ):
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