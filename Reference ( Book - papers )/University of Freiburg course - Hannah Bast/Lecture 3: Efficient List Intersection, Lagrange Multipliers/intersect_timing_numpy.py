"""
Copyright 2022, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Hannah Bast <bast@cs.uni-freiburg.de>
"""

import sys
import random
import time
import math
import numpy

def intersect_1(A, B):
    """
    Intersect A and B using a straighforward implementation of the basic zipper
    algorithm.

    >>> intersect_1([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        if i == len(A):
            break
        if B[j] < A[i]:
            j += 1
        if j == len(B):
            break
        if A[i] == B[j]:
            R.append(A[i])
            i += 1
            j += 1
    return R


def intersect_2(A, B):
    """
    Intersect A and B using a straighforward implementation of the basic zipper
    algorithm.

    >>> intersect_2([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            R.append(A[i])
            i += 1
            j += 1
    return R


def intersect_3(A, B):
    """
    Intersect A and B using a straighforward implementation of the basic zipper
    algorithm.

    >>> intersect_3([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        while i < len(A) and A[i] < B[j]:
            i += 1
        if i == len(A):
            break
        while j < len(B) and B[j] < A[i]:
            j += 1
        if j == len(B):
            break
        if A[i] == B[j]:
            R.append(A[i])
            i += 1
            j += 1
    return R


def intersect_4(A, B):
    """
    Intersect A and B using a straighforward implementation of the basic zipper
    algorithm.

    >>> intersect_4([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    i = 0
    j = 0
    n = len(A)
    m = len(B)
    while i < n and j < m:
        while i < n and A[i] < B[j]:
            i += 1
        if i == n:
            break
        while j < m and B[j] < A[i]:
            j += 1
        if j == m:
            break
        if A[i] == B[j]:
            R.append(A[i])
            i += 1
            j += 1
    return R


def intersect_5(A, B):
    """
    Intersect A and B using a straighforward implementation of the basic zipper
    algorithm.

    >>> intersect_5([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    n = len(A)
    m = len(B)
    A.append(math.inf)
    B.append(math.inf)
    i = 0
    j = 0
    while i < n and j < m:
        while A[i] < B[j]:
            i += 1
        if i == n:
            break
        while B[j] < A[i]:
            j += 1
        if j == m:
            break
        if A[i] == B[j]:
            R.append(A[i])
            i += 1
            j += 1
    A.pop()
    B.pop()
    return R

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 intersect_timing.py <n1> <n2> <k>")
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    k = int(sys.argv[3])
    random.seed(123456789)
    list1 = numpy.array(sorted(random.sample(range(n1 + n2), n1)))
    list2 = numpy.array(sorted(random.sample(range(n1 + n2), n2)))
    # list1 = numpy.array(sorted(random.sample(range(n1 + n2), n1)), dtype=int)
    # list2 = numpy.array(sorted(random.sample(range(n1 + n2), n2)), dtype=int)

    function_call = "intersect_%d(list1, list2)" % k
    for run in range(3):
        print("Intersecting two lists of sizes %d and %d ... " % (n1, n2),
                end="")
        start_time = time.monotonic()
        eval(function_call)
        end_time = time.monotonic()
        print("%d ms" % ((end_time - start_time) * 1000))
        # print("%d µs" % ((end_time - start_time) * 1000000))
