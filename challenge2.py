#!/bin/python3
# Compare the Triplets

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    bob, alice = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice+=1
        elif a[i] < b[i]:
            bob+=1
    return (alice,bob)

if __name__ == '__main__':
    
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print (result)