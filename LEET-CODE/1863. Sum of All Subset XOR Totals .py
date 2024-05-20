class Solution:
    def subsetXORSum(self, nums) :
        n=len(nums)
        def subset(index,temp):
            if index == n:
                return temp
            return subset(index+1,temp^nums[index])+subset(index+1,temp)
        return subset(0,0)