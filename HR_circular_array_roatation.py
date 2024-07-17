"""
Implementation Algorithms: Easy
Link: https://www.hackerrank.com/challenges/circular-array-rotation/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    pivot = k % len(a)  # because array of size 5 made 5 rotations is equal to 0 rotations
    new_arr = a[-pivot:] + a[:-pivot]
    res = []
    for i in queries:
        res.append(new_arr[i])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
