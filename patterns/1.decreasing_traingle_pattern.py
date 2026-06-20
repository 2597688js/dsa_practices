"""
Author : Janarddan Sarkar
File_name = decreasing_traingle_pattern.py
Date : 19-02-2024
Description :  pattern1:

               *  *  *  *  *
               *  *  *  *
               *  *  *
               *  *
               *

               pattern2:
               * * * * *
                 * * * *
                   * * *
                     * *
                       *



"""


def print_decreasing_triangle_pattern1(n_row):
    for i in range(n_row):
        for j in range(i, n_row):
            print("*", end="  ")

        print()

def print_decreasing_triangle_pattern2(n_row):
    for i in range(n_row):
        for j in range(i):
            print(" ", end="  ")

        # NOTE: the * loop is exactly same as above
        for j in range(i, n_row):
            print("*", end="  ")

        print()


if __name__ == "__main__":
    print_decreasing_triangle_pattern1(5)
    print_decreasing_triangle_pattern2(5)

