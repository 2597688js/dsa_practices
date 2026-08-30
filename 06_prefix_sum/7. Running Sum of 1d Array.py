"""
Author : janarddan
File_name = 7. Running Sum of 1d Array.py
Date : 31/08/26
Description :

Leetcode 1480. Running Sum of 1d Array (Easy)

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

** Example 1: **

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

** Example 2: **

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

** Example 3: **

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        TC -> O(n)
        SC -> O(n)
        """
        ans = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            ans.append(curr_sum)

        return ans

    def runningSum_2(self, nums: list[int]) -> list[int]:
        """
        TC -> O(n)
        SC -> O(1)s
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1,1,1,1,1]))
    print(sol.runningSum([3,1,2,10,1]))
    print()
    print(sol.runningSum_2([1, 1, 1, 1, 1]))
    print(sol.runningSum_2([3, 1, 2, 10, 1]))

