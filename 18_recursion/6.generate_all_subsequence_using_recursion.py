"""
Author : janarddan
File_name = 6.generate_all_subsequence_using_recursion.py
Date : 27/07/26
Description :
Given an array arr[]. The task is to find all the possible subsequences of the given array using recursion.

Examples:

Input: arr[] = [1, 2, 3]
Output : [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3], []

Input: arr[] = [1, 2]
Output : [2], [1], [1, 2], []

Approach:

For every element in the array, there are two choices, either to include it in the subsequence or not include it.
Apply this for every element in the array starting from index 0 until we reach the last index.
Print the subsequence once the last index is reached.

-------------------------------------------------------------------------------------------------
Subset vs Subsequence
---------------------

Although these terms are often used interchangeably in coding interviews,
they are conceptually different.

1. Subset
   - Derived from Set Theory.
   - A subset is any collection of elements chosen from a set.
   - Order does NOT matter.
   - Sets do NOT allow duplicate elements.

   Example:
       Set = {1, 2, 3}

       Subsets:
       {}
       {1}
       {2}
       {3}
       {1, 2}
       {1, 3}
       {2, 3}
       {1, 2, 3}

2. Subsequence
   - Derived from a sequence (array/string).
   - A subsequence is formed by selecting elements while preserving their
     original relative order.
   - Elements can be skipped, but their order cannot be changed.
   - Duplicate elements are allowed because arrays can contain duplicates.

   Example:
       Array = [1, 2, 3]

       Valid Subsequences:
       []
       [1]
       [2]
       [3]
       [1, 2]
       [1, 3]
       [2, 3]
       [1, 2, 3]

       Invalid:
       [3, 1]   # Order changed

Key Difference
--------------
Subset:
    - Order is irrelevant.
    - Based on mathematical sets.

Subsequence:
    - Relative order must be preserved.
    - Based on arrays/strings.

Interview Note
--------------
For arrays containing DISTINCT elements, generating all subsets and generating
all subsequences produce the SAME collection of results.

Example:
    Array = [1, 2, 3]

    Generated Results:
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    [2, 3]
    [1, 2, 3]

Hence, many coding interview problems use the terms "subset" and
"subsequence" interchangeably. The recursive solution is identical:

    At every index, make two choices:
        1. Include the current element.
        2. Exclude the current element.

This generates all 2^n possible combinations.
"""

from typing import List


def generate_subsequence(arr, curr_idx, subseq:List, res:List):
    if curr_idx == len(arr):
        res.append(subseq.copy())
        return

    # Include the current element
    subseq.append(arr[curr_idx])

    # Recurse to the next element
    generate_subsequence(arr, curr_idx+1, subseq, res)

    # Backtrack - remove the current element and explore next
    subseq.pop()

    generate_subsequence(arr, curr_idx+1, subseq, res)


if __name__ == "__main__":
    arr = [1,2,3]
    subseq = []
    res = []
    generate_subsequence(arr, 0, subseq, res)

    print(res)
