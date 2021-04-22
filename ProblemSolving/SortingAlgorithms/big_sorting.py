#!/bin/python3

import math
import os
import random
import re
import sys


# merge sort
def merge_sort(array1, array2):
    i, j, = 0, 0,
    result = []

    while i < len(array1) and j < len(array2):
        if (len(array1[i]) < len(array2[j])):
            result.append(array1[i])
            i += 1
        elif (len(array2[j]) < len(array1[i])):
            result.append(array2[j])
            j += 1
        elif array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    while i < len(array1):
        result.append(array1[i])
        i += 1

    while j < len(array2):
        result.append(array2[j])
        j += 1

    return result


# Devide
def devide(data):
    if len(data) < 2:
        return data
    else:
        middle = len(data) // 2
        left_array = devide(data[:middle])
        right_array = devide(data[middle:])
        return merge_sort(left_array, right_array)


# Complete the bigSorting function below.
def bigSorting(unsorted):
    # Merge Sort
    return devide(unsorted)

    '''Bubble Sort
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(unsorted)-1):
            if int(unsorted[i]) > int(unsorted[i+1]):
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
                swapped=True
    return unsorted

    #Insertion Sort
    for i in range(1, len(unsorted)):
        while int(unsorted[i]) < int(unsorted[i-1]) and i > 0:
            unsorted[i], unsorted[i-1] = unsorted[i-1], unsorted[i]
            i-=1
    return unsorted

    #Quick Sort
    if len(unsorted)<2:
        return unsorted
    else:
        smaller, larger = [],[]
        pivot = unsorted.pop()
        for item in unsorted:
            if int(item) > int(pivot):
                larger.append(item)
            else:
                smaller.append(item)

        return bigSorting(smaller) + [pivot]+bigSorting(larger)
    '''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
