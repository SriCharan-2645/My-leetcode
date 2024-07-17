#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    #print(queries)
    res = []
    for query in queries:
        problem = query[0]
        x = query[1]
        y = query[2]
        if problem == 1:
            ind = ((x ^ lastAnswer) % n)
            arr[ind].append(y)
        elif problem == 2:
            ind = ((x ^ lastAnswer) % n)
            inner_ind = y % len(arr[ind])
            lastAnswer = arr[ind][inner_ind]
            res.append(lastAnswer)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
