"""
Author : janarddan
File_name = 3.maximum_sum_subarray_size_k.py
Date : 16/07/26
Description :
1. Maximum Sum Subarray of Size K (Easy) ⭐⭐⭐⭐⭐

Problem:
Given an array of integers and an integer k, find the maximum sum of any contiguous subarray of size k.

Example:

nums = [2,1,5,1,3,2]
k = 3

Output = 9

Explanation:
[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9  ← Maximum
[1,3,2] = 6

"""



class Solution:
    def maxSubarraySum_brute(self, arr, k):
        """
        TC -> O(n-k+1) * O(k) ≈ O(n*k)
        SC -> O(1)
        """
        n = len(arr)
        maxi = float("-inf")

        for i in range(n - k + 1): # O(n-k)
            curr_sum = 0
            for j in range(i, k + i): # O(k)
                curr_sum += arr[j]

            maxi = max(curr_sum, maxi)

        return maxi

    def maxSubarraySum_optimal(self, arr, k):
        """
        TC -> O(n)
        SC -> O(1)
        """
        left = 0
        maxi = float('-inf')
        curr_sum = 0
        for right in range(len(arr)):
            curr_sum += arr[right]
            window_len = right - left + 1
            if window_len == k:
                maxi = max(maxi, curr_sum)
                curr_sum -= arr[left]
                left += 1

        return maxi

if __name__ == "__main__":

    nums = [-2,-1,-5,-1,-3,-2]
    k = 3

    sol = Solution()
    print(sol.maxSubarraySum_optimal(nums, k))
    print()
    print(sol.maxSubarraySum_brute([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
    print(sol.maxSubarraySum_brute([100, 200, 300, 400], 1))
    print(sol.maxSubarraySum_brute([-100, -200, -300, -400], 1))
