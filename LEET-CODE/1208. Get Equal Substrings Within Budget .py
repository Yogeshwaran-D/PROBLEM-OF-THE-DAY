class Solution:
    def equalSubstring(self, s, t, maxCost) :
        CurrentCost=0
        l=0
        res=0
        for r in range(len(s)):
            CurrentCost+= abs(ord(s[r])-ord(t[r]))
            while CurrentCost> maxCost :
                CurrentCost -= abs(ord(s[l])-ord(t[l]))
                l+=1
            res=max(res,r-l+1)
        return res