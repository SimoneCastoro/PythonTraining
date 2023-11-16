"""
Session I: Cheat Sheet
"""
import math

# Creating Python Classes
# may check PEP8 for style guidance!


class MyFirstClass:
    pass


a = MyFirstClass()
b = MyFirstClass()


# Adding Attributes
# "dot-notation
# <object>.<attribute> = <value>
class Point:
    pass


p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)


# Making it do something
# here def stand for "method", like for a function... (dont be confused)
class Point:
    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
print(p.x, p.y)

# Talking to yourself
# ATENZIONE: methods have only one argument. It is very common !!! to use the name "self"
# method = a function attached to a class
# no input required (), because python automatically knows the p is the input ;)

# Alternatively (two the code right above)
p = Point()
Point.reset(p)
print(p.x, p.y)

# More arguments


class Point:
    def __init__(self):
        self.y = None

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)


def calculate_distance(self, other_position):
    return math.sqrt(
        (self.x - other_position.x) ** 2
        + (self.y - other_position.y) ** 2
    )


point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)

dist = calculate_distance(point1, point2)
print(dist)
