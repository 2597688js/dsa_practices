"""
Author : janarddan
File_name = 0.1_break_continue.py
Date : 22/07/26
Description :

"""

for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            break

    print(i, j, end=" ")
    print()
