class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 'L' and (r, c) not in visited:
                visited.add((r, c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1

        return island_count
