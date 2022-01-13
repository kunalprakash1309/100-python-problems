# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


my_list = [1,2,3,4,5,6,7,8,9,10]

# def square(item):
#     return item * item

# new_list = list(map(square, my_list))

# another function
new_list = list(map(lambda x: x*x, my_list))
print(new_list)