"""
Author : janarddan
File_name = 7.generate_subsequence_with_sum_k.py
Date : 27/07/26
Description :
Find all subsequences with sum equals to K
Last Updated : 4 Mar, 2025
Given an array arr[] of length n and a number k, the task is to find all the subsequences of the array with sum of its elements equal to k.

Note: A subsequence is a subset that can be derived from an array by removing zero or more elements, without changing the order of the remaining elements.

Examples:

Input: arr[] = [1, 2, 3], k = 3
Output: [ [1, 2], [3] ]
Explanation: All the subsequences of the given array are:
[ [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3], [] ]
Out of which only two subsequences have sum of their elements equal to 3.

Input: arr[] = [1, 2, 3], k = 7
Output: []
Explanation: Sum of all the elements of the array is 6, which is smaller than the required sum, thus they are no subsequences with sum of its elements equal to 7.

Input: arr[] = [17, 18, 6, 11, 2, 4], k = 6
Output: [ [2, 4], [6] ]
"""
