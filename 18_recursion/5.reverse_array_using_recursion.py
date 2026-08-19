"""
Author : janarddan
File_name = 5.reverse_array_using_recursion.py
Date : 27/07/26
Description :

"""

def reverse_arr_using_recusrion(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    return reverse_arr_using_recusrion(arr, left + 1, right - 1)

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8,9]
    reverse_arr_using_recusrion(arr1, 0, len(arr1)-1)
    print("Reversed array (using Recursion) :", arr1)
    print()
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_arr_using_recusrion(arr1, 2, 5)
    print("Reversed array (using Recursion) :", arr1)
    print()
    arr2 = [1]
    reverse_arr_using_recusrion(arr1, 0, len(arr2) - 1)
    print("Reversed array (using Recursion) :", arr2)
    print()
    arr3= [1, 1, 1, 1]
    reverse_arr_using_recusrion(arr1, 0, len(arr3) - 1)
    print("Reversed array (using Recursion) :", arr3)
    print()
    arr4 = []
    reverse_arr_using_recusrion(arr1, 0, len(arr4) - 1)
    print("Reversed array (using Recursion) :", arr4)