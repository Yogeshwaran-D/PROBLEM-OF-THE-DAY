class Solution:
    def minimumDeletions(self, s: str) -> int:
        N=len(s)
        res=N
        a_count=[0]*N
        count=0
        for i in range(N-1,-1,-1):
            a_count[i] = count
            if s[i] == "a":
                count+=1
        deletion=0
        for i in range(N):
            res=min(res,deletion+a_count[i])
            if s[i] == "b":
                deletion+=1
        return res