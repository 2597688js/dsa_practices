"""
Author : Janarddan Sarkar
file_name : 4_maximum_subarray_sum.py
date : 14-09-2025
description :
Kadane's Algorithm (Maximum Subarray Sum)

Problem:
--------
Given an integer array 'nums', find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Example 1:
----------
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

Example 2:
----------
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum = 23.

Approach (Kadane's Algorithm):
------------------------------
1. Initialize:
   - max_sum = first element of nums
   - current_sum = 0
2. Traverse through each element:
   - Add current element to current_sum.
   - Update max_sum = max(max_sum, current_sum).
   - If current_sum < 0 → reset current_sum = 0
     (since negative sums reduce the future subarray total).
3. Return max_sum as the result.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# def maxSubArraySum_bruteforce(lst):
#     for item in lst