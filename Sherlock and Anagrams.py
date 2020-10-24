#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
# Complete the sherlockAndAnagrams function below.

def sherlockAndAnagrams(s):
    sLen = len(s)
    res = 0
    anagrams = []
    for i in range(0, sLen//2):
        for j in range(0, sLen - i):
            anagrams.extend(list(itertools.permutations(s[j:j+i])))

    for a in anagrams:
        print(a)
        print("".join(a))
    return res

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)