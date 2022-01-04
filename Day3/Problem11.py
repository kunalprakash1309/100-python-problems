# Question
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether 
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:

# 0100,0011,1010,1001
# Then the output should be:

# 1010

new_list = []

def check(num):
    return int(num,2)%5 == 0

numbers = input("Enter 4 digit binary numbers as a comma separated sequence: ").split(",")

# for i in range(len(numbers)):
#     if check(numbers[i]):
#         new_list.append(numbers[i])

new_list = list(filter(check,numbers))


print(new_list)
