"""
Author : Janarddan Sarkar
File_name = 12.reverse_array_portion.py
Date : 29-02-2024
Description :  given an array, start index and end index. Reverse the array from start index to end index
"""


def reverseGivenIndex(arr, strt_idx, end_idx):
    n = (end_idx - strt_idx) + 1   # size of the subarray arr[strt_idx:end_idx]

    for i in range(n // 2):
        temp = arr[strt_idx + i]
        arr[strt_idx + i] = arr[end_idx - i]
        arr[end_idx - i] = temp

    return arr


if __name__ == "__main__":
    print(reverseGivenIndex([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 5))
    print(reverseGivenIndex([1, 2, 3, 4, 5, 6], 1, 5))
    print(reverseGivenIndex([1, 2, 3, 4, 5, 6], 0, 5))
    print(reverseGivenIndex([1, 2, 3, 4, 5, 6], 0, 2))


