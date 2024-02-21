"""
Author : Janarddan Sarkar
File_name = code_any.py
Date : 28-11-2023
Description :  
"""

x = 42
y = x
z = 44
print(id(x))
print(id(y)) # (same as x)
print(id(z)) # (same as x and y)