"""
Author : Janarddan Sarkar
File_name = 6.left_rotate_1_place.py
Date : 29-02-2024
Description :   Given an array of N integers, left rotate the array by one place.

Example 1:
    Input: N = 5, array[] = {1,2,3,4,5}
    Output: 2,3,4,5,1
    Explanation:
        Since all the elements in array will be shifted toward left by one so ‘2’ will now become the
        first index and and ‘1’ which was present at first index will be shifted at last.

Example 2:
    Input: N = 1, array[] = {3}
    Output: 3
    Explanation: Here only element is present and so the element at first index will be shifted to
                last index which is also by the way the first index.
"""

# 1. Bruteforce
"""
Solution 1: Brute force Approach
Intuition:
The rotated array has just a difference that its first element is present at the last index of the array. 
So if we can just store the element at the first index and then shift all the elements towards the left
 and at last put the stored element at the last index. We will get th rotated array.

Approach:
We can take another dummy array of the same length and then shift all elements in the array toward the left and 
then at the last element store the index of 0th index of the array and print it.
"""


def leftRotateOnePlaceBruteforce(arr):
    n = len(arr)
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
    print()


# 3. Optimal
"""
Approach: 
Here, in the given array :

n = 5,
arr[] = {1,2,3,4,5}
At first, we have to shift the array towards the left so, we store the value of the first index in a variable
 (let it be x).

Then we iterate the array from the 0th index to the n-1th index.

And then store the value present in the next index to the current index like this :

arr[i] = arr[i+1]
And to prevent its segmentation fault we will iterate it till n-1.

At last, put the value of variable x in the last index of the array.
"""


def leftRotateOnePlace(arr):
    n = len(arr)

    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = temp

    return arr


if __name__ == "__main__":
    print(leftRotateOnePlace([1, 2, 3, 4, 5]))
