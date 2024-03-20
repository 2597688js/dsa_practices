"""
Author : Janarddan Sarkar
file_name : 4.bitwise_operators.py 
date : 20-03-2024
description : Bitwise operators are: AND (&) , OR (|), NOT(~), XOR(^), left shift(<<), right shift(>>)
"""

# AND
print(f"{5} AND {5} : ", 5 & 5)
print(f"{5} AND {4} : ", 5 & 4)
print()

# OR
print(f"{5} OR {5} : ", 5 | 5)
print(f"{5} OR {4} : ", 5 | 4)
print()

# NOT
print(f" NOT {5} : ", ~5)
print(f" NOT {-6} : ", ~(-6))
print(f" NOT {8} : ", ~8)
print(f" NOT {10} : ", ~10)
print(f" NOT {32} : ", ~32)
print(f" NOT {12} : ", ~12)
print(f" NOT {-33} : ", ~-33)
print()

# XOR
"""
XOR properties :
    1. XOR is odd one detector i.e., if number of 1s is odd then XOR is 1, otherwise 0
    2. XOR of two same number is 0
    3. XOR of any number with 0 is the number itself.
"""
print(f"{5} XOR {5} : ", 5 ^ 5)
print(f"{5} XOR {0} : ", 5 ^ 0)
print(f"{5} XOR {4} : ", 5 ^ 4)
print()

# Left shift
print("13 << 1 : ", 13 << 1)    # 13 * (2 ^ 1) = 26
print(f"13 << 2 : ", 13 << 2)    # 13 * (2^2) = 52
print()

# Right shift
print("13 >> 1 : ", 13 >> 1)    # 13 // (2 ^ 1) = 6
print(f"13 >> 2 : ", 13 >> 2)    # 13 // (2^2) = 3
