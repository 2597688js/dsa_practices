"""
Author : Janarddan Sarkar
File_name = 1.subarray_k_with_max_sum.py
Date : 27-03-2024
Description :

Example 1:
    Inputs: arr = [-1, 2, 3, 3, 4, 5, -1], k = 4 (window size)
    Output: [3, 3, 4, 5].
    Explanation: [-1, 2, 3, 3] sum = 7
                 [2, 3, 3, 4] sum = 12
                 [3, 3, 4, 5] sum = 15
                 [3, 4, 5, -1] sum = 11
    So, [3, 3, 4, 5] has the maximum sum(15) with window size 4.
"""

# 1. Bruteforce
"""
Find all the subarray with length 4 and then find the one with maximum sum.
"""

# 2. Better
"""
Using Sliding window and two pointer approach
"""
def subarray_k_maxsum1(arr, k):
    n = len(arr)

    left = 0
    right = k - 1

    maxsum = 0

    while right < n:
        curr_sum = sum(arr[left:right+1])
        maxsum = max(curr_sum, maxsum)

        right += 1
        left += 1

    return maxsum

def subarray_k_maxsum2(arr, k):
    n = len(arr)

    left = 0
    right = k - 1

    left_ans, right_ans = left, right
    maxsum = 0

    while right < n:
        curr_sum = 0
        for i in range(left, right+1):
            curr_sum += arr[i]

        if curr_sum > maxsum:
            maxsum = curr_sum
            left_ans = left
            right_ans = right

        right += 1
        left += 1

    return f"The maximum sum is {maxsum}, from index {left_ans} to {right_ans}"


def subarray_k_maxsum3(arr, k):
    n = len(arr)

    left = 0
    right = k - 1

    maxsum = 0
    for i in range(left, right+1):
        maxsum += arr[i]

    left_ans, right_ans = left, right

    curr_sum = maxsum

    while right < n-1:
        curr_sum = curr_sum - arr[left] + arr[right+1]

        if curr_sum > maxsum:
            maxsum = curr_sum
            left_ans = left + 1
            right_ans = right + 1

        right += 1
        left += 1

    return f"The maximum sum is {maxsum}, from index {left_ans} to {right_ans}"


if __name__ == "__main__":
    print(subarray_k_maxsum1([-1, 2, 3, 3, 4, 5, -1], 4))
    print(subarray_k_maxsum2([-1, 2, 3, 3, 4, 5, -1], 4))
    print(subarray_k_maxsum3([-1, 2, 3, 3, 4, 5, -1], 4))
