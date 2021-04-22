import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    total_count = 0

    for ch in s:
        if ch == "a":
            total_count += 1

    total_count *= n // len(s)
    pending = n % len(s)
    for ch in s[:pending]:
        if ch == "a":
            total_count += 1
    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
