import math

class Vector:
    def __init__(self, x: float = 0.0,
                       y: float = 0.0,
                       z: float = 0.0):
        self.x, self.y, self.z = x, y, z

    def length_sqr(self):
        return self.x**2 + self.y**2 + self.z**2
    def length(self):
        return math.sqrt(self.length_sqr())

    def normal(self):
        return Vector(self.x, self.y, self.z) / self.length()

    def __neg__(self):
        return self.__class__(-self.x, -self.y, -self.z)

    def __pos__(self):
        return self.__class__(+self.x, +self.y, +self.z)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"expected Vector, got {type(other)}")
        return self.__class__(self.x + other.x,
                              self.y + other.y,
                              self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"expected Vector, got {type(other)}")
        return self + -other

    def __mul__(self, other: float):
        if not isinstance(other, float) and \
           not isinstance(other, int):
            raise ValueError(f"expected float, got {type(other)}")
        return self.__class__(self.x * other,
                              self.y * other,
                              self.z * other)

    def __truediv__(self, other: float):
        if not isinstance(other, float) and \
           not isinstance(other, int):
            raise ValueError(f"expected float, got {type(other)}")
        return self.__class__(self.x / other,
                              self.y / other,
                              self.z / other)

    def __repr__(self): return self.__str__()
    def __str__(self): return f"Vector({self.x}, {self.y}, {self.z})"