"""
Author : Janarddan Sarkar
file_name : 21.two_sum_problem.py 
date : 27-11-2024
description :
1. Two Sum
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the value and its index
        index_map = {}

        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in index_map:
                # If found, return the indices
                return [index_map[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            index_map[num] = i


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1]


