import time

class TrafficLight:
    greenTime = 8
    yellowTime = 4
    redTime = greenTime + yellowTime

    def __init__(self, operational, signalColour, inter):   
        self.operational = operational #bool
        self.resetColour = signalColour #set a colour for the reset state
        self.signalColour = self.resetColour #string
        self.inter = inter
        self.timer = 0
        self.reset()

    def setColour(self, colour):
        self.signalColour = colour
    
    def cycle(self):
        while (self.inter.notfinished):
            if self.operational:
                if self.signalColour == "black":
                    self.reset()
                elif self.timer <= 0:
                    print(f"Now {self.signalColour}", flush=True)
                    if self.signalColour == "green":
                        self.setColour("yellow")
                        self.timer = TrafficLight.yellowTime
                    elif self.signalColour == "red":
                        self.setColour("green")
                        self.timer = TrafficLight.greenTime
                    elif self.signalColour == "yellow":
                        self.setColour("red")
                        self.timer = TrafficLight.redTime
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
        return self.signalColour # returns the next colour from cycling
    
    def reset(self):
        if self.resetColour == "red":
            self.timer = TrafficLight.redTime
        elif self.resetColour == "green":
            self.timer = TrafficLight.greenTime
        elif self.resetColour == "yellow":
            self.timer = TrafficLight.yellowTime
        self.signalColour = self.resetColour
