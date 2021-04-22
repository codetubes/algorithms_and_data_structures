#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    smallest = 99999999999999
    pairs = []

    arr.sort()
    for i in range(1, len(arr)):
        difference = abs(arr[i - 1] - arr[i])
        if difference < smallest:
            smallest = difference
            pairs = [arr[i - 1], arr[i]]
        elif difference == smallest:
            pairs.extend([arr[i - 1], arr[i]])

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
