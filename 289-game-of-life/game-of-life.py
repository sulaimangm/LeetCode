class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nboard = [row.copy() for row in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbours = 0
                for r in range(i-1, i+2):
                    for c in range(j-1, j+2):
                        if ((r == i and c == j) or r < 0 or c < 0 or r == len(board) or c == len(board[0])):
                            continue
                        neighbours += board[r][c]
                if board[i][j] == 1:
                    if neighbours < 2 or neighbours > 3:
                        nboard[i][j] = 0
                else:
                    if neighbours == 3:
                        nboard[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = nboard[i][j]
