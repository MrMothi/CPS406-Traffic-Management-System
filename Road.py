class Road:
    def __init__(self, operational, hasBusLane, hasSpeedCameras, sideWalks, vehiclesInLane1, vehiclesInLane2, rdNum):
        self.operational = operational #bool
        self.hasBusLane = hasBusLane #bool
        self.hasSpeedCameras = hasSpeedCameras #bool
        self.sideWalks = sideWalks #array
        self.vehiclesInLane1 = vehiclesInLane1 #arraylist queue vehicle         (rdnum) x1
        self.vehiclesInLane2 = vehiclesInLane2 #arraylist queue vehicle         (rdnum +2) x2

        #figure out the way to indicate which of the 1-4 arrays this is
        self.rdNum = rdNum     #do math to figure out the variables to check per vehicle array

    
    def getStatus(self):
        return self.operational
    