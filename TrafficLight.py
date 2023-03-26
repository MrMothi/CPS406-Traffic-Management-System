import time

class TrafficLight:
    
    signalTime = 5 #class variable for the traffic signal timings, can be edited globally by the intersection class

    def __init__(self, operational, signalColour):   
        self.operational = operational #bool
        self.signalColour = signalColour #string


    #Two cycleLight methods to have two separate running loops which are opposite to eachother in signal colour
    def cycleLight1(self):
        while (self.operational):
            self.signalColour = "red"
            print("Now red1", flush=True)
            time.sleep(self.signalTime)
            self.signalColour = "green"
            print("Now green1", flush=True)
            time.sleep(self.signalTime - (self.signalTime/2))
            print("Now yellow1", flush=True)
            self.signalColour = "yellow"
            time.sleep(self.signalTime/2)
        return
    
    def cycleLight2(self):
        while (self.operational):
            self.signalColour = "green"
            print("Now green2", flush=True)
            time.sleep(self.signalTime - (self.signalTime/2))
            self.signalColour = "yellow"
            print("Now yellow2", flush=True)
            time.sleep(self.signalTime/2)
            self.signalColour = "red"
            print("Now red2", flush=True)
            time.sleep(self.signalTime)
        return