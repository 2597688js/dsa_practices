"""
Author : Janarddan Sarkar
File_name = merge_sort.py
Date : 28-02-2024
Description :  Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray,
               and then merging the sorted subarrays back together to form the final sorted array.
               In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half,
               and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
"""
def merge(arr, low, mid, high):
    # Initialize indices for the left and right halves of the subarray
    left = low
    right = mid + 1

    # Create a temporary array to store sorted elements
    sorted_arr = [0] * len(arr)
    index = low  # Index to track position in sorted_arr

    # Merge elements from both halves into sorted order
    while left <= mid and right <= high:
        # Compare elements from left and right halves
        # and insert the smaller element into sorted_arr
        if arr[left] <= arr[right]:
            sorted_arr[index] = arr[left]
            left += 1
        else:
            sorted_arr[index] = arr[right]
            right += 1
        index += 1

    # Copy any remaining elements from left half
    while left <= mid:
        sorted_arr[index] = arr[left]
        left += 1
        index += 1

    # Copy any remaining elements from right half
    while right <= high:
        sorted_arr[index] = arr[right]
        right += 1
        index += 1

    # Copy sorted elements back to the original array
    for i in range(low, high + 1):
        arr[i] = sorted_arr[i]


def merge_sort(arr, low, high):
    if low < high:
        # Find the middle index
        mid = (low + high) // 2

        # Recursively divide the array into halves
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Merge the sorted halves
        merge(arr, low, mid, high)


if __name__ == "__main__":
    # Example usage
    # arr1 = [3, 1, 2, 4, 1, 5, 2, 6, 4]
    # print("Original array:", arr1)
    # merge_sort(arr1, 0, len(arr1) - 1)
    # print("Sorted array:", arr1)
    # print()
    arr2 = [334, 211, 112, 14, 1]
    print("Original array:", arr2)
    merge_sort(arr2, 0, len(arr2) - 1)
    print("Sorted array:", arr2)



