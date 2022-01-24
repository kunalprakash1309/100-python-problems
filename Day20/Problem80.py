# Question
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

given_list = [5,6,77,45,22,12,24]

my_list = list(filter(lambda x : x % 2 != 0, given_list))

print(my_list)
