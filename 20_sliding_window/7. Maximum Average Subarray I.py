"""
Author : janarddan
File_name = 7. Maximum Average Subarray I.py
Date : 17/09/26
Description :

Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

** Example 1: **

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

** Example 2: **

Input: nums = [5], k = 1
Output: 5.00000
"""

class Solution:
    def findMaxAverage_brute(self, nums: list[int], k: int) -> float:
        """
        - This is not the most naive brute-force approach.
        - The most naive approach would be to generate each subarray of size k,
          calculate its sum/average, and then return the maximum average.
        - Here, we directly calculate the sum of each window without explicitly
          creating the subarray.

        TC -> O(n-k+1) * O(k) ~ O(nk)
        SC -> O(1)
        """

        n = len(nums)
        max_avg = float("-inf")

        for i in range(n - k + 1):  # O(n-k+1)
            curr_sum = 0
            for j in range(i, k + i):  # O(k)
                curr_sum += nums[j]

            avg = curr_sum / k
            max_avg = max(max_avg, avg)

        return max_avg

    def findMaxAverage_optimal(self, nums: list[int], k: int) -> float:
        """
        Using Sliding window approach

        TC -> O(n)
        SC -> O(1)
        """

        max_avg = float("-inf")
        n = len(nums)
        start = 0

        curr_sum = 0
        for end in range(n):
            curr_sum += nums[end]
            window_size = end - start + 1
            if window_size == k:
                avg = curr_sum / k
                max_avg = max(avg, max_avg)

                curr_sum -= nums[start]
                start += 1

        return max_avg


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxAverage_brute([1,12,-5,-6,50,3], 4))
    print(sol.findMaxAverage_brute([5], 1))
    print()
    print(sol.findMaxAverage_optimal([1, 12, -5, -6, 50, 3], 4))
    print(sol.findMaxAverage_optimal([5], 1))




