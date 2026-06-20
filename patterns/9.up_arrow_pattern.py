"""
Author : Janarddan Sarkar
File_name = up_arrow_pattern.py
Date : 17-06-2026
Description :            *
                       * * *
                     * * * * *
                   * * * * * * *
                       * * *
                       * * *
                       * * *
                       * * *
                       * * *
                       * * *
                       * * *
                       * * *
                       * * * 
"""
def up_arrow_pattern(num_row, piller_width):
    """

    :param num_row: number of rows
    :param piller_width: How broad the pillar is.
    """
    n_row_triangle = int(num_row * 0.4)
    n_row_rectangle = int(num_row * 0.6)

    # The triangle part
    for i in range(n_row_triangle):
        # The first decreasing triangle pattern of spaces
        for j in range(i, n_row_triangle-1):
            print(" ", end=" ")

        # increasing patter of *
        for k in range(i+1):
            print("*", end=" ")

        # increasing pattern of *
        for l in range(i):
            print("*", end=" ")

        print()

    triangle_base_width = 2 * n_row_triangle - 1
    pillar_width = piller_width

    left_spaces = (triangle_base_width - pillar_width) // 2

    # The rectangular pillar
    for i in range(n_row_rectangle):
        for j in range(left_spaces):
            print(" ", end=" ")
        for k in range(pillar_width):
            print("*", end=" ")

        print()




if __name__ == "__main__":
    up_arrow_pattern(15, 5)