class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res=[]
        n1,n2=len(nums1),len(nums2)
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums2[j]<nums1[i]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res
# Time : NLog(N)