"""
Author : Janarddan Sarkar
File_name = 5.find_nth_largest.py
Date : 29-02-2024
Description :  Given an array and N, find N-th largest element from the array. This is the generalised version
of find second largest problem.

Example 1:
    Input : [1, 3, 2, 5, 7, 7, 6]], N = 3.
    Output = 5 as 5 is the 3rd largest number.

Example 2:
    Input : [19, 32, 52, 65, 37, 7, 61]], N = 2.
    Output = 61 as 61 is the 2-nd largest number.

"""

"""
Explanation:
The logic provided is essentially a modified version of the QuickSort algorithm. Instead of fully sorting the array,
 we are partitioning it based on the pivot element and then recursively searching in the appropriate partition 
 based on the desired position of the N-th largest element.

Here's a brief explanation of how it works:
1. We use the partition() function to place the pivot element in its correct position in the array such that
   all elements greater than the pivot are on its left and all elements smaller are on its right.
2. We compare the position of the pivot with the desired position of the N-th largest element. 
   If they are the same, we return the pivot element.
3. If the pivot's position is greater than the desired position, it means the N-th largest element lies in the
   left partition, so we recursively search in that partition.
4. If the pivot's position is less than the desired position, it means the N-th largest element lies in the right
   partition, so we recursively search in that partition.
5. We repeat this process until we find the N-th largest element.

While this logic resembles QuickSort, it's different in that it doesn't fully sort the array but rather partitions 
it based on the desired position of the N-th largest element.
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def find_nth_largest(arr, low, high, N):
    if N > 0 and N <= high - low + 1:
        pivot_index = partition(arr, low, high)
        if pivot_index - low == N - 1:
            return arr[pivot_index]
        elif pivot_index - low > N - 1:
            return find_nth_largest(arr, low, pivot_index - 1, N)
        else:
            return find_nth_largest(arr, pivot_index + 1, high, N - pivot_index + low - 1)
    return None


def nth_largest_element(arr, N):
    return find_nth_largest(arr, 0, len(arr) - 1, N)


if __name__ == "__main__":
    # Example usage:
    arr = [19, 32, 52, 65, 37, 7, 61]
    N = 3
    print(f"The {N}-th largest element in the array is: {nth_largest_element(arr, N)}")
    print()
    arr1 = [19, 32, 52, 65, 37, 7, 61]
    N1 = 5
    print(f"The {N1}-th largest element in the array is: {nth_largest_element(arr1, N1)}")

