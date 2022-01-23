# Question
# Please write a program to print the running time of execution of "1+1" for 100 times.

import time

t1 = time.time()*1000

for i in range(100000):
    x = 1 + 1

t2 = time.time()*1000

print(f"Total time taken {t2-t1}ms")
