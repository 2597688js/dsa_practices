"""
Author : Janarddan Sarkar
File_name = 2.print_1_to_N.py
Date : 28-02-2024
Description :  print from 1 to N using recursion
"""


def print_1_n(n):
    if n > 1:
        print_1_n(n-1)
    print(n)


if __name__ == "__main__":
    print_1_n(3)
