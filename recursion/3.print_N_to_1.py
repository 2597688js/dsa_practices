"""
Author : Janarddan Sarkar
File_name = 3.print_N_to_1.py
Date : 28-02-2024
Description : print from N to 1 using recursion
"""


def print_N_1(n):
    if n < 1:
        return

    print(n)
    print_N_1(n-1)


if __name__ == "__main__":
    print_N_1(n=3)
