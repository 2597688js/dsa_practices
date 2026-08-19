"""
Author : janarddan
File_name = 9.power_sum.py
Date : 28/07/26
Description :

Given two integers `X` and `N`, determine the number of distinct ways to
represent `X` as the sum of the `N`th powers of **unique natural numbers**.

Each natural number can be used **at most once**. The order of the selected
numbers does **not** matter.

Examples:
---------
Example 1:
Input:
    X = 10
    N = 2

Explanation:
    We need to express 10 as the sum of unique squares.

    10 = 1² + 3²
       = 1 + 9

Output:
    1

------------------------------------------------------------

Example 2:
Input:
    X = 100
    N = 2

Explanation:
    The valid combinations are:

    100 = 10²
    100 = 6² + 8²
    100 = 1² + 3² + 4² + 5² + 7²

Output:
    3

------------------------------------------------------------

Example 3:
Input:
    X = 100
    N = 3

Explanation:
    The only valid combination is:

    100 = 1³ + 2³ + 3³ + 4³
        = 1 + 8 + 27 + 64

Output:
    1

Constraints:
------------
- X > 0
- N > 0
- Only unique natural numbers (1, 2, 3, ...) may be used.
- Each number can be selected at most once.

Approach:
---------
This problem can be solved using recursion/backtracking.

For each natural number `k` such that `k^N <= X`, we have two choices:
    1. Include `k` in the current combination.
    2. Exclude `k` and move to the next number.

The recursion explores all possible subsets while keeping track of the
remaining sum. A valid combination is found when the remaining sum becomes 0.
"""

def find_power_sum(target ,power, current_sum, next_number)->int:
    # found valid combination
    if current_sum == target:
        return 1

    # current sum exceeded the target
    if current_sum > target:
        return 0

    if next_number ** power > target:
        return 0

    # include the current number
    include = find_power_sum(target, power, current_sum + (next_number**power), next_number+1)

    # exclude the current number
    exclude = find_power_sum(target, power, current_sum, next_number+1)

    return include + exclude

if __name__ == "__main__":
    target = 10
    power = 2
    print(find_power_sum(target, 2, 0, 1))
