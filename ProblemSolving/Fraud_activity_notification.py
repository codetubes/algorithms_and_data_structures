#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


def findMedian(counter, d):
    count = 0
    median = 0

    if d % 2 != 0:
        for i in range(len(counter)):
            count += counter[i]

            if count > d // 2:
                median = i
                break

    else:
        first = 0
        second = 0

        for i, _ in enumerate(counter):
            count += counter[i]

            if first == 0 and count >= d // 2:
                first = i

            if second == 0 and count >= d // 2 + 1:
                second = i
                break

        median = (first + second) / 2

    return median


def activityNotifications(expenditure, d):
    count = 0
    counter = [0] * 201

    for exp in range(d):
        counter[expenditure[exp]] += 1

    for i in range(d, len(expenditure)):

        median = findMedian(counter, d)

        if expenditure[i] >= 2 * median:
            count += 1

        counter[expenditure[i - d]] -= 1
        counter[expenditure[i]] += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
