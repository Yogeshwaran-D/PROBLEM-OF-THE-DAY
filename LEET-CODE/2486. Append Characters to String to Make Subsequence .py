class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        n=len(t)
        for ele in s:
            if i == n :
                return 0
            if t[i] == ele :
                i+=1
        return n-i