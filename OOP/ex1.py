import math


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, age):
        super().__init__(name, max_speed, mileage)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


p1 = Point(2, 3)
p2 = Point(3, 3)
print(p1.show())
print(p2.show())
p1.move(10, -10)
print(p1.show())
print(p1.dist(p2))
