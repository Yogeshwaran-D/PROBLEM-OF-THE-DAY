class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curmin , curmax = arrays[0][0] , arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
            arr = arrays[i]
            res = max( res ,arr[-1] - curmin , curmax - arr[0])
            curmin = min( arr[0] , curmin )
            curmax = max( arr[-1] , curmax )
        return res