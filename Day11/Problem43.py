# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# my_list = list(filter(lambda item: item % 2 == 0, [i for i in range(1,21)]))

# another method
my_list = list(filter(lambda item: item % 2 == 0, range(1,21)))

print(my_list)