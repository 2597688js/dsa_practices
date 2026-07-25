"""
Author : Janarddan Sarkar
File_name = 3.Ones_complement.py
Date : 20-03-2024
Description :  1's complement is flipping all bits 1->0 and 0 ->1

13 in decimal = 1101 in binary = 0010 (1's complement)
"""


def convert_to_1sComplement(binary_num: str):
    ones_complement = ''
    for digit in binary_num:
        if digit == '1':
            ones_complement += '0'
        if digit == '0':
            ones_complement += '1'

    return ones_complement


if __name__ == "__main__":
    print(convert_to_1sComplement('1101'))
