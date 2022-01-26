# Question
# Please write a program which count and print the numbers of each character in a string input by console.

# Example: If the following string is given as input to the program:

# abcdefgabc
# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

string = input("Provide string: ")
# my_dict = {}
# for i in string:
#     if i not in my_dict.keys():
#         my_dict[i] = 0
#     my_dict[i] += 1

# print(my_dict)

for i in sorted(set(string)):
    print(f"{i}, {string.count(i)}")