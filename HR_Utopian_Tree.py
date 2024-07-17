"""
Implementation Algorithm: Easy
Link: https://www.hackerrank.com/challenges/utopian-tree/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    if n == 0:  # base case
        return 1
    elif n == 1:
        return 2
    print(n)
    prev = 1  # initialize with 1 height
    for cycle in range(1, n+1):
        print(cycle, prev)
        if (cycle % 2 == 0):  # even case
            prev = prev + 1
        elif (cycle % 2 == 1):
            prev = prev * 2
        print(prev)
    return prev

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

