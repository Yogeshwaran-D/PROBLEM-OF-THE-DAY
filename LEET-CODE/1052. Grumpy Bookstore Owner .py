class Solution:
    def maxSatisfied(self, customers, grumpy, minutes) :
        l=0
        window=0
        maxWindow=0
        satisfied=0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied+=customers[r]
            if r-l+1 > minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            maxWindow=max(maxWindow,window)
        return satisfied+maxWindow