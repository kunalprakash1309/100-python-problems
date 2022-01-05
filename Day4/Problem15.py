# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit 
# as the value of a.

# Suppose the following input is supplied to the program:

# 9
# Then, the output should be:

# 11106

digit = input()


# one of the method
# def sum(num):
#     total_sum = int(num)
#     original_num = num
#     for i in range(3):
#         num = num + original_num
#         total_sum = total_sum + int(num)
    
#     print(total_sum)
# sum(digit)

print(sum([int(digit*i) for i in range(1,5)]))