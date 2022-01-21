# Question
# Please write a program to output a random even number between 0 and 10 inclusive 
# using random module and list comprehension.

import random
# def generate_even():
#     item = random.randint(0,100)
#     if item % 2 == 0:
#         return item
#     else:
#         return 0

resp = [i for i in range(0, 101, 2)]

print(random.choice(resp))