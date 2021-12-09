num = int(input("Provide number: "))

def factorial(num):

    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(num))