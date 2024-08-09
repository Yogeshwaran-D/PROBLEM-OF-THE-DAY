class Solution:
    def valid(self, grid , r , c ):
        count=set()
        for i in range(r,r+3):
            for j in  range(c,c+3):
                if grid [i] [j] in count or not(0 < grid [i] [j] < 10) :
                   return 0
                count.add(grid [i] [j])
        
        for i in range(r , r+3):
            if sum(grid[i][c:c+3]) != 15:
                return 0
        
        for i in range(c,c+3):
            if grid [r] [i] + grid [r+1] [i] + grid [r+2] [i] != 15 :
                return 0
        if (
            grid [r] [c] + grid [r+1] [c+1] + grid [r+2] [c+2] != 15 or
            grid [r] [c+2] + grid [r+1] [c+1] + grid [r+2] [c] != 15 
        ):
            return 0

        return 1
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid [0])
        res = 0
        for r in range(rows-2):
            for c in range(cols-2):
                res+=self.valid(grid,r,c)
        return res