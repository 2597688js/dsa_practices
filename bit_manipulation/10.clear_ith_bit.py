"""
Author : Janarddan Sarkar
File_name = 10.clear_ith_bit.py
Date : 21-03-2024
Description :
given a number N and i, clear the i-th bit i.e., make the i-th bit as 0. if it is already 0, leave as it is.
"""


# 3. Optimal
"""
Logic:
    perform  AND operation of N with negation of ( 1 << i) i.e., N & ~(1 << i). It will clear the i-th bit
"""
def clear_ith_bit_optimal(decimal_num, i):
    return decimal_num & ~(1 << i)


if __name__ == "__main__":
    print("Optimal : ", clear_ith_bit_optimal(9, 1))
    print("Optimal : ", clear_ith_bit_optimal(13, 2))
    print("Optimal : ", clear_ith_bit_optimal(7, 1))
    print("Optimal : ", clear_ith_bit_optimal(5, 0))
