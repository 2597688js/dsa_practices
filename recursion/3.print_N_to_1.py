"""
Author : Janarddan Sarkar
File_name = 3.print_N_to_1.py
Date : 28-02-2024
Description : print from N to 1 using recursion
"""


def print_N_1(i,n):
    if i < 1:
        return

    print(i)
    print_N_1(i-1, n)


if __name__ == "__main__":
    print_N_1(i=3, n=3)
