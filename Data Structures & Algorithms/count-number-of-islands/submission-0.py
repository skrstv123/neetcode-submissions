from collections import defaultdict as df
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        bd = df(bool)
        moves = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        def dfs(rx,cy):
            nonlocal r,c, grid
            if rx >= r or rx < 0 or cy >= c or cy < 0:
                return
            if grid[rx][cy] != '1' or bd[rx, cy]:
                return
            bd[rx, cy] = True
            for dr,dc in moves:
                dfs(rx + dr, cy + dc)
        num_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not bd[i,j]:
                    num_islands += 1
                    dfs(i,j)
        return num_islands