"""
Author : Janarddan Sarkar
File_name = 1. print_name_ntimes.py
Date : 28-02-2024
Description :  print your name N times using recursion
"""


def print_name(n:int, name:str):
    if n > 0:
        print_name(n-1, name)

    print(name)


"""
Time Complexity: O(N) { Since the function is being called n times, and for each function, 
                 we have only one printable line that takes O(1) time, so the cumulative
                  time complexity would be O(N) }
Space Complexity: O(N) { In the worst case, the recursion stack space would be full with all 
                  the function calls waiting to get completed and that would make it an O(N) 
                  recursion stack space }.
"""


if __name__ == "__main__":
    print_name(4, 'janarddan')
