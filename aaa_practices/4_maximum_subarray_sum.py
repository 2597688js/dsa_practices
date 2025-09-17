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

def maxSubArraySum_bruteforce(lst):
    """
    TC -> O(n^2)
    """
    n = len(lst)
    max_sum = lst[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += lst[j]
            # max_sum = max(curr_sum, max_sum)
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum

def maxSubArraySum_bruteforce_with_subarray(lst):
    """
    TC -> O(n^2)
    """
    n = len(lst)
    max_sum = lst[0]
    best_start_idx, best_end_idx = 0, 0

    for i in range(n):
        curr_sum = 0   # Track current sum for every element
        for j in range(i, n):
            curr_sum += lst[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_start_idx, best_end_idx = i, j

    return max_sum, lst[best_start_idx: best_end_idx + 1]

def maxSubArraySum_kadane(lst):
    """
    TC -> O(n)
    """
    n = len(lst)
    max_sum = lst[0]   # best sum overall
    curr_sum = lst[0]  # best sum ending at current position

    for i in range(1, n):
        if curr_sum < 0:
            curr_sum = lst[i]
        else:
            curr_sum += lst[i]

        max_sum = max(max_sum, curr_sum)

    return max_sum

def maxSubArraySum_kadane_with_subarray(lst):
    """
    TC -> O(n)
    """
    n = len(lst)
    max_sum = lst[0]   # best sum overall
    curr_sum = lst[0]  # best sum ending at current position

    start_idx = 0    # potential start of the current subarray
    best_start_idx, best_end_idx = 0, 0

    for i in range(1, n):
        if curr_sum < 0:
            curr_sum = lst[i]
            start_idx = i
        else:
            curr_sum += lst[i]   # let the curr_sum keep going

        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start_idx, best_end_idx = start_idx, i

    return max_sum, lst[best_start_idx:best_end_idx + 1]

if __name__ == "__main__":
    print(maxSubArraySum_bruteforce([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArraySum_bruteforce([5, 4, -1, 7, 8]))
    print(maxSubArraySum_bruteforce([-5, -4, -1, -7, -8]))

    print(maxSubArraySum_bruteforce_with_subarray([-5, -4, -1, -7, -8]))
    print(maxSubArraySum_bruteforce_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("----- kadane's algo -------")
    print(maxSubArraySum_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArraySum_kadane([-2, -1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArraySum_kadane_with_subarray([5, 4, -1, 7, 8]))
    print(maxSubArraySum_kadane_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
