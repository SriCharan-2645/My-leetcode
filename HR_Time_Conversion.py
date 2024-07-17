"""
Easy
Link:https://www.hackerrank.com/challenges/time-conversion/problem?
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_unit = s[-2:]
    # extract time
    onlyTime = s[:-2]
    hh, mm, ss = onlyTime.split(':')
    h = ''
    if time_unit == 'PM' and hh != '12':
        h = '12'
        newHH = str(int(h) + int(hh))
    elif time_unit == 'AM' and hh == '12':
        newHH = '00'
    else:
        h = '00'
        newHH = int(h) + int(hh)
        if newHH < 10:
            newHH = f'{newHH:02d}'
        else:
            newHH = str(newHH)

    newTime = newHH+':'+mm+':'+ss
    return newTime






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
