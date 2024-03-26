"""
Author : Janarddan Sarkar
File_name = kadane_algo_maximum_subarray.py
Date : 26-02-2024
Description :  
"""
import sys


def max_subarray(arr):
    n = len(arr)

    max_sum = float('-inf')  # Initialize max_sum with negative infinity to handle all negative array cases
    current_sum = 0

    start_idx, end_idx = -1, -1
    temp_start_idx = 0     # Keep track of temporary start index

    for i in range(n):
        if current_sum == 0:
            temp_start_idx = i

        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum

            start_idx = temp_start_idx  # Update start index
            end_idx = i                 # Update end index

        if current_sum < 0:
            current_sum = 0

    return max_sum, arr[start_idx: end_idx + 1]


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

