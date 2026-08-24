"""
Author : janarddan
File_name = 3. contiguous subarray with equal no of 0s and 1s.py
Date : 24/08/26
Description :

Leetcode 525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

** Example 1: **

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

** Example 2: **

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

** Example 3: **

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

"""


class Solution:
    def findMaxLengthOptimal(self, nums: list[int]) -> int:

        for idx, num in enumerate(nums):
            if nums[idx] == 0:
                nums[idx] = -1

        prefix_d = {0:-1}  # Sum : idx

        max_len = 0

        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum in prefix_d:
                curr_len = i - prefix_d[curr_sum]
                max_len = max(max_len, curr_len)
            else:
                prefix_d[curr_sum] = i

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLengthOptimal([0,0,0,0,1,1]))
    print(sol.findMaxLengthOptimal([0,1,1,1,1,1,0,0,0]))
    print(sol.findMaxLengthOptimal([0,1]))
    print(sol.findMaxLengthOptimal([0,1,0]))
    print(sol.findMaxLengthOptimal([0,1,0,1]))

