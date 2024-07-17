"""
easy
Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #if we sort the array then obviously first 4 will give least sum and last 4 will give max sum
    arr.sort()
    size = len(arr)
    MinSum, MaxSum = 0, 0 # given all positive integers
    l = 0
    r = size-1
    while l <4:
        MinSum += arr[l]
        MaxSum += arr[r]
        l += 1
        r -= 1
    print(MinSum,MaxSum,sep=' ')



if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
