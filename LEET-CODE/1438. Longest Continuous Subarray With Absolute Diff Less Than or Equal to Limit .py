from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums, limit) :
        N=len(nums)
        sl=SortedList()
        left,size=0,0
        for right in range(N):
            sl.add(nums[right])
            while sl[-1]-sl[0]>limit:
                sl.remove(nums[left])
                left+=1
            size=max(size,right-left+1)
        return size