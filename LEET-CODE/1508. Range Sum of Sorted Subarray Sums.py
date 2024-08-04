class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subArray=[]
        for i in range(n):
            temp=0
            for j in range(i,n):
                temp+=nums[j]
                subArray.append(temp)
        subArray.sort()
        total_sum=0
        for i in range(left-1,right):
            total_sum+=subArray[i]
        return total_sum % ((10**9)+7)