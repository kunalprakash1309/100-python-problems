# Question
# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Reactangle():
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

        # one way
        # self.area = length * breadth

    def area(self):
        return self.length * self.breadth

my_rect = Reactangle(4, 5)
print(my_rect.length)
print(my_rect.area())
