"""
Author : janarddan
File_name = 25.find_max_min_of_arr.py
Date : 07/08/26
Description : Find the maximum and minimum of an array

For both, TC -> O(n), SC -> O(1)

"""

def find_max(arr):
    maxi = float("-inf")

    n = len(arr)

    if n == 0:
        return

    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]

    return maxi

def find_min(arr):
    mini = float("inf")

    n = len(arr)

    if n == 0:
        return

    for i in range(n):
        if arr[i] < mini:
            mini = arr[i]

    return mini


if __name__ == "__main__":
    print(find_max([1,5,6,7,8,12,34]))
    print(find_max([11]))
    print(find_max([]))
    print()
    print(find_min([1, 5, 6, 7, -8, 12, 34]))
    print(find_min([11]))
    print(find_min([]))

