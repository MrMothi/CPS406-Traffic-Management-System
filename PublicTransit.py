import Vehicle
class PublicTransit(Vehicle):
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate, inBusLane):
        super().__init__(operational, inIntersection, stopped, name, speed, type, plate)
        self.inBusLane = inBusLane  #setting special instance variable
        # self.operational = operational
        # self.inIntersection = inIntersection
        # self.stopped = stopped
        # self.name = name
        # self.speed = speed
        # self.type = type
        # self.plate = plate
