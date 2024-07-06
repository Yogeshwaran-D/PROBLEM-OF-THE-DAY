class Solution:
    def passThePillow(self, n, time):
        if (time//(n-1)) % 2 == 0 :
            return ((time%(n-1))+1)
        else:
            return (n-(time%(n-1)))