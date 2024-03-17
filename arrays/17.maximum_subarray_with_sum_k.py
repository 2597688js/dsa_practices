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
Optimal Approach (Using Hashing): 
Approach:
The steps are as follows:
    1. First, we will declare a map to store the prefix sums and the indices.
    2. Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
    3. For each index i, we will do the following:
        3.1 We will add the current element i.e. a[i] to the prefix sum.
        3.2 If the sum is equal to k, we should consider the length of the current subarray i.e. i+1. We will compare this length with the existing 
            length and consider the maximum one.
        3.3 We will calculate the prefix sum i.e. x-k, of the remaining subarray.
        3.4 If that sum of the remaining part i.e. x-k exists in the map, we will calculate the length i.e. i-preSumMap[x-k], and consider the 
            maximum one comparing it with the existing length we have achieved until now.
        3.5 If the sum, we got after step 3.1, does not exist in the map we will add that with the current index into the map. We are checking the 
            map before insertion because we want the index to be as minimum as possible and so we will consider the earliest index where the sum 
            x-k has occurred.
            
    In this approach, we are using the concept of the prefix sum to solve this problem. Here, the prefix sum of a subarray ending at index i,
     simply means the sum of all the elements of that subarray.
     
Complexity Analysis
    Time Complexity:
        O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
    Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, 
    unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, 
    the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.
    
    Space Complexity: O(N) as we are using a map data structure.
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
