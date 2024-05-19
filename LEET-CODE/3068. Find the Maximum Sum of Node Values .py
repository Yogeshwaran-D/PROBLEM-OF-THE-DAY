class Solution:
    def maximumValueSum(self, nums, k, edges) :
        res = sum ( nums )
        arr = [ ( x ^ k ) - x for x in nums]
        arr.sort ( reverse = True )
        for i in range ( 0 , len ( nums ) , 2 ) :
            if i == len ( nums ) - 1 :
                break
            temp = arr [ i ] + arr [ i + 1 ]
            if temp <= 0 :
                break
            res += temp
        return res