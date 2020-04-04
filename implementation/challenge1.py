#!/bin/python3
# Grading Students



import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here

    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            r = 5 - grade % 5
            if r < 3:
                new_grades.append(grade + r )
            else:
                new_grades.append(grade)
    return new_grades
    


if __name__ == '__main__':

    # grades_count = int(input().strip())

    # grades = []

    # for _ in range(grades_count):
    #    grades_item = int(input().strip())
    #    grades.append(grades_item)

    grades = [ 73,67,38,33 ]

    result = gradingStudents(grades)

    print (result)
