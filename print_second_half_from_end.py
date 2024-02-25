"""
Author : Janarddan Sarkar
file_name : print_second_half_from_end.py 
date : 25-02-2024
description : input = [1, 3, 43, 56, 78, 90, 3]
             print till the mid of this array from last. i.e.,
             output = 3, 90, 78, 56

             input = [11, 45, 67, 76, 4, 55, 32, 12, 99]
             output = [99, 12, 32, 55, 4]
"""


def print_arr_half_end(arr):
    n = len(arr)

    res = []
    for i in range(n//2 + 1):
        res.append(arr[n-(i+1)])

    return res


print(print_arr_half_end([1, 3, 43, 56, 78, 90, 3]))
print(print_arr_half_end([11, 45, 67, 76, 4, 55, 32, 12, 99]))
