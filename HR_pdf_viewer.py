"""
Algorithm: Easy
Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    print(ord('a'))
    ord_a = ord('a')
    # create a dict to store the ord value as key and the heights as value
    dict_ord = {}
    for i in range(0, 26):
        new_ord = ord_a + i
        dict_ord[new_ord] = h[i]
    print(dict_ord)
    # list to store the heights of the word
    res_list = []
    for letter in word:
        if ord(letter) in dict_ord:
            res_list.append(dict_ord.get(ord(letter)))
    print(res_list)
    max_h = max(res_list)
    len_h = len(res_list)
    return max_h * len_h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
