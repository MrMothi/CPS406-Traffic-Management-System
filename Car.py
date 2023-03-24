class Car(Vehicle):
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate, car_type):
        super().__init__(operational, inIntersection, stopped, name, speed, type, plate)
        self.carType = car_type
        self.operational = operational
        self.inIntersection = inIntersection
        self.stopped = stopped
        self.name = name
        self.speed = speed
        self.type = type
        self.plate = plate
