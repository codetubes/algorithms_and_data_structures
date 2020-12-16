#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the introTutorial function below.
def introTutorial(V, arr):
    i = 0
    for item in arr:
        if item == V:
            return i
        i += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
