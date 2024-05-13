class Solution:

    def matrixScore(self, grid):
        m=len(grid)
        n=len(grid[0])
        MaxSum=0
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] = 1 - grid[row][col]
        for col in range(n):
            colOnes=0
            for row in range(m):
                if grid[row][col]==1 :
                    colOnes+=1
            if (m-colOnes)> colOnes :
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]
        for row in range(m):
            temp =''
            for col in range(n):
                temp+=str(grid[row][col])
            MaxSum+=int(temp,2)
        return MaxSum