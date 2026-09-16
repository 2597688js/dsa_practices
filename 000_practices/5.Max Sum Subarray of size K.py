"""
Author : janarddan
File_name = 5.Max Sum Subarray of size K.py
Date : 16/09/26
Description :

Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.

"""


class Solution:
    def maxSubarraySum_brute(self, arr, k):
        """
        TC -> O(n-k+1) * O(k) ≈ O(n*k)
        SC -> O(1) | O(k) when storing the subarray too
        """
        n = len(arr)
        maxi = float("-inf")

        result = None
        for i in range(n - k + 1): # O(n-k+1)
            curr_sum = 0
            subarr = []
            for j in range(i, k + i): # O(k)
                curr_sum += arr[j]
                subarr.append(arr[j])

            # maxi = max(curr_sum, maxi)

            if curr_sum > maxi:
                maxi = curr_sum
                result = subarr

        return maxi, result

    def maxSubarraySum_optimal(self, arr, k):
        """
        TC -> O(n)
        SC -> O(1)
        """
        n = len(arr)

        start = 0
        curr_sum = 0
        maxi = float("-inf")

        for end in range(n):
            curr_sum += arr[end]
            if (end - start + 1) == k: # end - start + 1 = window size
                maxi = max(maxi, curr_sum)

                curr_sum -= arr[start]
                start += 1

        return maxi

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySum_brute([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
    print(sol.maxSubarraySum_brute([100, 200, 300, 400], 1))
    print(sol.maxSubarraySum_brute([-100, -200, -300, -400], 1))
    print()
    print(sol.maxSubarraySum_optimal([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
    print(sol.maxSubarraySum_optimal([100, 200, 300, 400], 1))
    print(sol.maxSubarraySum_optimal([-100, -200, -300, -400], 1))
