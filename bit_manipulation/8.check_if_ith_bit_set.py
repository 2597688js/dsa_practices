"""
Author : Janarddan Sarkar
file_name : 8.check_if_ith_bit_set.py 
date : 20-03-2024
description : Given a number N and i, check if i-th bit is set or not. if set, return True, otherwise False.

Example : 13 in decimal = 1101 in binary. if i = 1, then 1st bit from right is 0, which is not set. So return False.
                                          if i = 0, then 0-th bit from right is 1, which is set. So return True

Logic is:
    Using Left shift operator:
        if [N & (1 << i)] != 0, then i-the bit is set, otherwise unset.
"""


# 1. Bruteforce
def isIthBitSet_bruteforce(decimal_num, i):
    binary_num = bin(decimal_num)[2:]

    n = len(binary_num)

    if binary_num[n - (i+1)] == '0':
        return False
    if binary_num[n - (i+1)] == '1':
        return True


# 2. Better


# 3. Optimal
def isIthBitSet_optimal(decimal_num, i):
    binary_num = bin(decimal_num)[2:]
    print(binary_num)
    if (int(binary_num) & (1 << i)) != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"{0}-th bit of {13}({bin(13)[2:]}) is (bruteforce): ", isIthBitSet_bruteforce(13, 0))
    print()
    print(f"{1}-th bit of {13}({bin(13)[2:]}) is (bruteforce): ", isIthBitSet_bruteforce(13, 1))
    print()

    print("Optimal : ", isIthBitSet_optimal(13, 0))
    print()

    print("Optimal : ", isIthBitSet_optimal(13, 1))
    print()

    print("Optimal : ", isIthBitSet_optimal(13, 2))
