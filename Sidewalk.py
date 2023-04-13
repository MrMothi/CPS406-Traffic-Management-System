class SideWalk:
    def __init__(self, inter, operational, s1, s2):
        self.inter = inter #intersection object reference
        self.operational = operational #bool
        self.sidewalk1 = s1 #list
        self.sidewalk2 = s2 #list


    def getStatus(self):
        return self.operational