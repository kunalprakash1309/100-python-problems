# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)


my_list = list(map(lambda x: x * x, range(1,21)))
print(my_list)

