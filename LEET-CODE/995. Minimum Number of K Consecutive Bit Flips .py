class Solution:
    def minKBitFlips(self, nums, k) :
        N=len(nums)
        flip=[False]*N  
        flips=0
        current=0
        for i,x in enumerate(nums):
            if flip[i]:
                current^=1
            if (x^current) == 0 : #This means that we flip x bit
                flips+=1
                current ^=1
                if i+k >N:
                    return -1
                if i+k <N:
                    flip[i+k]=True
        return flips



s=Solution()
print(s.minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3))