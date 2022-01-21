# Question
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random

resp = random.sample([i for i in range(10, 1001) if i % 35 == 0], 5)

print(resp)