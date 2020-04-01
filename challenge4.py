#!/bin/python
# Plus Minus

from __future__ import print_function

import os
import sys


#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    positive,negative,zeroes = 0,0,0
    for i in arr:
        if i < 0:
            negative+=1
        elif i > 0:
            positive+=1
        else:
            zeroes+=1
    
    return (positive / len(arr), negative / len(arr), zeroes / len(arr))

if __name__ == '__main__':
    # n = int(input())

    arr = list(map(int, input().rstrip().split()))

    responses = plusMinus(arr)

    for response in responses:
        print ("%.6f" % response)