#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        while arr[i] < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        print(" ".join([str(item) for item in arr]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
