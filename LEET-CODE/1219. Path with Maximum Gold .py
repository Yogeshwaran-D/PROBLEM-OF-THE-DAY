class Solution:

    def getMaximumGold(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        def dfs(r, c, visit):
            if (r < 0 or r >= n or c < 0 or c >= m or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            res = grid[r][c]
            neighbour = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            
            max_gold_from_neighbours = 0
            for r2, c2 in neighbour:
                max_gold_from_neighbours = max(max_gold_from_neighbours, dfs(r2, c2, visit))
            
            visit.remove((r, c))
            return res + max_gold_from_neighbours

        max_gold_collected = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    max_gold_collected = max(max_gold_collected, dfs(r, c, set()))
                    
        return max_gold_collected