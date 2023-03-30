from Intersection import *

class TrafficSystem:
    intersectionName = "MetroFloRoad"
    inter = None  #variable for the intersection object (Future expansion to list of intersections)
    userInfoDict = {
        "Admin1" : "Pa55word",
        "Admin2" : "traffic"
    }


    #implement login system here, backend for the frontend
    
    #prototype
    loggedIn = False
    
    @classmethod
    def login(cls):
        username = str(input("Username: "))
        password = str(input("Password: "))
        
        if username in TrafficSystem.userInfoDict.keys() and TrafficSystem.userInfoDict[username] == password:
            TrafficSystem.loggedIn = True
        else:
            TrafficSystem.loggedIn = False
        return



    #Function to create the intersection, and returns a reference to it
    @classmethod
    def initializeIntersection(cls):
        inter = Intersection(10, 4, "", pedestrianCount=10, totalVehicleCount=10)
        return inter

