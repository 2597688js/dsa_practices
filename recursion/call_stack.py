"""
Author : Janarddan Sarkar
File_name = call_stack.py
Date : 23-02-2024
Description :  
"""


def funcThree():
    print("Three")


def funcTwo():
    funcThree()
    print("Two")


def funcOne():
    funcTwo()
    print("One")


if __name__ == "__main__":
    funcOne()
