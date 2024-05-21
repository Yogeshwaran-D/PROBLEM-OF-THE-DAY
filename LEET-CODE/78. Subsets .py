class Solution:
    def subsets(self, nums):
        self.ans=[]
        self.n=len(nums)
        def subset(index,temp):
            if index == self.n :
                self.ans.append(temp.copy())
                return
            temp.append(nums[index])
            subset(index+1,temp)
            temp.pop()
            subset(index+1,temp)
        subset(0,[])
        return self.ans