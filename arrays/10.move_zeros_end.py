"""
Author : Janarddan Sarkar
File_name = 10.move_zeros_end.py
Date : 29-02-2024
Description :  move the zeros in an array to the end.

Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the
end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input: [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
Output: [1 ,2 ,3 ,4 ,1 ,0 ,0 ,0]
Explanation: All the zeros are moved to the end and non-negative integers are moved to
            front by maintaining order

"""

# 1.Bruteforce
"""
Brute Force Approach:  The extremely naive solution, we can think of, involves the use of an extra array. The algorithm is as follows.

Algorithm:
    1. Suppose, there are N-X zeros and X non-zero elements in the array. We will first copy those X non-zero elements from the original array to a 
        temporary array. 
    2. Then, we will copy the elements from the temporary array one by one and fill the first X places of the original array. 
    3. The last N-X places of the original array will be then filled with zero. Now, our task is completed.
    
Complexity Analysis
    1. Time Complexity: O(N) + O(X) + O(N-X) ~ O(2*N), where N = total no. of elements,
        X = no. of non-zero elements, and N-X = total no. of zeros.
    Reason: O(N) for copying non-zero elements from the original to the temporary array. O(X) for again copying it back from the temporary to the original array. O(N-X) for filling zeros in the original array. So, the total time complexity will be O(2*N).

    2. Space Complexity: O(N), as we are using a temporary array to solve this problem and the maximum size of the array can be N in 
        the worst case.
    Reason: The temporary array stores the non-zero elements. In the worst case, all the given array elements will be non-zero.
"""


def moveZerosEnd_bruteforce(arr):
    temp_arr = list()  # array to store all the non-zero elements
    for x in arr:
        if x != 0:
            temp_arr.append(x)

    # Now move the elements from the temp_arr to the main array
    for i in range(len(temp_arr)):
        arr[i] = temp_arr[i]

    for j in range(len(temp_arr), len(arr)):
        arr[j] = 0

    return arr


# 2. Optimal
"""
Optimal Approach(Using 2 pointers): 
    We can optimize the approach using 2 pointers i.e. i and j. The pointer j will point to the first 0 in the array and i will point
    to the next index.

    Assume, the given array is {1, 0, 2, 3, 2, 0, 0, 4, 5, 1}. Now, initially, we will place the 2-pointers like the following:
        j = 1, i = 2

The algorithm will be the following.
    1. First, using a loop, we will place the pointer j. If we don’t find any 0, we will not perform the following steps.
    2. After that, we will point i to index j+1 and start moving the pointer using a loop.
    3. While moving the pointer i, we will do the following:
        3.1) If a[i] != 0 i.e. a[i] is a non-zero element: We will swap a[i] and a[j]. Now, the current j is pointing to the non-zero 
          element a[i]. So, we will shift the pointer j by 1 so that it can again point to the first zero.
    4. Finally, our array will be set in the right manner.
    
Complexity Analysis
    Time Complexity: O(N), N = size of the array.
        Reason: We have used 2 loops and using those loops, we are basically traversing the array once.

    Space Complexity: O(1) as we are not using any extra space to solve this problem.
"""


def moveZerosEnd_optimal(arr):
    j = -1
    for k in range(len(arr)):
        if arr[k] == 0:
            j = k
            break

    i = j + 1

    for m in range(i, len(arr)):
        if arr[m] != 0:
            temp = arr[m]
            arr[m] = arr[j]
            arr[j] = temp

            j += 1
            i += 1

    return arr


if __name__ == "__main__":
    print(moveZerosEnd_bruteforce([1, 0, 2, 3, 0, 4, 0, 1]))
    print()
    print(moveZerosEnd_optimal([1, 0, 2, 3, 0, 4, 0, 1]))
