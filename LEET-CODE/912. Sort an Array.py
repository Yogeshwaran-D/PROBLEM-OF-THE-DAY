class Solution:
    
    def sortArray(self, nums) :
        def merge(low,mid,high,nums):
            i=low
            j=mid
            mix=[]
            while i < mid and j< high :
                if nums[i] < nums[j]:
                    mix.append(nums[i])
                    i+=1
                else:
                    mix.append(nums[j])
                    j+=1
            while i < mid :
                mix.append(nums[i])
                i+=1
            while j< high :
                mix.append(nums[j])
                j+=1
            for k in range(len(mix)):
                nums[low+k]=mix[k]
        def mergeSort(low,high,nums):
            if high-low == 1:
                return
            mid= (low + high)//2
            mergeSort(low,mid,nums)
            mergeSort(mid,high,nums)
            merge(low,mid,high,nums)
        mergeSort(0,len(nums),nums)
        return nums