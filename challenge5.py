#!/bin/python3
# Staircase

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    s='#'
    for i in range(n):
        print (s.rjust(n,' '))
        s+="#"


if __name__ == '__main__':
    n = int(input())

    staircase(n)
