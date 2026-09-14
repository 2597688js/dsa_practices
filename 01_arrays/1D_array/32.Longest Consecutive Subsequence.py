"""
Author : janarddan
File_name = 32.Longest Consecutive Subsequence.py
Date : 12/09/26
Description :

Leetcode 128: Longest Consecutive Subsequence

Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the
 subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.


"""


class Solution:
    def longestConsecutive_brute(self, arr):
        """
        TC -> O(n*n*n) = O(n**3)
        """
        longest = 0

        for num in arr:  # O(n)
            current_num = num

            count = 1
            curr_len = 1

           # # O(n) iterations × O(n) list search
            while current_num + count in arr: #  while -> O(n) | in arr -> O(n)
                curr_len += 1
                count += 1

            longest = max(longest, curr_len)

        return longest

    def longestConsecutive_better(self, arr):
        """
        TC -> O(nlogn) + O(n-1) = O(nlogn)
        """
        longest = 0

        arr.sort()  # TC -> O(n log n)

        curr_len = 1
        for i in range(1, len(arr)):  # TC -> O(n-1)
            if arr[i] == arr[i-1]:  # for duplicates -> skip
                continue
            elif arr[i] == arr[i-1] + 1:
                curr_len += 1
            else:
                curr_len = 1    # A new  sequence is started

            longest = max(longest, curr_len)

        return longest

    def longestConsecutive_optimal(self, arr):
        """
        TC -> O(n)
        SC -> O(n) for the extra set
        """

        arr_set = set()
        for num in arr:  # O(n)
            arr_set.add(num)

        longest = 0

        for num in arr_set:  # O(n)
            curr_len = 1
            if num - 1 not in arr_set: # O(1) - membership for set
                while (num + curr_len) in arr_set: # O(1) - membership for set
                    curr_len += 1

                longest = max(curr_len, longest)

        return longest


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive_brute([15, 13, 12, 14, 11, 10, 9]))
    print(sol.longestConsecutive_brute([1, 9, 3, 10, 4, 20, 2]))
    print(sol.longestConsecutive_brute([2, 6, 1, 9, 4, 5, 3]))
    print(sol.longestConsecutive_brute([22, 26, 1, 29, 24, 25, 23]))
    print()
    print(sol.longestConsecutive_better([15, 13, 12, 14, 11, 10, 9]))
    print(sol.longestConsecutive_better([1, 9, 3, 10, 4, 20, 2]))
    print(sol.longestConsecutive_better([2, 6, 1, 9, 4, 5, 3]))
    print(sol.longestConsecutive_better([22, 26, 1, 29, 24, 25, 23]))
    print(sol.longestConsecutive_better([22, 26, 25, 29, 24, 25, 23]))
    print(sol.longestConsecutive_better([1, 5, 5, 6, 7, 7, 8]))
    print()
    print(sol.longestConsecutive_optimal([15, 13, 12, 14, 11, 10, 9]))
    print(sol.longestConsecutive_optimal([1, 9, 3, 10, 4, 20, 2]))
    print(sol.longestConsecutive_optimal([2, 6, 1, 9, 4, 5, 3]))
    print(sol.longestConsecutive_optimal([22, 26, 1, 29, 24, 25, 23]))
    print(sol.longestConsecutive_optimal([22, 26, 25, 29, 24, 25, 23]))
    print(sol.longestConsecutive_optimal([1, 5, 5, 6, 7, 7, 8]))
