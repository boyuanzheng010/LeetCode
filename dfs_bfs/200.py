"""
With Recursion
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i_, j_):
            if i_ < 0 or i_ > len(grid) - 1:
                return
            if j_ < 0 or j_ > len(grid[0]) - 1:
                return
            if grid[i_][j_] != '1':
                return

            grid[i_][j_] = "#"
            dfs(i_ - 1, j_)
            dfs(i_ + 1, j_)
            dfs(i_, j_ - 1)
            dfs(i_, j_ + 1)

        if not grid:
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count