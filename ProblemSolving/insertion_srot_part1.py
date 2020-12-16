#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    for i in range(1, n):
        while arr[i] < arr[i - 1] and i > 0:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            print(" ".join([str(elem) for elem in arr]))
            arr[i - 1] = tmp
            i -= 1
    print(" ".join([str(elem) for elem in arr]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
