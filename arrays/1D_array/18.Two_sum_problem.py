"""
Author : Janarddan Sarkar
file_name : 18.Two_sum_problem.py 
date : 24-03-2024
description :
Two Sum : Check if a pair with given sum exists in Array
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3,
then nums[1] + nums[1] = target is not a solution.

Example 1:
    Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
    Result: YES (for 1st variant)
           [1, 3] (for 2nd variant)
    Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
    Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
    Result: NO (for 1st variant)
        [-1, -1] (for 2nd variant)
    Explanation: There exist no such two numbers whose sum is equal to the target.
"""

# Bruteforce
"""
Naive Approach(Brute-force approach): 
    Intuition: For each element of the given array, we will try to search for another element such that its sum is equal to the target.
                If such two numbers exist, we will return the indices or “YES” accordingly.

Approach:
    First, we will use a loop(say i) to select the indices of the array one by one.
    For every index i, we will traverse through the remaining array using another loop(say j) to find the other number such that the sum
    is equal to the target (i.e. arr[i] + arr[j] = target).
    
Time Complexity: O(N*N), where N = size of the array.
    Reason: There are two loops(i.e. nested) each running for approximately N times.

Space Complexity: O(1) as we are not using any extra space.
"""
def two_sum_bruteforce(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == target:
                return 'YES', i, j      #  arr[i] + arr[j] = target(14)

    return 'NO'


# 2. Better
"""
Better Approach(using Hashing): 

Intuition: Basically, in the previous approach we selected one element and then searched for the other one using a loop. 
Here instead of using a loop, we will use the HashMap to check if the other element i.e. target-(selected element) exists. 
Thus we can trim down the time complexity of the problem.

Approach:

The steps are as follows:
1. We will select the element of the array one by one using a loop(say i).
2. Then we will check if the other required element(i.e. target-arr[i]) exists in the hashMap.
    2.1 If that element exists, then we will return “YES” for the first variant or we will return the current index i.e. i, and 
    the index of the element found using map i.e. mp[target-arr[i]].
    2.2 If that element does not exist, then we will just store the current element in the hashMap along with its index.
     Because in the future, the current element might be a part of our answer.
3. Finally, if we are out of the loop, that means there is no such pair whose sum is equal to the target. In this case, 
   we will return either “NO” or {-1, -1} as per the variant of the question.\
   
Time Complexity: O(N), where N = size of the array.
    Reason: The loop runs N times in the worst case and searching in a hashmap takes O(1) generally. So the time complexity is O(N).
    
Space Complexity: O(N) as we use one dictionary data structure to store.
"""
def two_sum_better(arr, target):
    hash_dict = {}

    for i in range(len(arr)):
        if (target - arr[i]) not in hash_dict:
            hash_dict[arr[i]] = i
        else:
            return "YES", hash_dict[target - arr[i]], i

    return "NO"


# 3. Optimal - using 2 pointer approach - this will not use any space (in the better approach - it was O(n))
"""
Optimized Approach(using two-pointer): 

Intuition: In this approach, we will first sort the array and will try to choose the numbers in a greedy way.

We will keep a left pointer at the first index and a right pointer at the last index. Now until left < right, we will check the
sum of arr[left] and arr[right]. Now if the sum < target, we need bigger numbers and so we will increment the left pointer. 
But if sum > target, we need to consider lesser numbers and so we will decrement the right pointer. 
If sum == target we will return either “YES” or the indices as per the question.
But if the left crosses the right pointer, we will return “NO” or {-1, -1}.

Approach:
The steps are the following:
1. We will sort the given array first.
2. Now, we will take two pointers i.e. left, which points to the first index, and right, which points to the last index.
3. Now using a loop we will check the sum of arr[left] and arr[right] until left < right.
    3.1. If arr[left] + arr[right] > sum, we will decrement the right pointer.
    3.2 If arr[left] + arr[right] < sum, we will increment the left pointer.
    3.3 If arr[left] + arr[right] == sum, we will return the result.
4. Finally, if no results are found we will return “No” or {-1, -1}.

Time Complexity: O(N) + O(N*logN), where N = size of the array.
    Reason: The loop will run at most N times. And sorting the array will take N*logN time complexity.

Space Complexity: O(1) as we are not using any extra space. 
                  🤞Note: Here we are distorting the given array. So, if we need to consider this change, 
                          the space complexity will be O(N).
"""
def two_sum_optimal(arr, target):
    left, right = 0, len(arr) - 1

    arr = sorted(arr)
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return "YES", left, right
        elif curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1

    return "NO"


if __name__ == "__main__":
    print("Bruteforce : ", two_sum_bruteforce([2, 6, 5, 8, 11], 14))
    print("Bruteforce : ", two_sum_bruteforce([2, 6, 5, 8, 11], 23))
    print()
    print("Better : ", two_sum_better([2, 6, 5, 8, 11], 14))
    print("Better : ", two_sum_better([2, 6, 5, 8, 11], 23))
    print()
    print("Optimal : ", two_sum_optimal([2, 6, 5, 8, 11], 14))
    print("Optimal : ", two_sum_optimal([2, 6, 5, 8, 11], 23))
