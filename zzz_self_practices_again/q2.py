"""
Author : Janarddan Sarkar
file_name : q2.py 
date : 16-06-2023
description : Largest Sum Contiguous Subarray (Kadane’s Algorithm).
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[]
with the largest sum.
Ex : a = [-2, -3, 4, -1, -2, 1, 5, -3], ans is [4, -1, -2, 1, 5] because 4 + (-1) + (-2) + 1 + 5 = 7 (max), take any
contiguous array, sum will be less that this.
"""
from sys import maxsize


def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start_index = 0
    end_index = 0

    for i in range(size):
        max_ending_here += a[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            end_index = i

        if max_ending_here < 0:
            max_ending_here = 0
            start_index = i + 1

    print("Maximum contiguous sum is:", max_so_far)
    print("Maximum contiguous subarray is:", a[start_index:end_index+1])


# a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [-2, -3, -1, -1, -2, -1, -5, -3]
# a = [1, 1, 1, 2, 4, 5]
maxSubArraySum(a, len(a))


