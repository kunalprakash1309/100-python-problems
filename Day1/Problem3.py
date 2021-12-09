num = int(input("Provide number: "))

# def print_dict(num):
#     data = dict()
#     for i in range(num+1):
#         data[i] = i*i
#     return data

# print(print_dict(num))

data = {i: i*i for i in range(num) }
print(data)
