from Intersection import *
from TitleScreen import *   #Comment this line before testing via TestCases.py, if running TrafficSystem.py regularly then make sure it is uncommented

class TrafficSystem:
    intersectionName = "MetroFloRoad"
    inter = None #variable for the intersection object (Future expansion to list of intersections)
    userInfoDict = {
        "Admin1" : "Pa55word",
        "Admin2" : "traffic",
        "admin"  : "pass",
        "a" : "a"
    }

    #variable for logged in state or not
    loggedIn = False
    
    @classmethod
    def login(cls, username:str = "", password: str = ""):
        if username in cls.userInfoDict.keys() and cls.userInfoDict[username] == password:
            cls.loggedIn = True
        else:
            cls.loggedIn = False
        return cls.loggedIn

    #Function to create the intersection, and returns a reference to it
    @classmethod
    def initializeIntersection(cls):
        cls.inter = Intersection(10, 4, "", totalPedestrianCount=10, totalVehicleCount=10) #need to check if params even do anything
        return cls.inter

if __name__ == "__main__":
    create_title_screen()
