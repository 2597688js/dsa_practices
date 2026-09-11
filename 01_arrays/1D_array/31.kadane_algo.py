"""
Author : janarddan
File_name = 31.kadane_algo.py
Date : 12/09/26
Description :

Kadane's Algorithm

You are given an integer array arr[]. You need to find the maximum sum of a subarray
(containing at least one element) in the array arr[].

** Examples: **

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

"""

def kadane_algo(arr):
    n = len(arr)

    maxi = float("-inf")
    curr_sum = 0

    for num in arr:
        curr_sum += num
        maxi = max(curr_sum, maxi)

        if curr_sum < 0:
            curr_sum = 0

    return maxi

print(kadane_algo([5, 4, 1, 7, 8]))
print(kadane_algo([2, 3, -8, 7, -1, 2, 3]))
print(kadane_algo([-2, -4]))
