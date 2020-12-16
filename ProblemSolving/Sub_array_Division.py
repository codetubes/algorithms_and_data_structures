#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    for i in range(0, len(s)):

        j = 0
        check = 0
        while j < m and (i + j) < len(s):
            check += s[i + j]
            j += 1
        if check == d:
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
