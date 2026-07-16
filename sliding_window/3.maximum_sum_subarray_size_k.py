"""
Author : janarddan
File_name = 3.maximum_sum_subarray_size_k.py
Date : 16/07/26
Description :
1. Maximum Sum Subarray of Size K (Easy) ⭐⭐⭐⭐⭐

Problem:
Given an array of integers and an integer k, find the maximum sum of any contiguous subarray of size k.

Example:

nums = [2,1,5,1,3,2]
k = 3

Output = 9

Explanation:
[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9  ← Maximum
[1,3,2] = 6

"""

num = [-2,-1,-5,-1,-3,-2]
k = 3


left = 0
maxi = float('-inf')
curr_sum = 0
for right in range(len(num)):
    curr_sum += num[right]
    window_len = right - left + 1
    if window_len == k:
        maxi = max(maxi, curr_sum)
        curr_sum -= num[left]
        left += 1


print(maxi)

