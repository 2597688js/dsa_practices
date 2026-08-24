"""
Author : janarddan
File_name = 27.no_of_subarray_with_sum_k.py
Date : 19/08/26
Description :

Given an array of integers and a target sum, find the total number of
contiguous subarrays whose sum is equal to the target.

Example:
Input: arr = [3, 3, 2, 9, 5, 3, 11, 8], target = 8
Output: 3

Explanation:
There are 3 contiguous subarrays whose sum is equal to 8:
[3, 3, 2]
[5, 3]
[8]

Edge cases:

arr = [], target = 2
arr = [5], target = 3
arr = [3, 3, 2, 9, 5, 3, 11, 8, 12, -3], target = 8
"""

def count_subarrays_with_sum_k(arr, target)->int:
    """
    TC -> O(n**2)
    SC -> O(1)
    """
    n = len(arr)

    count = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == target:
                count += 1
                break


    return count

def count_subarrays_with_sum_k_way2(arr, target)->int:
    """
    TC -> O(n**2)
    SC -> O(1)
    """
    n = len(arr)

    count = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == target:
                count += 1
                break



    return count

if __name__ == "__main__":
    print(count_subarrays_with_sum_k([1,1,2,1], 2))
    print(count_subarrays_with_sum_k([3, 3, 2, 9, 5, 3, 11, 8], 8))
    print(count_subarrays_with_sum_k([3, 3, 2, 9, 5, 3, 11, 8, 12, -4], 8))
    print()
    print(count_subarrays_with_sum_k_way2([1, 1, 2, 1], 2))
    print(count_subarrays_with_sum_k_way2([3, 3, 2, 9, 5, 3, 11, 8], 8))
    print(count_subarrays_with_sum_k_way2([3, 3, 2, 9, 5, 3, 11, 8, 12, -4], 8))
