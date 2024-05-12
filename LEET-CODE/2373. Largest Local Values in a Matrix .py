class Solution:
    def largestLocal(self, grid):
        n=len(grid)
        maxLocal=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                tempMax=0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if tempMax < grid[k][l]:
                            tempMax=grid[k][l]
                maxLocal[i][j]=tempMax
        return maxLocal