# Question
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 3.55

n = int(input("Provide the value of n: "))
sum = 0

for i in range(1, n+1):
    sum = sum + (i/(i+1))

#print(round(sum(map(lambda x: x/(x+1), range(1, n+1))), 2))

print(sum)