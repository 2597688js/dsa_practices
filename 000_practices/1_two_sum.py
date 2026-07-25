"""
Author : Janarddan Sarkar
file_name : 1_two_sum.py 
date : 12-09-2025
description :
📝 Two Sum Problem (DSA)

📌 Problem Statement:
Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers such that they add up to `target`.

- Each input has exactly one solution.
- You cannot use the same element twice.
- Return the indices in any order.

✅ Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

"""

def two_sum1(lst, target):

    output = []

    for num in lst:
        idx1 = lst.index(num)
        remaining = target - num
        if remaining in lst:
            idx2 = lst.index(remaining)

        output.append([idx1, idx2])
        break

    return output

def two_sum2(lst, target):
    output = []

    for i in range(0, len(lst)):
        output.append(i)
        remaining = target - lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] == remaining:
                output.append(j)
        break

    return output

# best one
def two_sum3(lst, target):
    seen = {}

    for idx, num in enumerate(lst):
        remaining = target - num
        if remaining in seen:
            return [seen[remaining], idx]
        seen[num] = idx

    return []



if __name__ == "__main__":
    print(two_sum1([2, 7, 11, 15], 9))
    print(two_sum2([2, 7, 11, 15], 9))
    print(two_sum3([2, 17, 11, 15, 7], 9))







