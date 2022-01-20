# Question
# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

my_list = [10,12,24,29,39,40,51,56,69]

def binary_search(lst, item):
    beg = 0
    end = len(lst)
    mid = int((beg + end)/2)

    while True:
        print("hello")
        print("lst[mid]== ", lst[mid])
        if lst[mid] < item:
            beg = mid
            mid = int((beg+end)/2)
            print(beg, end, mid)
        elif lst[mid] > item:
            end = mid
            mid = int((beg+end)/2)
            print(beg, end, mid)
        else :
            print("found result")
            print(beg, end, mid)
            print(lst[mid])
            return 
        
        print("final: ",beg, end)

binary_search(my_list, 56)
