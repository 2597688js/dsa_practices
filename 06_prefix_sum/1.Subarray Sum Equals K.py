"""
Author : janarddan
File_name = 1.Subarray Sum Equals K.py
Date : 22/08/26
Description : Leetcode 560
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

TC -> O(n)
SC -> O(1)

"""

def subarraySum(arr, target):
    n = len(arr)

    count = 0

    prefixSum : dict[int, int] = {0:1}

    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        remaining = curr_sum - target
        if remaining in prefixSum:
            count += prefixSum.get(remaining)

        prefixSum[curr_sum] = prefixSum.get(curr_sum, 0) + 1

    return count


if __name__ == "__main__":
    print(subarraySum([1,1,1], 3))
    print(subarraySum([1,2,3], 3))
    print(subarraySum([2,3,-5,5,-5,1,4], 5))