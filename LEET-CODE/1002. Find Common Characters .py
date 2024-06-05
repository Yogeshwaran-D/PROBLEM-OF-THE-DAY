from typing import Counter


class Solution:
    def commonChars(self, words):
        res=[]
        arr=[]
        for word in words :
            arr.append(Counter(word))
        temp=arr[0]
        for i in temp.keys():
            minValue=100
            for word in arr:
                minValue = min(word.get(i,0),minValue)
            for j in range(minValue):
                res.append(i)
        return res