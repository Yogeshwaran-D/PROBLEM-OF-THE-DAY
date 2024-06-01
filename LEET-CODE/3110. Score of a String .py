class Solution:
    def scoreOfString(self, s):
        n=len(s)
        sum=0
        for i in range(n-1):
            sum+=abs(ord(s[i])-ord(s[i+1]))
        return sum