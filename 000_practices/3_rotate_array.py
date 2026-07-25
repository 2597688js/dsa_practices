"""
Author : Janarddan Sarkar
file_name : 3_rotate_array.py 
date : 12-09-2025
description :
Rotate Array Problem (Right Rotation by k steps)

Logic (Reversal Algorithm):
1. Normalize k:
   - If k >= n, then rotating by k is same as rotating by k % n.
   - Example: rotating by n or 2n gives the same array.

2. Idea:
   - Array can be divided into two parts:
       A = first (n-k) elements
       B = last k elements
   - Right rotation means: [A | B] → [B | A]

3. Reversal Trick:
   - Step 1: Reverse the entire array → [A | B] becomes [Bᵣ | Aᵣ]
   - Step 2: Reverse the first k elements (Bᵣ → B)
   - Step 3: Reverse the remaining n-k elements (Aᵣ → A)
   - Final result = [B | A] (desired rotated array)

Example:
arr = [1, 2, 3, 4, 5, 6, 7], k = 3
Step 1: reverse whole → [7, 6, 5, 4, 3, 2, 1]
Step 2: reverse first k → [5, 6, 7, 4, 3, 2, 1]
Step 3: reverse last n-k → [5, 6, 7, 1, 2, 3, 4]
Result = rotated array

"""

def rotate_arr(lst, k):
    n = len(lst)
    k = k % n

    def reverse_arr(arr, start_idx, end_idx):
        while start_idx < end_idx:
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]

            start_idx += 1
            end_idx -= 1

    # Step 1: Reverse whole array
    reverse_arr(lst, 0, n-1)
    # Step 2: Reverse first k elements
    reverse_arr(lst, 0, k-1)
    # Step 3: Reverse remaining n-k elements
    reverse_arr(lst, k, n-1)
    return lst

if __name__ == "__main__":
    print(rotate_arr([1, 2, 3, 4, 5], 3))


