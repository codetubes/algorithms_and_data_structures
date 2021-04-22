#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSort function below.
def countSort(arr):
    output = [[] for _ in range(0, len(arr))]

    for i in range(0, len(arr) // 2):
        arr[i][1] = "-"

    for item in arr:
        output[int(item[0])].append(item[1])

    stringOutput = ""
    for item in output:
        for element in item:
            if element:
                stringOutput += element + " "

    print(stringOutput)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
