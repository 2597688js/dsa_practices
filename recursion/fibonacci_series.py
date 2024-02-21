"""
Author : Janarddan Sarkar
File_name = fibonacci_series.py
Date : 21-02-2024
Description :  0 1 1 2 3 5 8 13 21 i.e.,   n = (n-1) + (n-2)
"""


def get_fibonacci_sereis(n_terms):
    """
    n_terms : how many terms we need in the fibonacci series
    """
    a, b = 0, 1

    fibonacci_numbers_l = []
    fibonacci_numbers_l.append(a)
    fibonacci_numbers_l.append(b)
    for _ in range(n_terms):
        next_term = a + b
        fibonacci_numbers_l.append(next_term)
        a = b
        b = next_term


    return fibonacci_numbers_l


if __name__ == "__main__":
    fibonacci_lst = get_fibonacci_sereis(8)
    print(fibonacci_lst)

