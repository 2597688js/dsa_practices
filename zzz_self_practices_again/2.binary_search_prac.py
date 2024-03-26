"""
Author : Janarddan Sarkar
File_name = binary_search_prac.py
Date : 26-03-2024
Description :  Practice binary search
"""


def binary_search_prac(arr, k):
    arr = sorted(arr)  # For binary search to work, array has to be in sorted order

    left = 0     # to keep track of left index
    right = len(arr) - 1     # keep track of right index

    while left <= right:
        mid = left + ((right - left) // 2)     # mid index

        if k == arr[mid]:       # if array element at mid index  is equal to the target element(k)
            return f"{k} found at {mid} index"
        elif k < arr[mid]:    # if k is less than array element at the mid index, move the right index
            right = mid - 1
        elif k > arr[mid]:
            left = mid + 1


if __name__ == "__main__":
    print(binary_search_prac([1, 22, 39, 49, 51, 67, 74, 87], 87))
    print(binary_search_prac([1, 22, 39, 49, 51, 67, 74, 87], 49))
    print(binary_search_prac([1, 22, 39, 49, 51, 67, 74, 87], 67))
