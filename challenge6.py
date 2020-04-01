#!/bin/python3
# Mini-Max Sum

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # Learned in hackerrank discussion pretty good
    # x = sum(arr)
    # print (x-(max(arr)), (x-(min(arr))))

    # My old rusty code
    max = 0
    min = sum(arr)
    for i in range(len(arr)):
        temp=arr.copy()
        temp.pop(i)
        r = sum(temp)
        if r > max:
            max = r
        if r < min:
            min = r
    print (min, max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    # Debug
    # arr=[1, 2, 3, 4, 5]

    miniMaxSum(arr)
