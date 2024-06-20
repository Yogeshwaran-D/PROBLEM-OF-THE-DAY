class Solution:
    def maxDistance(self, position, m) :
        INF= -(10**20)
        position.sort()
        low=1
        high=position[-1]-position[0]
        def good(mid):
            balls=0
            last_basket= INF
            for b in position:
                if b-last_basket >= mid :
                    balls+=1
                    last_basket=b
            return balls>=m
        while low<high:
            mid=(low+high+1)//2
            if good(mid):
                low=mid
            else:
                high=mid-1
        return low
    # def maxDistance(self, position, m):
    #     position.sort()
    #     lo, hi = 1, (position[-1] - position[0]) // (m - 1)
    #     ans = 1
        
    #     while lo <= hi:
    #         mid = lo + (hi - lo) // 2
    #         if self.canWePlace(position, mid, m):
    #             ans = mid
    #             lo = mid + 1
    #         else:   
    #             hi = mid - 1
        
    #     return ans
    
    # def canWePlace(self, arr, dist, balls):
    #     countBalls = 1
    #     lastPlaced = arr[0]
    #     for i in range(1, len(arr)):
    #         if arr[i] - lastPlaced >= dist:
    #             countBalls += 1
    #             lastPlaced = arr[i]
    #         if countBalls >= balls:
    #             return True
    #     return False
        