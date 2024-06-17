from cmath import sqrt


class Solution:
    def judgeSquareSum(self, c):
        low=0
        high=int(sqrt(c))
        while low<=high:
            temp=low*low + high*high    
            if temp == c:
                return True
            if temp>c:
                high-=1
            else:
                low+=1
        return False
