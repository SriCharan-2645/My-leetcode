"""
Implementation Algorithms: Easy
Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#  No return, print answer

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    #print(s, t, a, b, apples, oranges)
    res_apple = 0
    res_orange = 0
    for i in apples:
        if i + a >= s and i + a <= t:
            res_apple += 1
    for i in oranges:
        if i + b <= t and i + b >= s:
            res_orange += 1
    print(res_apple,res_orange,sep='\n')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
