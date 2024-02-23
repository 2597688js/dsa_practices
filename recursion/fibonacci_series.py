"""
Author : Janarddan Sarkar
File_name = fibonacci_series.py
Date : 21-02-2024
Description :  0 1 1 2 3 5 8 13 21 i.e.,   n = (n-1) + (n-2)

        Two approaches : 1. using loops
                         2. using recursion
"""


# 1. using loops
def get_fibonacci_series(n_terms):
    """
    n_terms : how many terms we need in the fibonacci series
    """
    a, b = 0, 1

    fibonacci_numbers_l = [a, b]
    for _ in range(n_terms):
        next_term = a + b
        fibonacci_numbers_l.append(next_term)
        a = b
        b = next_term

    return fibonacci_numbers_l


# 2. using recursion
def get_fibonacci_series_using_recursion(n:int):
    def fibonacci(n):
        if n < 1:
            return False
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    fib_series = [fibonacci(i) for i in range(1, n + 1)]

    return fib_series


if __name__ == "__main__":
    # fibonacci_lst = get_fibonacci_series(8)
    # print(fibonacci_lst)

    fibonacci_series = get_fibonacci_series_using_recursion(5)
    print(fibonacci_series)
