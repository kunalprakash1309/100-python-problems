# Define a class, which have a class parameter and have a same instance parameter.

class Car:

    def __init__(self, name=None):
        self.name = name

honda = Car("Honda")

print(honda)
print(honda.name)