"""
Author : Janarddan Sarkar
File_name = increasing_triangle_pattern.py
Date : 19-02-2024
Description :   *
                *  *
                *  *  *
                *  *  *  *
                *  *  *  *  *
"""


def print_increasing_triangle_pattern(n_row):
    for i in range(n_row):
        for j in range(i+1):
            print("*", end="  ")

        print()


if __name__ == "__main__":
    print_increasing_triangle_pattern(5)
