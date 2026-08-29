class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        black_cells = []
        whites = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    black_cells.append((i,j))
                elif grid[i][j] == 1:
                    whites += 1
        
        minutes = 0
        moves = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        if not whites:
            return 0
        while black_cells:
            new_blacks = []
            for x, y in black_cells:
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        whites -= 1
                        new_blacks.append((nx, ny))
            if new_blacks:
                minutes += 1
            black_cells = new_blacks
        return minutes if not whites else -1
