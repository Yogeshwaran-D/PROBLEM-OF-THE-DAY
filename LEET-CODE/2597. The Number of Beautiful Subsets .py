from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums, k) :
        self.n=len(nums)
        def subset(i,count):
            if i == self.n:
               return 1
            res=subset(i+1,count)
            if not count[nums[i]-k] and not count[nums[i]+k]:
                count[nums[i]]+=1
                res+=subset(i+1,count)
                count[nums[i]]-=1
            return res
        return subset(0,defaultdict(int))-1
