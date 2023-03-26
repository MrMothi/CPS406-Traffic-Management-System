import time

class TrafficLight:
    
    signalTime = 5 #class variable for the traffic signal timings, can be edited globally by the intersection class

    def __init__(self, operational, signalColour):                #  , timeRed, timeGreen, timeYellow
        self.operational = operational #bool
        self.signalColour = signalColour #string
        # self.timeRed = timeRed #int
        # self.timeGreen = timeGreen #int
        # self.timeYellow = timeYellow #int

    def cycleLight(self):
        while (self.operational):
            self.signalColour = "red"
            print("Now red", flush=True)
            time.sleep(self.signalTime)
            self.signalColour = "green"
            print("Now green", flush=True)
            time.sleep(self.signalTime)
            print("Now yellow", flush=True)
            self.signalColour = "yellow"
            time.sleep(self.signalTime/2)
        return