# Question
# Define a class named Circle which can be constructed by a radius. 
# The Circle class has a method which can compute the area.

class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

my_circle = Circle()
print(my_circle.radius)
print(my_circle.area())

    