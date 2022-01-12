# Question:
# Define a function which can generate and print a tuple where the value are square of numbers 
# between 1 and 20 (both included).

def square_tuple():
     return tuple(i*i for i in range(1,21))

print(square_tuple())