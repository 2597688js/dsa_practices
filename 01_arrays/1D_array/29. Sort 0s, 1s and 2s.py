"""
Author : janarddan
File_name = 29. Sort 0s, 1s and 2s.py
Date : 03/09/26
Description :

Sort 0s, 1s and 2s

Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

Note: You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

=============================It can be asked differently as well =====================================================

Leetcode 75. Sort Colors

You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the
same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


** Example 1: **

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

** Example 2: **

Input: nums = [2,0,1]

Output: [0,1,2]

Explanation:

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

"""


class Solution:
    def sort012(self, arr):
        """
        TC -> O(n)
        """
        d = {} # val : count
        for num in arr:  # First pass -> O(n)
            d[num] = d.get(num, 0) + 1
            # if num not in d:
            #     d[num] = 1
            # else:
            #     d[num] += 1

        # ---- (2nd pass)The 3 below loops together -> O(n)
        idx = 0
        for _ in range(d[0]):  # replace with 0s in the original array
            arr[idx] = 0
            idx += 1

        for _ in range(d[1]):  # Then replace with 1s in the original array
            arr[idx] = 1
            idx += 1

        for _ in range(d[2]):  # Then replace with 2s in the original array
            arr[idx] = 2
            idx += 1

        return arr

    def sort012_optimal(self, arr):
        """
        DNF (Duth National Flag) algo
        0 to low-1 → all 0s
        low to mid-1 → all 1s
        mid to high → unknown/ unsorted
        high+1 to end → all 2s
        """

        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            else: # arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


        return  arr


if __name__ == "__main__":
    sol = Solution()
    # print(sol.sort012([0, 1, 2, 0, 1, 2]))
    print()
    print(sol.sort012_optimal([0, 1, 2, 0, 1, 2]))

# code here
