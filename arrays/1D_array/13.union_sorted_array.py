"""
Author : Janarddan Sarkar
file_name : 13.union_sorted_array.py 
date : 10-03-2024
description :
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.
NOTE: Elements in the union should be in ascending order.

Example 1:
    Input:
        n = 5,m = 5.
        arr1[] = {1,2,3,4,5}
        arr2[] = {2,3,4,4,5}
    Output:
        {1,2,3,4,5}

    Explanation:
        Common Elements in arr1 and arr2  are:  2,3,4,5
        Distnict Elements in arr1 are : 1
        Distnict Elemennts in arr2 are : No distinct elements.
        Union of arr1 and arr2 is {1,2,3,4,5}
 ---------------------------------------------------------------------------------------------------

Example 2:
    Input:
        n = 10,m = 7.
        arr1[] = {1,2,3,4,5,6,7,8,9,10}
        arr2[] = {2,3,4,4,5,11,12}
    Output:
        {1,2,3,4,5,6,7,8,9,10,11,12}

    Explanation:
        Common Elements in arr1 and arr2  are:  2,3,4,5
        Distnict Elements in arr1 are : 1,6,7,8,9,10
        Distnict Elemennts in arr2 are : 11,12
        Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}
"""


# 1.Bruteforce
"""
Approach : Eta list lua, the given array keitar karone iterate kori jodi element tu already union list t nathake, the 
           add kora.
           
Time complexity : O(m logm + n logn), where m -> size of arr1; n -> size of arr2. Because, if we use set (which we should
use ), it uses binary tree to insert elements and binary tree insertion is log n.
Space complexity : O(m + n), in worst case we will need the total of m + n space. 
"""
def unionOfSortedArrays_bruteforce(arr1, arr2):
    union_list = []

    for element in arr1:
        if element not in union_list:
            union_list.append(element)

    for element2 in arr2:
        if element2 not in union_list:
            union_list.append(element2)

    return union_list


if __name__ == "__main__":
    print(unionOfSortedArrays_bruteforce([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]))
    print(unionOfSortedArrays_bruteforce([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 4, 5, 11, 12]))
