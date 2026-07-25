"""
Author : Janarddan Sarkar
file_name : pattern_test.py 
date : 19-02-2024
description : 
"""


def pattern(n_row):
  for i in range(n_row):
    # increasing triangle of *
    for j in range(i + 1):
      print("*", end='  ')

    # decreasing triangle of space
    for k in range(i, n_row - 1):
      print(" ", end='  ')

    # increasing triangle of *
    for m in range(i + 1):
      if m != n_row - 1:
        print("*", end='  ')

    print()


pattern(5)


