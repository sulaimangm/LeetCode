class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [0]*len(matrix)
        column = [0]*len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row[r] = 1
                    column[c] = 1
        print(row, column)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if column[c] == 1 or row[r] == 1:
                    matrix[r][c] = 0


