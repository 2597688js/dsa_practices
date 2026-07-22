"""
Author : Janarddan Sarkar
File_name = 3. check_if_sorted.py
Date : 28-02-2024
Description :  check if a given array is sorted.

Example 1:
input : [1, 2, 3, 4, 5]  output: True

Example 2:
input: [1, 4, 2, 8, 5]  output: False

There is no Bruteforce, better, optimal approach for this problem. Its a straight forward approach. Just traverse
the array and check if the previous element is smaller than the current one, if it finds atleast one element
which is not greater than the previous element, the array is not sorted.

"""


# 1. Bruteforce approach
"""
1. The idea is pretty simple here, We will start with the element at the 0th index, and will compare it with 
   all of its future elements that are present in the array.
2. If the picked element is smaller than or equal to all of its future values then we will move to the next 
   Index/element until the whole array is traversed.
3. If any of the picked elements is greater than its future elements, Then simply we will return False.
4. If the size of the array is Zero or One i.e ( N = 0 or N = 1 ) or the entire array is
   traversed successfully then we will simply return True.
   
Complexity Analysis for Bruteforce :
    Time Complexity: O(N^2)
    Space Complexity: O(1), because we are not using any other space, its a constant space. 
"""

# 2. Better solution
# No better solution

# 3. Optimal solution
"""
1. We will check every element with its previous element if the previous element is smaller than or equal 
   to the current element then we will move to the next index.
2. If the whole array is traversed successfully or the size of the given array is zero or one 
(i.e N = 0 or N = 1). Then we will return True else return False.

Complexity Analysis for Optimal solution:
    Time Complexity: O(N)
    Space Complexity: O(1)
"""


def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


if __name__ == "__main__":
    print(isSorted([1, 2, 3, 4, 5]))
    print(isSorted([1, 2, 7, 4, 5]))
