class Road:
    def __init__(self, operational, hasBusLane, hasSpeedCameras, sideWalks, vehiclesInLane1, vehiclesInLane2):
        self.operational = operational #bool
        self.hasBusLane = hasBusLane #bool
        self.hasSpeedCameras = hasSpeedCameras #bool
        self.sideWalks = sideWalks #array
        self.vehiclesInLane1 = vehiclesInLane1 #arraylist queue vehicle
        self.vehiclesInLane2 = vehiclesInLane2 #arraylist queue vehicle
