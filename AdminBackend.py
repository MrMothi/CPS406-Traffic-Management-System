import Intersection
from Vehicle import EmergencyVehicle

class AuthorizedUser:
    def __init__(self, userEmail, password):
        self.userEmail = userEmail
        self.password = password

    def setSpeed(self, subject: Intersection, speed:int ):
        return True
    
    def setSignalTiming(self, stoplight: int, pedestrianLight: int):
        return None
    
    def setEmergencySignal(self, subject: EmergencyVehicle, emergencySignal: str):
        return None
    
    def addVehicle(self, name: str, speed: int, type: str):
        return None
    
    def addPedestrian(self, name: str):
        return None
    
    def getCurrentData(self):
        return [] #supposed to return an array
    
    def login(self, user: str, password: str):
        return True
    
    def logout(self):
        return None
