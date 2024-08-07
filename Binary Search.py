# Comparison of Binary Search and Linear Search time 

import random
import time 

def Linear_Search(l, target):
    for x in range(len(l)):
        if l[x] == target:
            return x
        return -1
    
def Binary_Search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1
    
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < midpoint:
        return Binary_Search(l, target, low, midpoint-1)
    else:
        return Binary_Search(l, target, midpoint+1, high)
    
if __name__ == '__main__':
    
    length = 20000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        Linear_Search(sorted_list, target)
    end = time.time()
    print("Linear search time: ", (end - start)/length, "seconds.")

    start = time.time()
    for target in sorted_list:
        Binary_Search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds.")