"""
Author : Janarddan Sarkar
File_name = pointer.py
Date : 20-12-2023
Description :  
"""
num1 = 11
num2 = num1

print(id(num1))   # address of num1
print(id(num2))   # address of num2

num2 = 22
print(id(num1), id(num2))
