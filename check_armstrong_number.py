"""
Author : Janarddan Sarkar
file_name : check_amstrong_number.py 
date : 25-02-2024
description : 
"""


def get_order(num):
    """
    function to get the order i.e., the number of digit in the number. Ex, order of 123 is 3, order of 1234 is 4
    """

    order = 0
    while num > 0:
        num //= 10   # num = num // 10
        order += 1

    return order


def isArmstorng(num):
    """
    example, 153. order of 153 is 3. And, 1^3 + 5^3 + 3^3 = 153
    1634. order of 1634 is 4. And, 1^4 + 6^4 + 3^4 + 4^4 = 1634
    """
    order = get_order(num)
    original_num = num
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + (digit**order)
        num = num // 10

    if sum == original_num:
        return True
    else:
        return False


print(isArmstorng(153))
print(isArmstorng(370))
print(isArmstorng(371))
print(isArmstorng(407))
print(isArmstorng(1634))
print(isArmstorng(8208))
print(isArmstorng(9407))
print(isArmstorng(100))
print(isArmstorng(9999))
