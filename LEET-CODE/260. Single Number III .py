from typing import Counter

class Solution:
    def singleNumber(self, nums) :
        s=Counter(nums)
        res=[]
        for i,j in s.items():
            if j==1:
                res.append(i)
        return res