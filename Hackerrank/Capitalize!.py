#https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    res=''
    primera=True
    for x in range(len(s)):
        if s[x]==" ":
            res=res+" "
            primera=True
        elif primera:
            res=res+s[x].upper()
            primera=False
        else:
            res=res+s[x]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
