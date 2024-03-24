"""
Author : Janarddan Sarkar
file_name : 2.binary_search.py 
date : 24-03-2024
description :

Conditions to apply Binary Search algorithm:
    1. The data structure must be sorted.
    2. Access to any element of the data structure takes constant time.

Steps:
1. Divide the search space into two halves by finding the middle index “mid”.
2. Compare the middle element of the search space with the key.
3. If the key is found at middle element, the process is terminated.
4. If the key is not found at middle element, choose which half will be used as the next search space.
    4.1 If the key is smaller than the middle element, then the left side is used for next search.
    4.2 If the key is larger than the middle element, then the right side is used for next search.
5. This process is continued until the key is found or the total search space is exhausted.


Time complexity: O(log n); n = length of the array. This is because binary search divides the search space in half in each iteration,
                 leading to a logarithmic time complexity. Specifically, with each iteration, the size of the search space is halved until
                 the target element is found or the search space becomes empty.
Space complexity: O(1); we are not using any extra space.
"""


def binary_search(arr, k):
    """
    search for k in the given array
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if k == arr[mid]:
            return f"{k} found at index {mid} of {arr}."
        elif k < arr[mid]:
            right = mid - 1
        elif k > arr[mid]:
            left = mid + 1

    return f"{k} not found in {arr}."


if __name__ == '__main__':
    print(binary_search([2, 3, 4, 10, 40], 10))
    print(binary_search([2, 3, 4, 10, 40], 3))
    print(binary_search([2, 3, 4, 10, 40, 50], 3))
    print(binary_search([2, 3, 4, 10, 40, 50], 10))
    print(binary_search([1, 3, 5, 7, 9, 11], 7))
    print(binary_search([1, 3, 5, 7, 9], 9))
    print(binary_search([1, 3, 5, 7, 9], 11))
