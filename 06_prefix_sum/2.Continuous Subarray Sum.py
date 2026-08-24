"""
Author : janarddan
File_name = 2.Continuous Subarray Sum.py
Date : 22/08/26
Description : Leetcode 523

Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:
- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k.

Note that:
- A subarray is a contiguous part of the array.
- An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


** Example 1: **

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

** Example 2: **

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

** Example 3: **

Input: nums = [23,2,6,4,7], k = 13
Output: false

"""

class Solution:
    def checkSubarraySumBruteforce(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            curr_sum = nums[i]
            for j in range(i+1, n):
                curr_sum = curr_sum + nums[j]
                if curr_sum % k ==0:
                    return True


        return False

    def checkSubarraySumOptimal(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        prefix_hashmap = {0:-1}  # store remainder (while divided by k) : index

        curr_sum = 0

        for idx, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k
            if remainder in prefix_hashmap:
                if (idx - prefix_hashmap[remainder]) >=2:
                    return True
            else:
                prefix_hashmap[remainder] = idx

        return False



if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySumBruteforce([23,2,4,6,7], k = 6))
    print(sol.checkSubarraySumOptimal([23,2,6,4,7], k = 6))
    print(sol.checkSubarraySumOptimal([4,1,9], k = 4))
    print(sol.checkSubarraySumOptimal([1,2,3], k = 6))
