"""
Author : janarddan
File_name = 5. Range Sum Query.py
Date : 27/08/26
Description :

# Leetcode 303. Range Sum Query - Immutable (Easy)

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

"""


class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixSum = []

        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += self.nums[i]
            self.prefixSum.append(curr_sum)

    def sumRangeBruteforce(self, left: int, right: int) -> int:
        """
        TC -> O(n)
        SC -> O(1)
        """
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]

        return total

    def sumRangeOptimal(self, left: int, right: int) -> int:

        rightSum = self.prefixSum[right]
        leftSum = self.prefixSum[left-1] if left >0 else 0

        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRangeBruteforce(0,2))
print(obj.sumRangeBruteforce(2,4))
print()
print(obj.sumRangeOptimal(0,2))
print(obj.sumRangeOptimal(2,4))

