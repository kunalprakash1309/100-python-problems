# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20
# (both included). Then the function needs to print the last 5 elements in the list.

my_list = [i*i for i in range(1, 21)]
length = len(my_list)

print(my_list[-5:])

# for i in range(1,6):
#     print(my_list[length-i])