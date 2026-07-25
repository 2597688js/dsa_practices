"""
Author : janarddan
File_name = binary_search.py
Date : 19/07/26
Description : Implementation of Binary Search Algorithm

"""

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n-1

    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search1(arr, target):
    n = len(arr)
    left = 0
    right = n-1

    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1

    mid = left + (right - left)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:               # arr[mid] > target
        return binary_search_recursive(arr, target, left, mid - 1)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(arr, 23))
    print(binary_search([2,5,8,12,16,23,38,56,72], 23))
    print(binary_search([2,5,8,12,16,23,38,56,72], 16))
    print()
    print(binary_search1(arr, 23))
    print(binary_search1([2, 5, 8, 12, 16, 23, 38, 56, 72], 23))
    print(binary_search1([2, 5, 8, 12, 16, 23, 38, 56, 72], 16))
    print()
    arr1 = [11, 23, 34, 56, 78, 99]
    print(binary_search_recursive(arr1, 23, 0, len(arr1) - 1))
    print(binary_search_recursive(arr1, 16, 0, len(arr1) - 1))
