"""
Author : Janarddan Sarkar
File_name = 9.set_ith_bit.py
Date : 21-03-2024
Description :  given a number N and i, set the i-th bit i.e., make the i-th bit as 1. if it is already 1, leave as it is.

Example 1:
    N = 9, i = 1
    9 in decimal = 1001 in binary, i-th bit = 1st bit is 0, make that 1 i.e., 1011 which is 11 in decimal. so return 11
"""


# 1. Bruteforce
def set_ith_bit_bruteforce(decimal_num, i):
    binary_num = bin(decimal_num)[2:]
    n = len(binary_num)

    set_binary_num = ''
    for k in range(n):
        if k == n-(i+1):
            set_binary_num += '1'
        else:
            set_binary_num += binary_num[k]

    return int(set_binary_num, 2)


# 3. Optimal
"""
Logic:
    perform  OR operation of N with ( 1 << i) i.e., N | (1 << i). It will set the i-th bit
"""
def set_ith_bit_optimal(decimal_num, i):
    # binary_num = bin(decimal_num)[2:]
    # set_binary_num = binary_num | (1 << i)

    return decimal_num | (1 << i)



if __name__ == "__main__":
    print("Bruteforce : ", set_ith_bit_bruteforce(9, 1))
    print("Optimal : ", set_ith_bit_optimal(9, 1))
