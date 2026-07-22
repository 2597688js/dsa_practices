"""
Author : Janarddan Sarkar
file_name : 20.check_if_power.py 
date : 04-07-2024
description : Find if number is represented by power of some other number
n = 27, is 27 = a **b, where a and b are integers
"""
import math

def is_power(n):
    if n <= 1:
        return False

    for a in range(2, int(math.sqrt(n)) + 1):
        b = 2
        while (a ** b) < n:
            b += 1
            if (a**b) == n:
                return True, a, b
    return False, None, None


if __name__ == "__main__":
    print(is_power(27))
    print(is_power(10))

