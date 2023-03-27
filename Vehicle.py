from Intersection import *
from Road import *

class Vehicle:
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum):
        self.operational = True
        self.inIntersection = True  #<=== maybe delete
        self.stopped = True
        self.name = name #car id
        self.speed = 0
        self.type = "" #can be either car, public transport, or emergency
        self.plate = ""
        self.inter = inter  #Intersection object reference
        self.rd = rd #Road object reference which holds the vehicle
        self.actionType = actionType #if the car is given an action type to do
        self.carArrayNum = carArrayNum #Number to indicate which vehicle array the vehicle is in
        self.moveTime = 2 #default movetime (Base on speed for future) =======================================

    #Variable Numbering info
    #carArrayNum, based on the C# indicate which vehicle array the vehicle is in goes from 1-4
    #actionType, indicates which action the car will do
                    #1 means go left
                    #2 means go straight
                    #3 means go right

    #Most of the logic is hardcoded in ifstatements, while it is possible to code this by doing modulo addition and subtraction on the variables
    def doAction(self):
        print(self.name) #For testing prints ID when prompted
        #If car is in rd 1, C1
        if(self.carArrayNum == 1):
            print("a")
            #checks if stoplight is green for rd1
            if(self.inter.checkTrafficSignal(self.rd) == "green"):       
                print("b")
                #if going left (ARROW #1)
                if(self.actionType == 1):
                    print("c")
                      #checking pedestrian,     car from left,              and oncoming right turn          4 6
                    if(self.inter.occ[3] <= 0 and self.inter.occ[5] <= 0):
                        print("d")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[0] = 10 #self.moveTime
                        self.inter.updateAfterTime(0)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action1")

                #if going straight (ARROW #2)
                if(self.actionType == 2):
                    #checking pedestrian
                    if(self.inter.occ[15] <= 0):               
                        #calling thread to change the occupied variable, after setting it to moveTime        16
                        self.inter.occ[1] = self.moveTime
                        self.inter.updateAfterTime(0)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action2")
                
                #if turning right (ARROW #3)
                if(self.actionType == 2):
                    #checking pedestrian           oncoming forward             oncoming left                12 10 9
                    if(self.inter.occ[11] <= 0 and self.inter.occ[9] <= 0 and self.inter.occ[8] <= 0):
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[1] = self.moveTime
                        self.inter.updateAfterTime(0)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action3")
        
        print("Waiting", self.name)

#Right of way going straight, leftturn, then rightturn
#ie leftturn checks pedestrian and vehicle coming from left
#ie goingstraight checks pedestrian
#ie right turn checks pedestrian, oncoming forward, leftturn from oncoming


    def getRandomAction():
        #maybe 80% of the time is straight
        #10% left and right respectively
        pass