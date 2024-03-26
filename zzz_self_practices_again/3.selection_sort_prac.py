"""
Author : Janarddan Sarkar
File_name = selection_sort_prac.py
Date : 26-03-2024
Description :  Selection sort practice
"""


def selection_sort_prac(arr):
    n = len(arr)
    for i in range(n):
        smallest = 0
        smallest_idx = i
        for j in range(i+1, n):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_idx = j

        # swap
        temp = arr[i]
        arr[i] = smallest
        arr[smallest_idx] = temp

    return arr

if __name__ == "__main__":
    print(selection_sort_prac([1, 1, 1, 1, 1]))
    print(selection_sort_prac([5, 5, 6, 7, 8, 9]))