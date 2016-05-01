__author__ = 'neilson.ramalho'


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)

    def __add__(self, other):
        return (Vector(self.a + other.a, self.b + other.b))


v1 = Vector(1, 2)
v2 = Vector(-2, 6)

print(v1 + (v2))
