#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # create an empty set
    result = set()

    for factor in range(a[-1], b[0] + 1):
        for num in a:
            if factor % num != 0:
                break
        # if inner loop completes without encountering the break statement
        # then the following else block will be executed
        else:
            for num in b:
                if num % factor != 0:
                    break
            else:
                result.add(factor)
            continue

    return len(result)


if __name__ == "__main__":
    total = getTotalX([2, 4], [16, 32, 96])

    print(total)
