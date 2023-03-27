from Vehicle import Vehicle 
class Car(Vehicle):
    def __init__(self, operational, stopped, name, speed, type, plate,  inter, rd, actionType, carArrayNum, car_type):
        super().__init__(operational, stopped, name, speed, type, plate, inter, rd, actionType, carArrayNum)
        self.carType = car_type
        # self.operational = operational
        # self.inIntersection = inIntersection
        # self.stopped = stopped
        # self.name = name
        # self.speed = speed
        # self.type = type
        # self.plate = plate