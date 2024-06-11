from typing import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2) :
        arr2_set=set(arr2)
        count={}
        end=[]
        res=[]
        for ele in arr1:
            if ele not in arr2_set:
                end.append(ele)
            else:
                count[ele]=1+count.get(ele,0)
        end.sort()
        for ele in arr2:
            for _ in range(count[ele]):
                res.append(ele)
        return res+end