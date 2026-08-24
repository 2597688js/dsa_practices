"""
Author : janarddan
File_name = 24.reverse_array.py
Date : 07/08/26
Description :

Time Complexity
The loop runs approximately n/2 times.
Big-O ignores constant factors.

Therefore:

Time Complexity: O(n)
Space Complexity: O(1) (in-place, only i and j are used)

"""

def reverse_array(arr):
    n = len(arr)

    i = 0
    j = n-1
    while i<=j:
        arr[j], arr[i] = arr[i], arr[j]
        i += 1
        j -= 1

    return arr

if __name__ == "__main__":
    print(reverse_array([1,2,3,4,5,6]))
    print(reverse_array([1,2,3,4,5]))