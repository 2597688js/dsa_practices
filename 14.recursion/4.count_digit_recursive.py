"""
Author : janarddan
File_name = 4.count_digit_recursive.py
Date : 19/07/26
Description :
Each recursive call removes one digit, so you count 1 for each call.

"""
def count_digit(n):
    # Base case
    if n < 10:
        return 1

    return 1 + count_digit(n//10)


if __name__ == "__main__":
    print(count_digit(10))
    print(count_digit(9876))
    print(count_digit(123456))