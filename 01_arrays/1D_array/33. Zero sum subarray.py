"""
Author : janarddan
File_name = 33. Zero sum subarray.py
Date : 14/09/26
Description : 33. Zero Sum Subarray
Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum.
Return true/false depending upon whether there is a subarray present with 0-sum or not.

** Examples: **

Input: arr[] = [4, 2, -3, 1, 6]
Output: true
Explanation: 2, -3, 1 is the subarray with a sum of 0.

Input: arr = [4, 2, 0, 1, 6]
Output: true
Explanation: 0 is one of the elements in the array so there exist a subarray with sum 0.

Input: arr = [1, 2, -1] Output: false

"""
from curses.ascii import isxdigit


class Solution:
    def subArrayExists_bruteforce(self, arr):
        """
        TC -> O(n**2)
        SC -> O(1)
        """
        n = len(arr)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                if curr_sum == 0:
                    return True

        return False

    def subArrayExists_optimal(self, arr):
        """
        TC -> O(n) + O(n) ~ O(n)
        SC -> O(n) for the prefix_d
        """
        n = len(arr)
        prefix_d = {} # sum : idx

        curr_sum  = 0
        for idx, num in enumerate(arr):  # TC -> O(n)
            curr_sum += num
            prefix_d[curr_sum] = prefix_d.get(curr_sum, 0) + 1

        for k,v in prefix_d.items(): # TC -> O(n)
            if v >= 2:
                return True

        return False


if __name__ == "__main__":
    sol  = Solution()
    print(sol.subArrayExists_bruteforce([4, 2, -3, 1, 6]))
    print(sol.subArrayExists_bruteforce([4, 2, 0, 1, 6]))
    print(sol.subArrayExists_bruteforce([1, 2, -1]))
    print()
    print(sol.subArrayExists_optimal([4, 2, -3, 1, 6]))
    print(sol.subArrayExists_optimal([4, 2, 0, 1, 6]))
    print(sol.subArrayExists_optimal([1, 2, -1]))