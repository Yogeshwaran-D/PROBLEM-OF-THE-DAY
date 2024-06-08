class Solution:
    def checkSubarraySum(self, nums, k) :
        new_dict={0:-1}
        Total=0
        for i in range(len(nums)):
            Total+=nums[i]
            rem=Total % k
            if rem not in new_dict:
                new_dict[rem]=i
            elif i - new_dict[rem] > 1 :
                return True
        return False