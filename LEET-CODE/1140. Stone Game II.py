class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs( Alice , index , M ):
            if index == len(piles):
                return 0
            if ( Alice , index , M ) in dp :
                return dp[ ( Alice , index , M ) ]
            res = 0 if Alice else float('inf')
            total = 0
            for i in range( 1 , ( 2 * M ) + 1 ):
                if index + i -1 == len(piles):
                    break
                total += piles[ index + i - 1 ]
                if Alice :
                    res = max( res , total + dfs( not Alice , index + i , max( M , i ) ) )
                else:
                    res = min( res , dfs( not Alice , index + i , max( M , i ) ) )
            dp[ ( Alice , index , M ) ] = res
            return res
        return dfs( True , 0 , 1 )