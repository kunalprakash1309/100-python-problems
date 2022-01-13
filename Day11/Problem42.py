# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

my_list = [1,2,3,4,5,6,7,8,9,10]

# even_list = list(filter(lambda i: i % 2 == 0, my_list))

# output_list = list(map(lambda x: x*x, even_list))

output_list = list(map(lambda i: i*i, filter(lambda item: item % 2 == 0, my_list)))

print(output_list)