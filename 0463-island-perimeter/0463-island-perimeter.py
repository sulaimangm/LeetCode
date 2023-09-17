class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    perimeter += 4
                    if row == 0 and col == 0:
                        continue
                    elif row == 0:
                        if grid[row][col-1] == 1:
                            perimeter -= 2
                    elif col == 0:
                        if grid[row-1][col] == 1:
                            perimeter -= 2
                    else:
                        if grid[row][col-1] == 1:
                            perimeter -= 2
                        if grid[row-1][col] == 1:
                            perimeter -= 2
        return perimeter

