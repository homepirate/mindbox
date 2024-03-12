import math


class Figure:
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) not in [int, float]:
            raise TypeError
        self.__radius = value

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
      self.__set_sides(side1, side2, side3)

    def __set_sides(self, *args):
        if not all(isinstance(side, (int, float)) for side in args):
            raise TypeError
        self.side1, self.side2, self.side3 = args

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        max_side = max(sides)
        sides.remove(max_side)
        return sides[0]**2 + sides[1]**2 == max_side**2
