from Vehicle import Vehicle 
class PublicTransit(Vehicle):
    def __init__(self, operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum, inBusLane):
        super().__init__(operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum)
        self.inBusLane = inBusLane  #setting special instance variable
        # self.operational = operational
        # self.inIntersection = inIntersection
        # self.stopped = stopped
        # self.name = name
        # self.speed = speed
        # self.type = type
        # self.plate = plate
