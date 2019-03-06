# SOLVED
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        columns = []
        rows = []

        for r in range(0, m):
            c = [i for i, e in enumerate(matrix[r]) if e == 0]
            if c:
                rows.append(r)
                columns.extend(c)
                matrix[r] = [0] * n

        columns = set(columns)
        rows = set(rows)
        rows_to_visit = [x for x in range(0, m) if x not in rows]

        for c in columns:
            for r in rows_to_visit:
                matrix[r][c] = 0
