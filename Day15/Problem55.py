# Question
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.
# Then, the output of the program should be:

# ['2', '3']

lst = input("Provide sequence word separated by whitespace: ").split()
final_list = [word for word in lst if word.isnumeric()]

# for word in lst:
#     if word.isnumeric():
#         final_list.append(word)

print(final_list)