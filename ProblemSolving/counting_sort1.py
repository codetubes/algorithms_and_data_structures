#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def countingSort(arr):
    output = [0 for _ in range(0, 100)]

    for item in arr:
        output[item] += 1

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
