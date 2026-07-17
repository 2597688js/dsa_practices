"""
Author : janarddan
File_name = 6. Fruit Into Baskets.py
Date : 17/07/26
Description :
(LeetCode 904)

Problem

You are given an integer array fruits where each element represents a type of fruit.

You have 2 baskets, and each basket can hold only one type of fruit, but an unlimited quantity of that type.

Starting from any tree, pick exactly one fruit from each tree while moving to the right. You must stop when you encounter a fruit that doesn't fit into your two baskets.

Return the maximum number of fruits you can collect.

Example 1
Input:
fruits = [1,2,1]

Output:
3

Explanation:
Basket 1 -> 1
Basket 2 -> 2

Collect all fruits.
Example 2
Input:
fruits = [0,1,2,2]

Output:
3

Explanation:
Collect [1,2,2]
Example 3
Input:
fruits = [1,2,3,2,2]

Output:
4

Explanation:
Collect [2,3,2,2]
"""
fruits = [1,2,3,2,2]

def fruitIntoBaskets(fruits):
    maxi = 0
    count = {}
    left = 0

    for right in range(len(fruits)):
        if fruits[right] in count:
            count[fruits[right]] += 1
        else:
            count[fruits[right]] = 1



        while len(count) > 2:

            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        curr_window_size = right - left + 1  # This is the maximum number of fruits that can be collected.
        maxi = max(maxi, curr_window_size)

    return maxi

if __name__ == "__main__":
    print(fruitIntoBaskets([1,2,3,2,2]))
    print(fruitIntoBaskets([1,2,3,4,5]))
    print(fruitIntoBaskets([3,3,3,1,2,1,1,2,3,3,4]))

