"""
Author : Janarddan Sarkar
file_name : 16.find_element_appearing_once.py 
date : 16-03-2024
description : Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
    Input Format: arr[] = {2,2,1}
    Result: 1
    Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
    Input Format: arr[] = {4,1,2,1,2}
    Result: 4
    Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""

# 1.Bruteforce
""""
Naive Approach(Brute-force approach): 
Intuition:
For every element present in the array, we will do a linear search and count the occurrence. If for any element, the occurrence is 1, 
we will return it.

Approach:
The steps are as follows:
    1. First, we will run a loop(say i) to select the elements of the array one by one.
    2. For every element arr[i], we will perform a linear search using another loop and count its occurrence.
    3. If for any element the occurrence is 1, we will return it.
    
Time Complexity: O(N**N), where N = size of the given array.
Reason: For every element, we are performing a linear search to count its occurrence. The linear search takes O(N) time complexity. 
And there are N elements in the array. So, the total time complexity will be O(N2).

Space Complexity: O(1) as we are not using any extra space.
"""
def find_element_appearing_once_bruteforce(arr):
    for i in range(len(arr)):
        num = arr[i]   # selected element tp be searched in the array
        count = 0
        for j in range(len(arr)):
            if arr[j] == num:
                count += 1

        if count == 1:
            return num

# 2. Better approach (using Hashing)
"""
Better Approach(Using Hashing): 
Intuition:
In the previous approach, we were finding the occurrence of an element using linear search. We can optimize this using hashing technique.
We can simply hash the elements along with their occurrences in the form of (key, value) pair. 
Thus, we can reduce the cost of finding the occurrence and hence the time complexity.

Now, hashing can be done in two different ways and they are the following:

Array hashing(not applicable if the array contains negatives or very large numbers)
Hashing using the map data structure

Array hashing:
In order to hash using an array, we need to first find the maximum element(say maxElement) to get the range of the hash array. 
The index of the hash array will represent the elements of the given array and the value stored in that index will be the number of occurrences.
 Now, the size of the array must be maxElement+1 as we need to hash the maxElement itself.
 
Complexity Analysis
    Time Complexity: O(N)+O(N)+O(N), where N = size of the array
    Reason: One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in 
            the array.
    
    Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.
"""
def find_element_appearing_once_better(arr):
    hash_dict = {}
    for x in arr:
        hash_dict[x] = 0                           # O(N), N = len(arr)

    for x in arr:
        if x in hash_dict:
            hash_dict[x] = hash_dict[x] + 1        # O(N), N = len(arr)

    for k in hash_dict:
        if hash_dict[k] == 1:                      # O(N), N = len(arr)
            return k


def find_element_appearing_once_optimal(arr):
    xor_res = 0
    for x in arr:
        xor_res ^= x     # xor_res = xor_res ^ x

    return xor_res


if __name__ == "__main__":
    print("(Bruteforce) element appearing once : ", find_element_appearing_once_bruteforce([2, 2, 1]))
    print("(Bruteforce) element appearing once: ", find_element_appearing_once_bruteforce([4, 1, 2, 1, 2]))
    print("(Better) element appearing once: ", find_element_appearing_once_better([4, 1, 2, 1, 2]))
    print("(Optimal) element appearing once: ", find_element_appearing_once_optimal([4, 1, 2, 1, 2]))
    print("(Optimal) element appearing once: ", find_element_appearing_once_optimal([4, 1, 2, 1, 2, 5, 6, 7, 7, 6, 4]))

