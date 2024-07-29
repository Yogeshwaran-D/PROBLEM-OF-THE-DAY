class Solution:
    def numTeams(self, rating):
        res=0
        N=len(rating)
        for j in range(N):
            asc_left,dsc_left,asc_right,dsc_right=0,0,0,0
            for i in range(j):
                if rating[i]<rating[j]:
                    asc_left+=1
                else:
                    dsc_left+=1
            for k in range(j+1,N):
                if rating[k]>rating[j]:
                    asc_right+=1
                else:
                    dsc_right+=1
            res+=asc_left*asc_right
            res+=dsc_left*dsc_right
        return res