class Solution:
    def specialArray(self, nums) :
        nums.sort()
        i=0
        preValue=-1
        TotalRightEle=len(nums)
        while i< len(nums) :
            if nums[i] == TotalRightEle or (preValue <TotalRightEle < nums[i] ) :
                return TotalRightEle
            while i+1<len(nums) and  nums[i] == nums[i+1] :
                i+=1
            preValue=nums[i]
            i+=1
            TotalRightEle=len(nums)-i
            
        return -1