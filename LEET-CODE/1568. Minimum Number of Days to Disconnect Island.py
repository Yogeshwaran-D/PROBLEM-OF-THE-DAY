class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c,visited):
            visited.add((r,c))
            neighbor=[[-1,0],[1,0],[0,-1],[0,1]]
            for nr,nc in neighbor:
                nr+=r
                nc+=c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] and (nr,nc) not in visited:
                    dfs(nr,nc,visited)
        count=0
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c)not in visited:
                    dfs(r,c,visited)
                    count+=1
        if count != 1:
            return 0
        land=list(visited)
        for r,c in land:
            grid[r][c]=0
            visited=set()
            count=0
            for r2 in range(rows):
                for c2 in range(cols):
                    if grid[r2][c2] and (r2,c2)not in visited:
                        dfs(r2,c2,visited)
                        count+=1
            if count != 1:
                return 1
            grid[r][c]=1
        return 2