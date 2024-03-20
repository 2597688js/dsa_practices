"""
Author : Janarddan Sarkar
File_name = 2.binary_to_decimal.py
Date : 18-03-2024
Description :  convert from binary number to decimal number

binary_to_decimal = lambda binary_num: int(binary_num, 2)
         int('1010', 2) will interpret '1010' as a binary number and convert it to decimal, which is 10.

"""

# This is the most naive approach
"""

"""
def binary_to_decimal(binary_num:str):
    digit_len = len(binary_num)
    decimal_num = 0
    for i in range(digit_len):
        place = digit_len - i - 1
        digit = int(binary_num[place])
        pow_sum = digit * (2 ** i)
        decimal_num = decimal_num + pow_sum

    return decimal_num


# Another logic to calculate the power of 2
def binary_to_decimal1(binary_num: str):
    """
    here, we are not calculating exponent value each time, this is expensive.
    Instead, we are using the same previous multiplication value iteratively.
    """
    decimal_num = 0

    digit_len = len(binary_num)
    pow_val = 1

    for i in range(digit_len):
        curr_digit = binary_num[digit_len - (i+1)]
        decimal_num += int(curr_digit) * pow_val
        pow_val = 2 * pow_val


    return decimal_num


if __name__ == "__main__":
    print(binary_to_decimal('1010'))
    print(binary_to_decimal('10100'))
    print(binary_to_decimal('10000'))
    print()
    print(binary_to_decimal1('1010'))
    print(binary_to_decimal1('10100'))
    print(binary_to_decimal1('10000'))

