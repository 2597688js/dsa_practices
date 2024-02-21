"""
Author : Janarddan Sarkar
File_name = pattern2.py
Date : 19-02-2024
Description :  *  *  *  *  *
                  *  *  *  *
                     *  *  *
                        *  *
                           *

first part is a increasing triangle pattern with space and
other part is a decreasing triangle pattern with *
"""


def pattern2(n_row):
    for i in range(n_row):
        # increasing triangle pattern of *
        for k in range(i + 1):
            print(" ", end=" ")

        # decreasing triangle pattern of space
        for j in range(i, n_row):
            print("*", end=" ")

        print()


if __name__ == "__main__":
    pattern2(5)

