"""
Author : Janarddan Sarkar
File_name = factorial.py
Date : 23-02-2024
Description :  
"""


def find_factorial(n):
    if n == 1 :
        return 1
    return n*find_factorial(n-1)

if __name__ == "__main__":
    ans = find_factorial(5)
    print(ans)