class TrafficSystem:
    intersectionName = "MetroFloRoad"
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

#not object class
#fjfjfeof