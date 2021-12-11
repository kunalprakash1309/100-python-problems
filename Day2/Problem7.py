x,y = map(int, input("Provide two number seprated by comma: ").split(","))

result = []
for i in range(x):
    new_lst = []
    for j in range(y):
        value = i*j
        new_lst.append(value)
    result.append(new_lst)

print(result)