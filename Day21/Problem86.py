# Question
# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

given_list = [12,24,35,24,88,120,155]

while 24 in given_list:
    given_list.remove(24)

print(given_list)