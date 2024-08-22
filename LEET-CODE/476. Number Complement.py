class Solution:
    def findComplement(self, num: int) -> int:
        com=""
        while num > 0 :
            if num % 2 :
                com=str(0)+com
            else:
                com=str(1)+com
            num//=2
        res=0
        for i in range(1,len(com)+1):
            if com[-i] == "1":
                res+=2 ** (i-1)
        return res