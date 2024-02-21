"""
Author : Janarddan Sarkar
File_name = two_consecutive_sums.py
Date : 19-01-2024
Description : input = [1, 2, 3, 4, 5, 6], output = [1, 2, (1+2=3)], [2, 3, 5(2+3)], [3, 4, 7] . . . [5, 6, 11]
"""

lst1 = [1, 2, 3, 4, 5, 6]

ptr1, ptr2 = 0, 1

n = len(lst1)

while ptr2 != n:
    print([lst1[ptr1], lst1[ptr2], lst1[ptr1] + lst1[ptr2]])
    ptr1 += 1
    ptr2 += 1
