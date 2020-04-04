#!/bin/python3
# BirthdayCakeCandles

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    m = max(ar)
    return ar.count(m)

if __name__ == '__main__':
    
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    # Debug
    # ar = [1, 5, 3, 4, 5, ]

    result = birthdayCakeCandles(ar)

    print (result)

