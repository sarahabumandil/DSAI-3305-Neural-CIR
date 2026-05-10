"""
Copyright 2022, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Hannah Bast <bast@cs.uni-freiburg.de>
"""

import sys
import random
import time
import math


def intersect_1(A, B):
    """
    Intersect A and B using a straightforward implementation of the basic zipper
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
    Variant with less ifs (and more elifs).

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
    Variant with while loops to benefit from the case, where we can skip larger
    segments in one list.

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
    Avoid repeated evaluation of len(A) and len(B), which don't change.

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
    Avoid repeated check whether we are at the end of one of the lists by adding
    a "sentinel" (infinity in this case) at the end of both lists.

    >>> intersect_5([1, 3, 5, 11], [2, 4, 5, 8, 11, 17])
    [5, 11]
    """

    R = []
    i = 0
    j = 0
    n = len(A)
    m = len(B)
    A.append(math.inf)
    B.append(math.inf)
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
    # Parse command line arguments.
    if len(sys.argv) != 4:
        print("Usage: python3 intersect_timing.py <n1> <n2> <k>")
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    k = int(sys.argv[3])
    random.seed(123456789)
    list1 = sorted(random.sample(range(n1 + n2), n1))
    list2 = sorted(random.sample(range(n1 + n2), n2))
    function_call = "intersect_%d(list1, list2)" % k
    for run in range(3):
        print("Intersecting two lists of sizes %d and %d ... " % (n1, n2),
                end="")
        start_time = time.monotonic()
        result = eval(function_call)
        end_time = time.monotonic()
        print("%d ms, result size = "
              % ((end_time - start_time) * 1000), len(result))
