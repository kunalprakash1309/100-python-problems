# Question
# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

heads = 35
legs = 94

no_of_rabbits = 0
no_of_hens = 0
for i in range(heads+1):
    j = heads - i
    if i * 4 + j * 2 == legs:
        no_of_rabbits = i
        no_of_hens = j

print(no_of_rabbits, no_of_rabbits)

    