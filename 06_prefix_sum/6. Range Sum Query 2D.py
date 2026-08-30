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

    def sumRegionBruteforce(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Complexity

        For a region of height H and width W:

        Time: O(H × W) per query
        Space: O(1)
        """
        total = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]

        return total




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