"""
easy
link:  https://www.hackerrank.com/challenges/staircase/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code her
    i = 1
    while i <= n:
        space = " " * (n-i)
        star = '#' * i
        print(f'{space}{star}')
        i += 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
