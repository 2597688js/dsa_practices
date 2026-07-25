"""
Author : Janarddan Sarkar
file_name : check_palindrome.py 
date : 24-02-2024
description : To check if a given number is palindrome. ex:, 12321, 123454321 are palindrome. 123456 is not a palindrome.
"""


# This will only work for number, for string it will not work
def check_palindrome_number(n):
    temp_num = n
    reversed_num = 0

    while temp_num > 0:
        digit = temp_num % 10
        temp_num = temp_num // 10
        reversed_num = reversed_num * 10 + digit

    if reversed_num == n:
        return True
    else:
        return False


def check_palindrome_string_method1(strng):
    if strng[::-1] == strng:
        return True
    else:
        return False


def check_palindrome_string_method2(str):
    n = len(str)
    for i in range(0, n//2):
        if str[i] != str[n-(i+1)]:
            return False

    return True


if __name__ == "__main__":
    print(check_palindrome_number(123421))
    print(check_palindrome_number(123454321))
    print(check_palindrome_string_method1('ABCBAV'))
    print(check_palindrome_string_method2('ABCBA'))
