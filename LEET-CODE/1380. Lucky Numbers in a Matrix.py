class Solution:
    def luckyNumbers (self, matrix):
        res=[]
        for row in range(len(matrix)):
            minValue=0
            for col in range(1,len(matrix[0])):
                if matrix[row][col]<matrix[row][minValue]:
                    minValue=col
            lucky=True
            r=0
            while r<len(matrix):
                if matrix[r][minValue]>matrix[row][minValue]:
                    lucky=False
                    break
                r+=1
            if lucky :
                res.append(matrix[row][minValue])
        return res