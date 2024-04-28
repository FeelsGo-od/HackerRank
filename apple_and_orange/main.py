#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_amount = 0
    oranges_amount = 0
    
    for d in apples:
        if s <= d + a <= t:
            apples_amount += 1
            
    for d in oranges:
        if s <= b + d <= t:
            oranges_amount += 1
            
    print(f'{apples_amount}\n{oranges_amount}')

if __name__ == '__main__':
    countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
