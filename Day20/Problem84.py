# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

my_list = [[[0 for i in range(3)] for i in range(4)] for i in range(5)]
print(my_list)