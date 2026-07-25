"""
Author : Janarddan Sarkar
file_name : 1.fibonacci_sequence.py 
date : 28-11-2024
description : Implementation of fibonacci sequence using
                1. Recursion
                2. Dynamic programming -  both memoization(top-down) approach
                                            and tabulation(bottom-up) approach
"""


def fibonacci_recursion(n):
    if n == 0:  # Base case for F(0)
        return 0
    if n == 1:  # Base case for F(1)
        return 1

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_tabulation(n):
    dp = {}

    dp[0] = 0  # base case for f(0) = 0
    dp[1] = 1  # base case for f(1) = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def fibonacci_tabulation_space_optimized(n):
    if n == 0:  # Base case for F(0)
        return 0
    if n == 1:  # Base case for F(1)
        return 1

    # Initialize variables for F(n-2) and F(n-1)
    prev2, prev1 = 0, 1

    # Compute Fibonacci iteratively
    for _ in range(2, n + 1):
        current = prev1 + prev2  # F(n) = F(n-1) + F(n-2)
        prev2, prev1 = prev1, current  # Update previous values

    return prev1  # F(n) is stored in prev1

def fibonacci_memoization(n, dp_memo):
    '''
    Top - down approach
    '''

    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in dp_memo:
        dp_memo[n] = fibonacci_memoization(n-1, dp_memo) + fibonacci_memoization(n-2, dp_memo)

    return dp_memo[n]


if __name__ == "__main__":
    print(fibonacci_recursion(5))
    print(fibonacci_tabulation(5))
    print(fibonacci_tabulation_space_optimized(5))
    dp_memo = {}
    print(fibonacci_memoization(5, dp_memo))
    print(fibonacci_memoization(10, dp_memo))
