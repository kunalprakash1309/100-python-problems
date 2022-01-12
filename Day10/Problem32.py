# Question:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
# (both included) and the values are square of keys. The function should just print the keys only.

my_dict = {i: i*i for i in range(1, 21)}

for i, _ in my_dict.items():
    print(i)

# for i in my_dict.keys():
#     print(i)
