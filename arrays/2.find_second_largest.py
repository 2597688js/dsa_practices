"""
Author : Janarddan Sarkar
File_name = 2.find_second_largest.py
Date : 27-02-2024
Description :  find the second largest element in an array

Example 1: input : [1, 3, 2, 5, 7, 7, 6]  output = 6
"""


# 1. Bruteforce
# sort the array and return the second last element, but this approach may not work if input array is like
# [1, 2, 4, 7, 7, 5], which after sorting becomes [1, 2, 4, 5, 7, 7] where arr[n-1](last element) = 7 is
# the largest and arr[n-1] (second last element) = 7, which is not second largest.
# if input is [1, 7, 7, 7, 7], we have to go back again and again like arr[n-2], arr[n-3] . . .untill we find
# an element lesser than the largest. so this is a worst case scenario.


# 2. Better
def find_second_largest(arr):
    def find_largest(arr):
        n = len(arr)
        largest = arr[0]
        for i in range(1, n):
            if arr[i] > largest:
                largest = arr[i]

        return largest

    largest = find_largest(arr)
    second_largest = arr[0]
    for i in range(len(arr)):
        if (arr[i] > second_largest) and (arr[i] < largest):
            second_largest = arr[i]

    return second_largest

"""
Time complexity :       O(n) to find the largest in the first pass
(find_second_largest)   O(n) to find the second largest in the second pass
                        So, O(2n) is the time complexity. 
"""


# 3. Optimal solution
def findSecondLargest(arr):
    largest = arr[0]
    second_largest = -99999

    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        else:
            if (arr[i] > second_largest) and (arr[i] != largest):
                second_largest = arr[i]

    return second_largest


if __name__ == "__main__":
    lst = [1, 3, 2, 5, 7, 7, 6]
    print(find_second_largest(lst))
    print(find_second_largest([1, 2, 4, 7, 7, 5]))
    print()

    print(findSecondLargest([1, 3, 2, 5, 7, 7, 6]))
    print(findSecondLargest([1, 2, 4, 7, 7, 5]))
