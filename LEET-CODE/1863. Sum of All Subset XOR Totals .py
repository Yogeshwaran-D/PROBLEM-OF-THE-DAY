class Solution:
    def subsetXORSum(self, nums) :
        self.Totalsum=0
        n=len(nums)-1
        def subset(nums,index,n,temp):
            if index > n:
                self.Totalsum+=temp
                return
            subset(nums,index+1,n,temp^nums[index])
            subset(nums,index+1,n,temp)
        subset(nums,0,n,0)
        return self.Totalsum