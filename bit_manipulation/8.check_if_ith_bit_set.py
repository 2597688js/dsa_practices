"""
Author : Janarddan Sarkar
file_name : 8.check_if_ith_bit_set.py 
date : 20-03-2024
description : Given a number N and i, check if i-th bit is set or not. if set, return True, otherwise False.

Example : 13 in decimal = 1101 in binary. if i = 1, then 1st bit from right is 0, which is not set. So return False.
                                          if i = 0, then 0-th bit from right is 1, which is set. So return True
"""


def isIthBitSet(decimal_num, i):
    binary_num = bin(decimal_num)[2:]
    print(binary_num)
    if (int(binary_num) & (1 << i)) != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isIthBitSet(13, 0))
    print()

    print(isIthBitSet(13, 1))
    print()

    print(isIthBitSet(13, 2))
