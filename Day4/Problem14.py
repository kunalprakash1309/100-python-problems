# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters 
# and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

senctence = input()
Upper_count = 0
Lower_count = 0

for word in senctence:
    if word.islower():
        Lower_count += 1

    if word.isupper():
        Upper_count += 1

print("UPPER CASE ", Upper_count)
print("LOWER CASE ", Lower_count)