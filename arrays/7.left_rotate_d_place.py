"""
Author : Janarddan Sarkar
File_name = 7.left_rotate_d_place.py
Date : 29-02-2024
Description :   Given an array of N integers and an integer D, left rotate the array by D place.

Example 1:
    Input: N = 7, array[] = {1,2,3,4,5,6,7} , d = 3
    Output: 4 5 6 7 1 2 3
    Explanation: The array is rotated to the left by 3 positions.

Example 2:
    Input: N = 6, array[] = {3,7,8,9,10,11} , d = 2
    Output: 8 9 10 11 3 7
    Explanation: The array is rotated to the left by 2 positions.
"""

# 1. Bruteforce approach
"""
Brute Force Approach: 
The steps are as follows:
    1. First, we will perform (d%n) to get the effective number of rotations.
    2. We will store the first d elements in a temporary array.
    3. We will shift the last (n-d) elements by d places to the left using a loop(say i) that will start from 
       index d and run up to index n-1 (in case of 0-based indexing). Inside the loop, 
       the shifting will be like: arr[i-d] = arr[i].
    4. After that, we will place the elements of the temporary array in the last d places of the given array 
       using another loop that starts from (n-d) and runs up to n-1 (0-based index).
        4.1. While selecting elements from the temporary array, one of the ways is to use a 
        variable(say j and starts from 0) and increment it inside the loop.
        4.2. The efficient way will be the following. The element at index i in the temporary array will be placed 
       at index (n-d+i) in the given array. So, to place the elements in the correct position, inside the loop,
        we will do this: arr[i] = temp[i-(n-d)].
"""

# 3. Optimal approach
"""
Optimized Approach(without using any extra space): Using “Reversal Algorithm” This is a straightforward method.
The steps are as follows:
    Step 1: Reverse the subarray with the first d elements (reverse(arr, arr+d)).
    Step 2: Reverse the subarray with the last (n-d) elements (reverse(arr+d, arr+n)).
    Step 3: Finally reverse the whole array (reverse(arr, arr+n)).
    
Time Complexity: O(d)+O(n-d)+O(n) = O(2*n), where n = size of the array, d = the number of rotations. 
                  Each term corresponds to each reversal step.
Space Complexity: O(1) since no extra space is required.
"""


def leftRotate_d_place_brutefore(arr, d):
    pass


def leftRotate_d_place_optimal(arr, d):

    def reverseGivenIndex(arr, strt_idx, end_idx):
        n = (end_idx - strt_idx) + 1  # size of the subarray arr[strt_idx:end_idx]

        for i in range(n // 2):
            temp = arr[strt_idx + i]
            arr[strt_idx + i] = arr[end_idx - i]
            arr[end_idx - i] = temp

        return arr

    n = len(arr)

    d = d % n

    # step 1 - reverse first d elemenets in the  array
    reverseGivenIndex(arr, 0, d-1)

    # step 2 - reverse the remaining (n- d) elements in the array
    reverseGivenIndex(arr, d, n-1)

    # step 3 - reverse the whole array
    reverseGivenIndex(arr, 0, n-1)

    return arr


if __name__ == "__main__":
    print(leftRotate_d_place_optimal([1, 2, 3, 4, 5, 6], 2))
    print(leftRotate_d_place_optimal([1, 2, 3, 4, 5, 6], 3))


