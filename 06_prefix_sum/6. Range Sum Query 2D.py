"""
Author : janarddan
File_name = 6. Range Sum Query 2D.py
Date : 30/08/26
Description :

Leetcode 304: https://leetcode.com/problems/range-sum-query-2d-immutable/description/
"""


class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

        rows = len(self.matrix)
        cols = len(self.matrix[0])

        self.prefix_matrix = []

        # ---- Loop -----
        # for _ in range(rows):
        #     row = []
        #     for _ in range(cols):
        #         row.append(0)
        #
        #     self.prefix_matrix.append(row)

        # --- List comprehension ---
        """
        The calculation of prefix matrix takes 
        Time: O(m × n)
        Space: O(m × n). 
        """
        self.prefix_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                # --- list comprehension ---
                top = self.prefix_matrix[r-1][c] if r > 0 else 0
                left = self.prefix_matrix[r][c-1] if c > 0 else 0
                diag = self.prefix_matrix[r-1][c-1] if r > 0 and c > 0 else 0

                # --- normal loop ---
                # if r > 0:
                #     top = self.prefix_matrix[r-1][c]
                # else:
                #     top = 0
                #
                # if c > 0:
                #     left = self.prefix_matrix[r][c-1]
                # else:
                #     left = 0


                # if r > 0 and c > 0:
                #     diag = self.prefix_matrix[r - 1][c - 1]
                # else:
                #     diag = 0
                self.prefix_matrix[r][c] = self.matrix[r][c] + top + left - diag


    def sumRegionBruteforce(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Complexity

        For a region of height H and width W:

        Time: O(H × W) per query => O(H x W x Q)
        Space: O(1)
        """
        total = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]

        return total

    def sumRegionOptimal(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Complexity:

        Prefix matrix construction:
            Time: O(m × n)
            Space: O(m × n)

        Per query:
            Time: O(1)
            Space: O(1)

        For Q queries:
            Total Time: O(m × n + Q)
            Space: O(m × n)

        """
        topRegionSum = self.prefix_matrix[row1 - 1][col2] if row1 > 0 else 0
        leftRegionSum = self.prefix_matrix[row2][col1 - 1] if col1 > 0 else 0
        overlappingSum = self.prefix_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        regionSum = self.prefix_matrix[row2][col2] - topRegionSum - leftRegionSum + overlappingSum
        return regionSum


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    row1, col1, row2, col2 = 2, 1, 4, 3

    obj = NumMatrix(matrix)
    print(obj.sumRegionBruteforce(2, 1, 4, 3))
    print()
    print(obj.sumRegionOptimal(2, 1, 4, 3))
    print(obj.sumRegionOptimal(0, 0, 2, 3))
