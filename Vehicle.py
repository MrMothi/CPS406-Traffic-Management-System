from Intersection import *
from Road import *

class Vehicle:
    def __init__(self, operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum):
        self.operational = True
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

    #Right of way going straight, leftturn, then rightturn
    #ie leftturn checks pedestrian and vehicle coming from left
    #ie goingstraight checks pedestrian
    #ie right turn checks pedestrian, oncoming forward, leftturn from oncoming


    #Most of the logic is hardcoded in ifstatements, while it is possible to code this by doing modulo addition and subtraction on the variables
    # Numbers on the side tell which occ variables are being checked (index+1)
    def doAction(self):
        print(self.name) #For testing prints ID when prompted
        #If car is in rd 1, C1
        if(self.carArrayNum == 1):
            print("c1")
            #checks if stoplight is green for rd1
            if(self.inter.checkTrafficSignal(self.rd) == "green"):                                    #FOR THIS CHECK, IF NEEDED ADD A TIME CHECK TO NOT ALLOW ANY ARROWS WHILE RED (PREVIOUSLY MADE FROM GREENLIGHT)
                print("grenR1")                                                                                  #   and checkIfTrafficLightTime > moveTime
                #if going left (ARROW #1)
                if(self.actionType == 1):
                    print("a1")
                    #checking pedestrian,     car from left,                                                 4 6
                    if(self.inter.occ[3] <= 0 and self.inter.occ[5] <= 0):
                        print("clear1")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[0] = self.moveTime #self.moveTime
                        self.inter.updateAfterTime(0)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action1")

                #if going straight (ARROW #2)
                elif(self.actionType == 2):
                    print("a2")
                    #checking pedestrian                                                                     16
                    if(self.inter.occ[15] <= 0):               
                        print("clear2")
                        #calling thread to change the occupied variable, after setting it to moveTime        
                        self.inter.occ[1] = self.moveTime
                        self.inter.updateAfterTime(1)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action2")
                
                #if turning right (ARROW #3)
                elif(self.actionType == 3):
                    print("a3")
                    #checking pedestrian           oncoming forward             oncoming left                12 10 9
                    if(self.inter.occ[11] <= 0 and self.inter.occ[9] <= 0 and self.inter.occ[8] <= 0):
                        print("clear3")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[2] = self.moveTime
                        self.inter.updateAfterTime(2)
                        #delete car from C1 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action3")
        
        #If car is in rd 2, C2
        elif(self.carArrayNum == 2):
            print("c2")
            #checks if stoplight is green for rd2
            if(self.inter.checkTrafficSignal(self.rd) == "green"):    
                print("grenR2")
                #if going left (ARROW #5)
                if(self.actionType == 1):
                    print("a1")
                    #checking pedestrian,     car from left,                                                  8 10            
                    if(self.inter.occ[7] <= 0 and self.inter.occ[9] <= 0):
                        print("clear1")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[4] = self.moveTime #self.moveTime
                        self.inter.updateAfterTime(4)
                        #delete car from C2 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action1")

                #if going straight (ARROW #6)
                elif(self.actionType == 2):
                    print("a2")
                    #checking pedestrian                                                                     4
                    if(self.inter.occ[3] <= 0):               
                        print("clear2")
                        #calling thread to change the occupied variable, after setting it to moveTime        
                        self.inter.occ[5] = self.moveTime
                        self.inter.updateAfterTime(5)
                        #delete car from C2 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action2")
                
                #if turning right (ARROW #7)
                elif(self.actionType == 3):
                    print("a3")
                    #checking pedestrian           oncoming forward             oncoming left                16 14 13
                    if(self.inter.occ[15] <= 0 and self.inter.occ[13] <= 0 and self.inter.occ[12] <= 0):
                        print("clear3")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[6] = self.moveTime
                        self.inter.updateAfterTime(6)
                        #delete car from C2 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane1.pop(0))
                        print("Action3")

        #If car is in rd 1, C3
        elif(self.carArrayNum == 3):
            print("c3")
            #checks if stoplight is green for rd1
            if(self.inter.checkTrafficSignal(self.rd) == "green"):       
                print("grenR1")
                #if going left (ARROW #9)
                if(self.actionType == 1):
                    print("a1")
                    #checking pedestrian,     car from left,                                                 12 14
                    if(self.inter.occ[11] <= 0 and self.inter.occ[13] <= 0):
                        print("clear1")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[8] = self.moveTime #self.moveTime
                        self.inter.updateAfterTime(8)
                        #delete car from C3 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action1")

                #if going straight (ARROW #10)
                elif(self.actionType == 2):
                    print("a2")
                    #checking pedestrian                                                                     8
                    if(self.inter.occ[7] <= 0):               
                        print("clear2")
                        #calling thread to change the occupied variable, after setting it to moveTime        
                        self.inter.occ[9] = self.moveTime
                        self.inter.updateAfterTime(9)
                        #delete car from C3 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action2")
                
                #if turning right (ARROW #11)
                elif(self.actionType == 3):
                    print("a3")
                    #checking pedestrian           oncoming forward             oncoming left                4 2 1
                    if(self.inter.occ[3] <= 0 and self.inter.occ[1] <= 0 and self.inter.occ[0] <= 0):
                        print("clear3")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[10] = self.moveTime
                        self.inter.updateAfterTime(10)
                        #delete car from C3 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action3")
        
        #If car is in rd 2, C4
        elif(self.carArrayNum == 4):
            print("c4")
            #checks if stoplight is green for rd2
            if(self.inter.checkTrafficSignal(self.rd) == "green"):    
                print("grenR2")
                #if going left (ARROW #13)
                if(self.actionType == 1):
                    print("a1")
                    #checking pedestrian,     car from left,                                                 16 2                      
                    if(self.inter.occ[15] <= 0 and self.inter.occ[1] <= 0):
                        print("clear1")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[12] = self.moveTime #self.moveTime
                        self.inter.updateAfterTime(12)
                        #delete car from C4 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action1")

                #if going straight (ARROW #14)
                elif(self.actionType == 2):
                    print("a2")
                    #checking pedestrian
                    if(self.inter.occ[11] <= 0):               
                        print("clear2")
                        #calling thread to change the occupied variable, after setting it to moveTime        12
                        self.inter.occ[13] = self.moveTime
                        self.inter.updateAfterTime(13)
                        #delete car from C4 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action2")
                
                #if turning right (ARROW #15)
                elif(self.actionType == 3):
                    print("a3")
                    #checking pedestrian           oncoming forward             oncoming left                8 6 5
                    if(self.inter.occ[7] <= 0 and self.inter.occ[5] <= 0 and self.inter.occ[4] <= 0):
                        print("clear3")
                        #calling thread to change the occupied variable, after setting it to moveTime
                        self.inter.occ[14] = self.moveTime
                        self.inter.updateAfterTime(14)
                        #delete car from C4 list
                        self.inter.passedVehicles.append(self.rd.vehiclesInLane2.pop(0))
                        print("Action3")


        #if None of the if statements match, then print wait and do nothing
        print("Waiting", self.name)


    def getRandomAction():
        #maybe 80% of the time is straight
        #10% left and right respectively
        pass