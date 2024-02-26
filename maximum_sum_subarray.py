"""
Author : Janarddan Sarkar
file_name : maximum_sum_subarray.py 
date : 25-02-2024
description : Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23. subarray should be always contiguous. i.e.,
          we can not consider [5, 4, 7, 8] as a subarray whose sum is 24.

Solution 1 : using Kadane's algorithm
"""


# does not print the subarray, only return the maximum sum
def max_subarray(numbers: list):
    """Find the largest sum of any contiguous subarray.
    This function does not print the subarray that has the largest sum.
    """
    best_sum = -99999
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


# prints the subarray and the sum
def maxSubArraySum(arr):
    """Find the largest sum of any contiguous subarray.
    This function prints the subarray that has the largest sum.
    """
    size = len(arr)
    max_so_far = -9999
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return f"subarray : {arr[start:end+1]}, sum : {max_so_far}"


if __name__ == "__main__":
    print(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArraySum([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
    print(maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(maxSubArraySum([-1, -1, 10]))
    print(maxSubArraySum([5, 4, -1, 7, 8]))

    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
    print(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
