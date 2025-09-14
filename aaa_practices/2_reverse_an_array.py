"""
Author : Janarddan Sarkar
file_name : 2_reverse_an_array.py 
date : 12-09-2025
description : 
"""

def reverse_arr(lst):
    """
    Two pointer approach
    """
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst


if __name__ == "__main__":
    print(reverse_arr([1, 2, 3, 4, 5]))
