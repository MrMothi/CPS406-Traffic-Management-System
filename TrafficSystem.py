from Intersection import *
from TitleScreen import *

class TrafficSystem:
    intersectionName = "MetroFloRoad"
    inter = None #variable for the intersection object (Future expansion to list of intersections)
    userInfoDict = {
        "Admin1" : "Pa55word",
        "Admin2" : "traffic",
        "a" : "a"
    }

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
    # if(cls.testing = False)
    create_title_screen()
