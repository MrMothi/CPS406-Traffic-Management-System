class Car(Vehicle):
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate, car_type):
        super().__init__(operational, inIntersection, stopped, name, speed, type, plate)
        self.car_type = car_type
