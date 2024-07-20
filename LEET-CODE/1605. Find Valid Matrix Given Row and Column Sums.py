class Solution:
    def restoreMatrix(self, rowSum, colSum):
        row,col=len(rowSum),len(colSum)
        matrix=[[0]*col for _ in range(row)]
        for r in range(row):
            matrix[r][0]=rowSum[r]
        for c in range(col):
            cur_col_Sum=0
            for r in range(row):
                cur_col_Sum+=matrix[r][c]
            r=0
            while cur_col_Sum > colSum[c]:
                diff=cur_col_Sum-colSum[c]
                max_shift=min(diff,matrix[r][c])
                matrix[r][c]-=max_shift
                matrix[r][c+1]+=max_shift
                cur_col_Sum-=max_shift
                r+=1
        return matrix