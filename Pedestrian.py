import Sidewalk
class Pedestrian:
    def __init__(self, crossing, name):
        self.crossing = crossing #bool
        self.name = name #bool

    def crossStreet(self): #changing it from destination:Sidewalk bc we are no longer following pedestrian after crossing - simplifying things
        return bool
    
    def requestCrossSignal(self):
        return bool
    
    def checkCrossLight(self, destination: Sidewalk): #leaving destination:sidwalk for now bc we prolly gonna be checking which sidewalk they on before crossing
        return ""
