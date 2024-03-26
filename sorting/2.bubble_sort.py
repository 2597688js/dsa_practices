"""
Author : Janarddan Sarkar
File_name = bubble_sort.py
Date : 28-02-2024
Description :

Approach:
In Bubble Sort algorithm,
1. traverse from left and compare adjacent elements and the higher one is placed at right side.
2. In this way, the largest element is moved to the rightmost end at first.
3. This process is then continued to find the second largest and place it and so on until the data is sorted.

In bubble sort,
First Pass:
    The largest element is placed in its correct position, i.e., the end of the array.
Second Pass:
    Place the second largest element at correct position
i.e., by the end of n-th pass, n-th largest element will be at its correct position.
"""


def bubble_sort(arr):
    n = len(arr)
    pass


if __name__ == "__main__":
    print(bubble_sort([8, 1, 9, 3, 7, 1]))
