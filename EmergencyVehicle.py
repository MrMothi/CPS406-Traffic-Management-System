class EmergencyVehicle(Vehicle):
    def __init__(self, operational, inIntersection, stopped, name, speed, type, plate, onScene, emergencyType, emergencySignal):
        super().__init__(operational, inIntersection, stopped, name, speed, type, plate)
        self.operational = operational
        self.inIntersection = inIntersection
        self.stopped = stopped
        self.name = name
        self.speed = speed
        self.type = type
        self.plate = plate
        self.onScene = onScene
        self.emergencyType = emergencyType
        self.emergencySignal = emergencySignal
