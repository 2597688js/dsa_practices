"""
Author : Janarddan Sarkar
file_name : 15.maximum_consecutive_ones.py 
date : 16-03-2024
description : Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Example 1:
    Input: prices = {1, 1, 0, 1, 1, 1}
    Output: 3
    Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Example 2:
    Input: prices = {1, 0, 1, 1, 0, 1}
    Output: 2
    Explanation: There are two consecutive 1's in the array.
"""

# No Bruteforce, Better and Optimal approach, It's a simple approach
"""
Approach: 
 1. We maintain a variable count that keeps a track of the number of consecutive 1’s while traversing the array. The other variable
 max_count maintains the maximum number of 1’s, in other words, it maintains the answer.

2. We start traversing from the beginning of the array. Since we can encounter either a 1 or 0 there can be two situations:-

3. If  the value at the current index is equal to 1 we increase the value of count by one. After updating  the count variable if it becomes 
more than the max_count  update the max_count.
4. If the value at the current index is equal to zero we make the variable count as 0 since there are no more consecutive ones.


Time Complexity: O(N) since the solution involves only a single pass.
Space Complexity: O(1) because no extra space is used.
"""
def count_maximum_consecutive_ones(arr):
    curr_sum = 0
    maxi = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            curr_sum += 1
        else:
            curr_sum = 0

        maxi = max(curr_sum, maxi)

    return maxi


if __name__ == "__main__":
    print(count_maximum_consecutive_ones([1, 1, 0, 1, 1, 1]))
    print(count_maximum_consecutive_ones([0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
