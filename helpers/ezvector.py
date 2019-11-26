class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return f"ezpg.Vector object : [{self.x}, {self.y}, {self.z}]"

    def set(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return createVector(self.x, self.y, self.z)

def createVector(x=0, y=0, z=0):
    return Vector(x, y, z)