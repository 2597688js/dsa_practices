"""
Author : Janarddan Sarkar
File_name = 1. find_largest_element.py
Date : 27-02-2024
Description :  find the largest element in an array.

Note: we should approach a problem in 3 ways, first by bruteforce approach i.e., the naive approach that comes
to our mind. Then go for a better approach and then go for the optimal solution.

1. Bruteforce
2. Better
3. Optimal

Sometimes, the better solution might not exist.

"""


# 1. Bruteforce approach
# Sort the array and then return the last element. Time complexity in this approach will be
# O(n logn) [for sorting] + O(1) [for arr[n-1] the last element after sorting] =~ O(n logn)

# 2. Better solution
# This problem does not have any better solution

# 3. Optimal solution
def find_largest(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    return largest


"""
Time complexity is O(n) (Big O of n), since we traversing the array for n elements.
"""

if __name__ == "__main__":
    lst = [1, 3, 2, 5, 7, 7, 6]
    print(find_largest(lst))
