# Question
# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

given_list = [12,24,35,70,88,120,155]

my_list = [x for (i, x) in enumerate(given_list) if i not in (0, 4, 5)]

print(my_list)