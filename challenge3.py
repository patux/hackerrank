#!/bin/python3
# Diagonal Difference

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary,secondary = [],[]

    for i,row in enumerate(arr):
        primary.append(row[i])
        secondary.append(row[-i-1])

    return abs((sum(primary) - sum(secondary)))

if __name__ == '__main__':
    
    n = int(input().strip())
    
    # debug
    arr = [ 
        [36, 25, 39, 79],
        [36, 24, 20, 93],
        [36, 33, 66, 98],
        [33, 23, 2, 19],
    ]
    
    arr = [] 
    for _ in range(n):
       arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print (result)


