# Question:
# Write a program to generate and print another tuple whose values are even numbers 
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

my_tuple = (1,2,3,4,5,6,7,8,9,10)
my_list = []

# one method
# for i in my_tuple:
#     if i%2 == 0:
#         my_list.append(i)
# print(tuple(my_list))

# one of the method
# tpl = tuple(i for i in my_tuple if i%2 == 0)
# print(tpl)

tpl = tuple(filter(lambda x: x%2 == 0, my_tuple))
print(tpl)


