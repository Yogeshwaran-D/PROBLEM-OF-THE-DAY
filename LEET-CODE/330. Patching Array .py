class Solution:
    def minPatches(self, nums, n) :
        TotalSum,count,i=0,0,0
        N=len(nums)
        while TotalSum<n:
            if i<N and nums[i] <= TotalSum+1:
                TotalSum+=nums[i]
                i+=1
            else:
                TotalSum+=(TotalSum+1)
                count+=1
        return count
