import time

class TrafficLight:
    greenTime = 8                       # sleep counter for green light
    yellowTime = 4                      # sleep counter for yellow light
    redTime = greenTime + yellowTime    # sleep counter for red light (stays red during the duration of green and yellow)

    def __init__(self, operational, signalColour, inter):   
        self.operational = operational #bool
        self.resetColour = signalColour #set a colour for the reset state
        self.signalColour = self.resetColour #string
        self.inter = inter
        self.timer = 0                  # timer initializes as 0
        self.reset()                    # initialize timer for the cycle (based off of its signal colour)

    def setColour(self, colour):
        self.signalColour = colour

    # thread run cycle    
    def cycle(self):
        while (self.inter.notfinished):
            # updates timer and light colour if the object is operational (bool)
            if self.operational:
                # light colour set to black if not operational so when it's operational again, reset the light colour and timer
                if self.signalColour == "black":
                    self.reset()
                # if light colour timer runs out, update light colour and update timer to correspond with light colour
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
                    # decrement sleep timer
                    self.timer -= 1
                    time.sleep(1)
            else:
                # if there's an emergency, set lights to red, otherwise to black (default when not operational)
                if(self.inter.emergency == True):
                    self.setColour("red")
                    time.sleep(1)
                else:
                    self.setColour("black")
                    self.timer = 0
                    time.sleep(1)
    
    # sets the timer to 0 so the thread cycle skips to the next colour
    def cycleNext(self):
        self.timer = 0
        return self.signalColour # returns the next colour from cycling
    
    # reset signal colour to the preset default, update timer accordingly
    def reset(self):
        if self.resetColour == "red":
            self.timer = TrafficLight.redTime
        elif self.resetColour == "green":
            self.timer = TrafficLight.greenTime
        elif self.resetColour == "yellow":
            self.timer = TrafficLight.yellowTime
        self.signalColour = self.resetColour
