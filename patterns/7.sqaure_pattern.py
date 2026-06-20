"""
Author : Janarddan Sarkar
File_name = sqaure_pattern.py
Date : 19-02-2024
Description :  *  *  *  *  *
               *  *  *  *  *
               *  *  *  *  *
               *  *  *  *  *
               *  *  *  *  *
"""


def print_sqaure_pattern(n_row, n_col):
    for i in range(n_row):
        for j in range(n_col):
            print("*", end="  ")

        print()


if __name__ == "__main__":
    print_sqaure_pattern(5, 5)
