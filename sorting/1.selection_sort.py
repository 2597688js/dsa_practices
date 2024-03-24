"""
Author : Janarddan Sarkar
file_name : 1.selection_sort.py 
date : 10-03-2024
description :
Steps:
1. Initialization: Start with an unsorted array of elements.
2. Iteration through the array: Iterate through the array from the first element to the second-to-last element.
3. Finding the minimum: For each iteration, assume the current element is the smallest (initially set it as the minimum).
   Then, compare it with all subsequent elements to find the actual minimum element.
4. Swapping: After finding the minimum element, swap it with the element at the current position (the first element in the unsorted
   portion of the array).
5. Moving to the next element: Move to the next position and repeat steps 3 and 4.
6. Completing the sorting: Continue this process until the entire array is sorted.
7. Termination: Once all elements are sorted, the array is completely sorted.

Time complexity: O(n*n); n = length of the array
SPace complexity: O(1); no extra space is used
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        smallest_idx = i
        for j in range(i, n):
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j

        # swap
        temp = arr[i]
        arr[i] = arr[smallest_idx]
        arr[smallest_idx] = temp

    return arr


if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))
    print(selection_sort([640, 350, 212, 122, 11]))
