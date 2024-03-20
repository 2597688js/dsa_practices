"""
Author : Janarddan Sarkar
file_name : 7.swap_two_numbers_using_xor.py 
date : 20-03-2024
description : swap two numbers without using third variable.
             Hint: use XOR operation
"""


def swap_nums(a, b):
    print("Before swapping : ", (a, b))
    a = a ^ b
    b = a ^ b    # (a ^ b) ^ b = a ^ (b^b) = a ^ 0 = a
    a = a ^ b    # (a ^ b) ^ a = 0 ^ b = b

    return a, b


if __name__ == "__main__":
    print("After swapping : ", swap_nums(5, 6))
