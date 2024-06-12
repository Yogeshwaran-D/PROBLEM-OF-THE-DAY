class Solution:
    def sortColors(self, nums):
            l,r=0,len(nums)-1
            i=0
            while(i<=r):
                if nums[i] == 0 :
                    nums[l],nums[i] = nums[i],nums[l]
                    l+=1
                elif nums[i] == 2 :
                    nums[r],nums[i] = nums[i],nums[r]
                    r-=1
                    i-=1
                i+=1