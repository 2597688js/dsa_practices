"""
Author : Janarddan Sarkar
File_name = merge_sort_prac.py
Date : 01-04-2024
Description :  Practice of merge sort
"""

def merge(arr, low, mid, high):
    print("============ Merge ==========: ", arr[low:high+1])
    left = low
    right = mid + 1

    sorted_arr = [0] * len(arr)
    idx = low

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            sorted_arr[idx] = arr[left]
            left += 1
        else:
            sorted_arr[idx] = arr[right]
            right += 1

        idx += 1

    while right <= high:
        sorted_arr[idx] = arr[right]
        right += 1
        idx += 1

    while left <= mid:
        sorted_arr[idx] = arr[left]
        left += 1
        idx += 1

    for i in range(low, high+1):
        arr[i] = sorted_arr[i]

def merge_sort(arr, low, high):
    print("Merge sort: ", arr[low:high+1])
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


if __name__ == "__main__":
    # arr1 = [5, 4, 3, 2, 1]
    # print("Original array: ", arr1)
    # merge_sort(arr1, 0, len(arr1)-1)
    # print("After sorting: ", arr1)
    print()
    arr2 = [201, 129, 56, 32, 11, 7]
    print("Original array: ", arr2)
    merge_sort(arr2, 0, len(arr2) - 1)
    print("After sorting: ", arr2)
