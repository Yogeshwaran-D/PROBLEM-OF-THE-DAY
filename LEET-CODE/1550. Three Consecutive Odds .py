class Solution:
    def threeConsecutiveOdds(self, arr):
        low,end = 0,0
        N = len(arr)
        while end < N :
            if arr[end] % 2 == 0 :
                low = end
                while low<N and arr[low] % 2 == 0:
                    low+=1
                end=low
            if (end-low+1) == 3 :
                return True
            end+=1
        return False
