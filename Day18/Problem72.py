# Question
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random
# my_list = []

# while len(my_list) < 5:
#     num = random.randint(100, 200)
#     if num not in my_list:
#         my_list.append(num)
my_list = random.sample(range(100, 201), 5)

print(my_list)
