
import math

values = input("Enter number separated by comma: ")
lst = values.split(",")

result = [str(round(math.sqrt((2*50*int(i))/30))) for i in lst]

print(",".join(result))

