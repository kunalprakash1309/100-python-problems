# Question
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

given_list = [12,24,35,70,88,120,155]

li = [x for (i,x) in enumerate(given_list) if i%2 != 0 and i <= 6]

print(li)
