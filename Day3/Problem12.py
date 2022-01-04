# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.The numbers obtained should be printed 
# in a comma-separated sequence on a single line.


# another method to do 
# def check_even(num):
#     for i in str(num):
#         if int(i)%2 != 0:
#             return False
#     return True
    
#     return(all())

def check_even(num):
    new_lst = [int(i)%2 == 0 for i in num]
    return all(new_lst)


numbers = [str(i) for i in range(1000, 3001)]

numbers = list(filter(check_even, numbers))
print(numbers)

