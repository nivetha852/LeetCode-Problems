class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        empty = 0
        start_row = 0
        start_col = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1

                if grid[r][c] == 1:
                    start_row = r
                    start_col = c

        def dfs(r, c, empty):
            
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == -1):
                return 0

            
            if grid[r][c] == 2:
                return 1 if empty == 0 else 0

            temp = grid[r][c]

            if grid[r][c] == 0:
                empty -= 1

            
            grid[r][c] = -1

            paths = (
                dfs(r + 1, c, empty) +  # Down
                dfs(r - 1, c, empty) +  # Up
                dfs(r, c + 1, empty) +  # Right
                dfs(r, c - 1, empty)    # Left
            )

            
            grid[r][c] = temp

            return paths

        return dfs(start_row, start_col, empty)