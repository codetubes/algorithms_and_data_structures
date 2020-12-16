#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    steps = 0
    for i in range(1,len(arr)):
        while arr[i]<arr[i-1] and i > 0:
            steps+=1
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
