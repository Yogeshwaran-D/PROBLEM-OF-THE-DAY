class Solution:
    def maximumImportance(self, n, roads) :
        edg_count=[0]*n
        for n1,n2 in roads:
            edg_count[n1]+=1
            edg_count[n2]+=1
        res=0
        label=1
        for count in sorted(edg_count):
            res+=label*count
            label+=1
        return res