import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = {}
    total = 0
    for el in ar:
        if el in pairs:
            pairs[el]+=1
            if pairs[el]%2 == 0:
                total+=1
        else:
            pairs[el] = 1
    return total

if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = len(ar)

    result = sockMerchant(n, ar)
    print(result)

