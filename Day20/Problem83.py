# By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

given_list = [12,24,35,70,88,120,155]

my_list = [i for (x, i) in enumerate(given_list) if x < 3 or x > 4]
print(my_list)