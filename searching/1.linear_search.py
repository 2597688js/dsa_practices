"""
Author : Janarddan Sarkar
file_name : 1.linear_search.py 
date : 24-03-2024
description :

Time Complexity:
    Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
    Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list.
                So the worst-case complexity is O(N) where N is the size of the list.
    Average Case: O(N)

Space Complexity: O(1) as except for the variable to iterate through the list, no other variable is used.
"""
# Python3 code to linearly search x in arr[].


def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
