class Vehicle:
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate ):
        self.operational = True
        self.inIntersection = True
        self.stopped = True
        self.name = "" #car id
        self.speed = 0
        self.type = "" #can be either car, public transport, or emergency
        self.plate = ""
