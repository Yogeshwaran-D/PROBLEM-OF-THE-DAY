class Solution:
    def subarraysDivByK(self, nums, k):
        TotalSum=0
        count={0:1}
        res=0
        for i in nums:
            TotalSum+=i
            rem=TotalSum % k
            if count.get(rem):
                res+=count.get(rem)
                count[rem]=1+count.get(rem)
            else:
                count[rem]=1
        return res