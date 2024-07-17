"""
easy
link:https://www.hackerrank.com/challenges/plus-minus/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    size = len(arr)
    for i in arr:
        if i == 0:
            zer += 1
        elif i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    print(round(pos/size, 6))
    print(round(neg/size, 6))
    print(round(zer/size, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
