"""
Author : janarddan
File_name = 0.1_basic_2d_array.py
Date : 22/07/26
Description :

"""


def print_2d_array_diagonal_elements(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if i == j:
                print(arr[i][j])


def print_2d_upper_triangular_elements(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if j>=i:
                print(arr[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

def print_2d_transpose(arr):

    row = len(arr)
    col = len(arr[0])

    transposed_arr = [[0] * row for _ in range(col)]


    for i in range(col):
        for j in range(row):
            transposed_arr[i][j] = arr[j][i]
            # print(arr[j][i], end=" ")

        # print()
    print(transposed_arr)

if __name__ == "__main__":
    arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = len(arr_2d)
    col = len(arr_2d[0])

    print(f"Size of the array: \tRow x Column : {len(arr_2d)} x {len(arr_2d[0])}")

    print_2d_array_diagonal_elements(arr_2d)
    print()
    print_2d_upper_triangular_elements(arr_2d)
    print()
    arr1 = [[1,2], [3,4], [5,6]]
    print_2d_transpose(arr1)
    