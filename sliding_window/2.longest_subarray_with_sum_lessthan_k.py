"""
Author : Janarddan Sarkar
File_name = 2.longest_subarray_with_sum_less_than_k.py
Date : 29-03-2024
Description :  Given an array of integers and a target value k, you need to find the length of the longest subarray
           whose sum is less than k. If no such subarray exists, return 0.

Example 1:
    arr = [9, 2, 5, 1, 10, 10], k = 14
    Ans = 3
    Explanation = [2, 5, 1] is the longest subarray with sum 8 which is less than 14

Example 2:
    arr = [1, -2, 1, 3, -4, 5, 2], target k = 5
    ans = 6
    Explanation = In the given example, the longest subarray with a sum less than 5 is [1, -2, 1, 3, -4, 5],
                  whose sum is 4. There is no other subarray with a sum less than 5 that has a longer length.

Example 3:
    arr = [1, -2, 1, 3, -4, 5, 2], target k = -6
    ans = 6
    Explanation = In the given example, the longest subarray with a sum less than 5 is [1, -2, 1, 3, -4, 5],
                  whose sum is 4. There is no other subarray with a sum less than 5 that has a longer length.
"""


def longest_subarr_with_sum_lessthan_k(arr, k):
    n = len(arr)

    maxlen = 0
    ans_subarr = {'ans': ''}
    left, right = 0, 0

    while right < n:
        subarr = arr[left: right+1]
        curr_sum = sum(subarr)
        subarr_len = right - left + 1
        if curr_sum <= k:
            if subarr_len > maxlen:
                maxlen = subarr_len
                ans_subarr['ans'] = subarr

            right += 1
        elif curr_sum > k:
            left += 1

    return (f"The length of longest subarray of sum < {k} is {maxlen}."
            f" The subarray is {ans_subarr['ans']}")


if __name__ == '__main__':
    print(longest_subarr_with_sum_lessthan_k([9, 2, 5, 1, 10, 10], 14))
    print(longest_subarr_with_sum_lessthan_k([1, -2, 1, 3, -4, 5, 2], 5))
    print(longest_subarr_with_sum_lessthan_k([1, 2, 1, 0, 1, 1, 0], 4))
