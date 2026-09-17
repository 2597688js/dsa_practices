"""
Author : janarddan
File_name = 8.Minimum Size Subarray Sum.py
Date : 17/09/26
Description :
Leetcode 209. Minimum Size Subarray Sum (Medium)

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


** Example 1: **

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

** Example 2: **

Input: target = 4, nums = [1,4,4]
Output: 1

** Example 3: **

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""


class Solution:
    def minSubArrayLen_brute(self, target: int, nums: list[int]) -> int:
        """
        TC -> O(n**2)
        SC -> O(1)
        """
        n = len(nums)

        min_len = float("inf")

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    # break

        return 0 if min_len == float("inf") else min_len

    def minSubArrayLen_optimal(self, target: int, nums: list[int]) -> int:
        """
        TC -> O(n)
        SC -> O(1)
        """
        n = len(nums)

        curr_sum = 0
        left = 0
        min_len = float("inf")

        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1


        return 0 if min_len == float("inf") else min_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen_brute(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen_brute(4, [1, 4, 4]))
    print(sol.minSubArrayLen_brute(11, [1,1,1,1,1,1,1,1]))
    print()
    print(sol.minSubArrayLen_optimal(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen_optimal(4, [1, 4, 4]))
    print(sol.minSubArrayLen_optimal(11, [1, 1, 1, 1, 1, 1, 1, 1]))

