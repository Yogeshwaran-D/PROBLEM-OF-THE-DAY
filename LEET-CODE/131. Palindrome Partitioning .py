class Solution:
    def partition(self, s) :
        res=[]
        part=[]
        self.n=len(s)
        def isPali(s,l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        def substring(index):
            if index == self.n:
                res.append(part.copy())
                return 
            for j in range(index,self.n):
                if isPali(s,index,j):
                    part.append(s[index:j+1])
                    substring(j+1)
                    part.pop()
        substring(0)
        return res