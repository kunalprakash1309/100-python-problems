# Question
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

given_list = [12,24,35,24,88,120,155,88,120,155]

lst = list(set(given_list))
print(lst)

sorted_list = sorted(lst)
print(sorted_list)
