values = input("Provide strings serarated with comma: ").split(",")

values.sort()
print(",".join(values))

# def my_func(e):
#     print(e)
#     return e[0]  #key - function that serves as a key for the sort comparison

# my_list = input('Enter a comma separated string: ').split(",")
# my_list.sort(key=my_func)
# print(",".join(my_list))