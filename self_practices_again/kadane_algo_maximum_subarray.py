"""
Author : Janarddan Sarkar
File_name = kadane_algo_maximum_subarray.py
Date : 26-02-2024
Description :  
"""


def maxSumSubarray(arr):
    n = len(arr)

    max_sum = -99999
    max_so_far = 0

    start, end = 0, 0

    for x in arr:
        max_so_far += x

        if max_so_far > max_sum:
            max_sum = max_so_far

        if max_so_far < 0:
            max_so_far = 0

    return max_sum


if __name__ == "__main__":
    print(maxSumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSumSubarray([-2, -1, -3, -4, -5]))
