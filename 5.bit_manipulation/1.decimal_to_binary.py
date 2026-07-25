"""
Author : Janarddan Sarkar
File_name = 1.decimal_to_binary.py
Date : 18-03-2024
Description :  convert a decimal number to binary
In python, we can use bin(decimal_num) to convert from decimal to binary
"""

# This is the most naive approach
"""
TC - log n; n -> number of digits. because we are dividing by 2
SC - log n ; for the same reason.
"""
def decimal_to_binary(num:int):
    binary_num = ''
    while num != 0:
        rem = num % 2
        binary_num += str(rem)
        num = num // 2

    return binary_num[::-1]


if __name__ == "__main__":
    print(decimal_to_binary(10))
    print(decimal_to_binary(20))
    print(decimal_to_binary(16))
    print(decimal_to_binary(7))

