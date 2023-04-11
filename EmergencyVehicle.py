from Vehicle import Vehicle   #importing superclass of vehicle
class EmergencyVehicle(Vehicle):
    def __init__(self, operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum, onScene, emergencyType, emergencySignal, ):
        super().__init__(operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum)
        self.onScene = onScene                         #setting any special instance variables for this type of vehicle
        self.emergencyType = emergencyType
        self.emergencySignal = emergencySignal

        # self.operational = operational
        # self.stopped = stopped
        # self.name = name
        # self.speed = speed
        # self.type = type
        # self.plate = plate
