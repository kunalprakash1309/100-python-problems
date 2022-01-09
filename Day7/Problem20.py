# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, 
# between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14


class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7)+ 1):
            yield i*7

num = int(input("Please enter value of n: "))

for i in MyGen().by_seven(num):
    print(i)

