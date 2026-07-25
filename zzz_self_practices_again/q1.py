"""
Author : Janarddan Sarkar
file_name : q1.py 
date : 16-06-2023
description : Given an array A[] of n numbers and another number x, the task is to check whether or not there exist
two elements in A[] whose sum is exactly x. Get all such pairs

Input: arr[] = {0, -1, 2, -3, 1}, x= -2
Output: Yes
Explanation:  If we calculate the sum of the output,1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}, x = 0
Output: No
"""


def printPairs(arr, sum):
    arr_size = len(arr)
    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {}

    res_arr = []

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if temp in hashmap:
            print('Yes')
            res_arr.append((temp, arr[i]))
        hashmap[arr[i]] = i

    return res_arr


if __name__ == "__main__":
    A = [1, 4, 45, 6, 12, 10, 8]
    n = 16
    ret = printPairs(A, n)
    print(ret)

    B = [3, 34, 4, 12, 5, 2]
    sum = 9
    ret1 = printPairs(B, sum)
    print(ret1)
