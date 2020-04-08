#!/bin/python3
# Apple and orange

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    # The python way 
    #print(sum([ 1 for x in apples if (x + a) >= s and (x + a) <= t]))
    #print(sum([ 1 for x in oranges if (x + b) >= s and (x + b) <= t]))
    
    fall_house = 0
    for apple in apples:
        position = a + apple
        if position >= s and position <= t:
            fall_house+=1
    print (fall_house)

    fall_house = 0
    for orange in oranges:
        position = b + orange
        if position >= s and position <= t:
            fall_house+=1
    print (fall_house)


if __name__ == '__main__':

    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    
    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))  

    """ # debug
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-1, -1, -1]
    oranges  = [5, 6] """

    countApplesAndOranges(s, t, a, b, apples, oranges)
