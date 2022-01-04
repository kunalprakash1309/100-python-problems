# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3

no_of_letter = 0
no_of_digit = 0

sentence = input()
for i in sentence:
    if i.isalpha():
        no_of_letter += 1
    elif i.isnumeric():
        no_of_digit += 1

print("LETTERS: ", no_of_letter)
print("DIGITS: ", no_of_digit)