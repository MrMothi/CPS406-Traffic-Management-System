from Intersection import *
#Pedestrians are randomly placed within any of the 8 pedestrian arrays, and check the respective pedestrianLight to cross
class Pedestrian:
    def __init__(self, name, inter, rdcross, sidew, side, occnum):
        self.inter = inter
        self.name = name #bool
        self.rdcross = rdcross #variable indicated which pedestrian light to look at for crossing the road
        #rdcross == 1 then crossing across rd1
        #rdcross == 2 then crossing across rd2
        self.sidew = sidew  #variable holding reference to sidewalk holding this pedestrian
        self.side = side #variable holding integer which corresponds to either array1 or array2 within sidewalk that holds pedestrians
        self.occnum = occnum #Variable holding occnum


    #Function that is called by the main loop to induce a check to cross
    def tryCrossRoad(self):
        #checking the respective pedestrian lights, for the road that is being crossed
        if(self.inter.pedLightObj[self.rdcross].signalColour == "green"):
            #updating occ variable
            self.inter.occ[self.occnum-1] = 2 #2 seconds for the pedestrians to cross
            self.inter.updateAfterTime(self.occnum-1)
            #removing from respective array
            if(self.side == 1):
                self.sidew.sidewalk1.pop(0) #removing pedestrian from sidewalk1 array within sidewalk obj
            else:
                self.sidew.sidewalk2.pop(0) #removing from sidewalk2
            self.inter.pedestrianCount = self.inter.pedestrianCount - 1
        return True
    

    def requestCrossSignal(self):   # maybe leave out
        return True
    



    # def checkCrossLight(self, destination: Sidewalk): #leaving destination:sidwalk for now bc we prolly gonna be checking which sidewalk they on before crossing
    #     return ""
    #single if statement if ^ then go otherwise dont



