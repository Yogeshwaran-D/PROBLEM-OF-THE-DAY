class Solution:
    def numberOfSubarrays(self, nums, k) :
        count,left,mid,n=0,0,0,0
        for right in range(len(nums)):
            if nums[right] % 2 :
                n+=1
            while n > k:
                if nums[left] % 2 :
                    n-=1
                left+=1
                mid=left
            if n == k :
                while not nums[mid] % 2 :
                    mid+=1
                count+=(mid-left+1)
        return count

# Time Complexity  : O(N)
# Space Complexity : O(1)