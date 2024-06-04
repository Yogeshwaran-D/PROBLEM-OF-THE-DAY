class Solution:
    def longestPalindrome(self, s: str) -> int:
            count={}
            res=0
            for ele in s :
                count[ele]=1+count.get(ele,0)
                if count.get(ele)%2 == 0:
                    res+=2
            for j in count.values():
                if j%2 == 1:
                    res+=1
                    break
            return res