"""
Author : Janarddan Sarkar
file_name : 2.longest_increasing_subsequence_(LIS).py 
date : 28-11-2024
description :
The Longest Increasing Subsequence (LIS) problem involves finding the length (or the subsequence itself) of the longest
subsequence in a sequence of numbers such that all elements of the subsequence are sorted in increasing order.
The subsequence does not have to be contiguous.

Example
Input:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

Output:
LIS = [10, 22, 33, 50, 60, 80] (Length = 6)
"""


def lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    return max(dp)


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]   # [10, 22, 33, 41, 60, 80]
    # arr = [3, 10, 2, 1, 20]    # Output: 3 - [3, 10, 20]
    print("Length of LIS is", lis(arr))

