"""
Author : Janarddan Sarkar
File_name = 11.reverse_array.py
Date : 29-02-2024
Description :  given an array, reverse the array
"""

# 1. Bruteforce approach
"""
beleg eta temp_arr bonai tat main array tur element bur lastt r pora append kori jam. 
In this approach, we will need an extra space of size N. 
Time complexity O(n)
Space complexity O(n)
"""


def reverseArrayBruteforce(arr):
    n = len(arr)
    temp_arr = [0]*n
    for i in range(n):
        temp_arr[i] = arr[n-(i+1)]

    return temp_arr


# 3. Optimal approach
"""
Time complexity : O(n)
space complexity : O(n) [space of the already available array] + O(1) [No extra space is used i.e, constant space]
{
we have used temp variable, but that space is negligible.
}
"""


def reverseArrayOptimal(arr):
    n = len(arr)

    for i in range((n//2)):
        temp = arr[i]
        arr[i] = arr[n-(i+1)]
        arr[n-(i+1)] = temp

    return arr


if __name__ == "__main__":
    print(reverseArrayBruteforce([1, 2, 3, 4, 6, 5]))
    print(reverseArrayBruteforce([11, 22, 33, 44, 55]))
    print()

    print(reverseArrayOptimal([1, 2, 3, 4, 6, 5]))
    print(reverseArrayOptimal([11, 22, 33, 44, 55]))

