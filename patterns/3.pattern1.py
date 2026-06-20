"""
Author : Janarddan Sarkar
File_name = pattern1.py
Date : 19-02-2024
Description :           *
                      * *
                    * * *
                  * * * *
                * * * * *

Here, we can imagine that there is a sqaure, where first part is a decreasing triangle pattern with space and
other part is a increasing triangle pattern with *
"""

def pattern1(n_row):
    for i in range(n_row):
        # decreasing triangle pattern of space
        for j in range(i, n_row):
            print(" ", end=" ")

        # increasing triangle pattern of *
        for k in range(i + 1):
            print("*", end=" ")

        print()


if __name__ == "__main__":
    pattern1(5)


