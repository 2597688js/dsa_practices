"""
Author : Janarddan Sarkar
File_name = decreasing_traingle_pattern.py
Date : 19-02-2024
Description :  *  *  *  *  *
               *  *  *  *
               *  *  *
               *  *
               *

"""


def print_decreasing_triangle_pattern(n_row):
    for i in range(n_row):
        for j in range(i, n_row):
            print("*", end="  ")

        print()


if __name__ == "__main__":
    print_decreasing_triangle_pattern(5)

