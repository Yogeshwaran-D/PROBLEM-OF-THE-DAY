class Solution:
    def possible(self,bloomDay, day, m, k):
        n = len(bloomDay) 
        cnt = 0
        noOfB = 0
        for i in range(n):
            if bloomDay[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m
    def minDays(self, bloomDay, m, k) :
        val = m * k
        n = len(bloomDay)  
        if val > n:
            return -1  
        mini = float('inf')
        maxi = float('-inf')
        for i in range(n):
            mini = min(mini, bloomDay[i])
            maxi = max(maxi, bloomDay[i])
        low = mini
        high = maxi
        while low <= high:
            mid = (low + high) // 2
            if self.possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        return low