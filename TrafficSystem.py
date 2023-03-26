import Intersection

class TrafficSystem:
    intersectionName = "MetroFloRoad"
    Intersection inter
    userInfoDict = {
        "Admin1" : "Pa55word",
        "Admin2" : "traffic"
    }


    #Function to create the intersection
    def initializeIntersection():
        inter = Intersection()



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

#not object class
#fjfjfeof