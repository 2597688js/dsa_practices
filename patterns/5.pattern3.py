"""
Author : Janarddan Sarkar
File_name = pattern3.py
Date : 21-02-2024
Description :                        *
                                   * * *
                                 * * * * *
                               * * * * * * *
                             * * * * * * * * *


                             # # # # *
                             # # # * * *
                             # # * * * * *
                             # * * * * * * *
                             * * * * * * * * *

   Here, there are three triangles : 1. decreasing triangle with space
                                     2. increasing triangle of *
                                     3. decreasing triangle of *
"""


def pattern3(n_row):
    for i in range(n_row):
        for j in range(i, n_row-1):
            print(" ", end=' ')

        for j in range(i + 1):
            print("*", end=' ')

        for j in range(i):
            print("*", end=' ')

        print()


if __name__ == "__main__":
    pattern3(5)

