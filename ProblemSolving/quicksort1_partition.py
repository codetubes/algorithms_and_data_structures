#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    smaller, larger, equal = [], [], []
    for item in arr:
        if item > pivot:
            larger.append(item)
        elif item < pivot:
            smaller.append(item)
        else:
            equal.append(item)
    result = smaller + equal + larger
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
