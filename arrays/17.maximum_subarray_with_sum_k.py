"""
Author : Janarddan Sarkar
file_name : 17.maximum_subarray_with_sum_k.py 
date : 17-03-2024
description :
Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Example 1:
    Input Format: N = 3, k = 5, array[] = {2,3,5}
    Result: 2
    Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
    Input Format: N = 3, k = 1, array[] = {-1, 1, 1}
    Result: 3
    Explanation: The longest subarray with sum 1 is {-1, 1, 1}. And its length is 3.

Example 3:
    Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
    Result: 3
    Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""

# 1. Bruteforce approach - find all the sub-arrays
"""
Bruteforce approach 
Complexity Analysis
Time Complexity: O(N x N) approx., where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
"""
def maximum_subarray_with_sum_k_bruteforce1(arr, k):
    n = len(arr)

    max_len = 0

    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            subarray_sum = sum(subarray)
            if subarray_sum == k:
                subarray_len = len(subarray)

                max_len = max(subarray_len, max_len)

    return max_len


def maximum_subarray_with_sum_k_bruteforce2(arr, k):
    """
    TC - O( N * N), because 2 loops
    SC - O(1), because no extra space is used
    """
    n = len(arr)

    max_len = 0

    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum = subarray_sum + arr[j]
            if subarray_sum == k:
                subarray_len = j + 1 - i

                max_len = max(subarray_len, max_len)

    return max_len

# 3. Optimal - Using Hashing
"""
"""
def maximum_subarray_with_sum_k_optimal(arr, k):
    n = len(arr)

    prefix_sum = 0
    max_len = 0
    hash_dict = {}
    hash_dict[prefix_sum] = -1  # Initialize the dictionary with prefix sum 0 at index -1

    for i in range(n):
        prefix_sum += arr[i]

        remaining_sum = prefix_sum - k
        if remaining_sum in hash_dict:
            subarr_len = i - hash_dict[remaining_sum]
            max_len = max(max_len, subarr_len)

        if prefix_sum not in hash_dict:
            hash_dict[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    print("Bruteforce 1 : ", maximum_subarray_with_sum_k_bruteforce1([2, 0, 0, 3], 3))
    print("Bruteforce 1 : ", maximum_subarray_with_sum_k_bruteforce1([2, 3, 5], 5))

    print("Bruteforce 2 : ", maximum_subarray_with_sum_k_bruteforce2([2, 3, 5], 5))
    print("Bruteforce 2 : ", maximum_subarray_with_sum_k_bruteforce2([2, 0, 0, 3], 5))
    print("Bruteforce 2 : ", maximum_subarray_with_sum_k_bruteforce2([2, 0, 0, 3], 3))
    print()

    print("Optimal : ", maximum_subarray_with_sum_k_optimal([2, 3, 5], 5))
    print("Optimal : ", maximum_subarray_with_sum_k_optimal([2, 0, 0, 3], 3))
    print("Optimal : ", maximum_subarray_with_sum_k_optimal([1, -1, 5, -2, 3], 3))   # 1, -1 , 5, -2
